from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot
from PySide6.QtGui import QIcon

from ui.base_qt_ui.ui_mainwindow import Ui_MainWindow
from ui.coordwidget import CoordWidget

import sqlite3 as sq

with sq.connect('proto.sqlite') as con:
	cur = con.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS checklist(
		id INTEGER PRIMARY KEY,
		item TEXT,
		price REAL
		)''')

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id: int = 0
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('app_icon.png'))

        with sq.connect('proto.sqlite') as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM checklist')
            for row in cur.fetchall():
                max_id = 0
                if row[0] > max_id:
                    max_id = row[0]
                coord_widget = CoordWidget(row[0], row[1])
                self.ui.coordwidget_layout.addWidget(coord_widget)
                coord_widget.delete.connect(self.delete_coordwidget)
                coord_widget.redact.connect(self.redact_coordwidget)

                self.counter_id = max_id

        self.ui.add_pushbutton.clicked.connect(self.add_coordwidget)
        self.ui.clear_pushbutton.clicked.connect(self.clear_area)
        #self.ui.scan_pushbutton.clicked.connect(self.take_photo)

    @Slot()
    def add_coordwidget(self):
        self.counter_id += 1
        coord_widget = CoordWidget(self.counter_id, 'Название продукта...')
        self.ui.coordwidget_layout.addWidget(coord_widget)
        coord_widget.delete.connect(self.delete_coordwidget)
        coord_widget.redact.connect(self.redact_coordwidget)
        with sq.connect('proto.sqlite') as con:
            cur = con.cursor()
            cur.execute('INSERT INTO checklist (id, item, price) VALUES (?, ?, ?)', [self.counter_id, 'Название продукта...', 0])

    @Slot()
    def clear_area(self):
        while self.ui.coordwidget_layout.count() > 0:
            item = self.ui.coordwidget_layout.takeAt(0)
            item.widget().deleteLater()
        self.counter_id = 0
        with sq.connect('proto.sqlite') as con:
            cur = con.cursor()
            cur.execute('DELETE FROM checklist')

    @Slot(int)
    def delete_coordwidget(self, wid: int):
        #print(f'Удаляем виджет с id: {wid}')
        with sq.connect('proto.sqlite') as con:
            cur = con.cursor()
            cur.execute('DELETE FROM checklist WHERE id = (?)', [wid])
        widget = self.sender()
        self.ui.coordwidget_layout.removeWidget(widget)
        widget.deleteLater()

    @Slot(int, str)
    def redact_coordwidget(self, wid: int, text: str):
        #print(f'redact виджет с id: {wid}')
        #widget = self.sender()
        print(wid, " ", text)
        with sq.connect('proto.sqlite') as con:
            cur = con.cursor()
            cur.execute('UPDATE checklist SET item = ? WHERE id LIKE ?', (text, wid))
