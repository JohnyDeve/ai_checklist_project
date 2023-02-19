from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from ui.base_qt_ui.ui_coordwidget import Ui_CoordWidget


class CoordWidget(QWidget):
    delete = Signal(int)
    redact = Signal(int, str)

    def __init__(self, id_widget: int, item_name: str, parent=None):
        super(CoordWidget, self).__init__(parent)
        self.ui = Ui_CoordWidget()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.item_name = item_name
        self.ui.lineEdit.setText(item_name)
        self.ui.groupBox.setTitle(str(id_widget))

        self.ui.pushButton.clicked.connect(self.press_del)
        self.ui.pushButton_2.clicked.connect(self.press_redact)

    @Slot()
    def press_del(self):
        self.delete.emit(self.id_widget)

    @Slot()
    def press_redact(self):
        if self.ui.lineEdit.isReadOnly():
            self.ui.lineEdit.setReadOnly(False)
        else:
            self.ui.lineEdit.setReadOnly(True)
            txt = self.ui.lineEdit.text()
            self.redact.emit(self.id_widget, txt)
