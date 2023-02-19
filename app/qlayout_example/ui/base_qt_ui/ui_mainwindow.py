# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import res2_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(389, 607)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 80, 371, 435))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 369, 433))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.coordwidget_layout = QVBoxLayout()
        self.coordwidget_layout.setObjectName(u"coordwidget_layout")

        self.horizontalLayout.addLayout(self.coordwidget_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 401, 71))
        self.header.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(223, 25, 151, 20))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label_2 = QLabel(self.header)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(59, 24, 91, 20))
        font2 = QFont()
        font2.setPointSize(13)
        self.label_2.setFont(font2)
        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 20, 31, 31))
        self.label_3.setPixmap(QPixmap(u":/icon/free-icon-connections-7936822.png"))
        self.label_3.setScaledContents(True)
        self.footer = QFrame(self.centralwidget)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(-1, 529, 391, 79))
        self.footer.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.scan_pushbutton = QPushButton(self.footer)
        self.scan_pushbutton.setObjectName(u"scan_pushbutton")
        self.scan_pushbutton.setGeometry(QRect(20, 25, 111, 31))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.scan_pushbutton.setFont(font3)
        self.scan_pushbutton.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(73, 190, 255);")
        self.add_pushbutton = QPushButton(self.footer)
        self.add_pushbutton.setObjectName(u"add_pushbutton")
        self.add_pushbutton.setEnabled(True)
        self.add_pushbutton.setGeometry(QRect(140, 25, 111, 31))
        font4 = QFont()
        font4.setBold(True)
        self.add_pushbutton.setFont(font4)
        self.add_pushbutton.setStyleSheet(u"background-color: rgb(15, 255, 52);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.clear_pushbutton = QPushButton(self.footer)
        self.clear_pushbutton.setObjectName(u"clear_pushbutton")
        self.clear_pushbutton.setGeometry(QRect(260, 25, 111, 31))
        self.clear_pushbutton.setFont(font4)
        self.clear_pushbutton.setStyleSheet(u"background-color: rgb(255, 50, 23);\n"
"border-radius: 15px;\n"
"color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.footer.raise_()
        self.scrollArea.raise_()
        self.header.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI Checklist", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043f\u043e\u043a\u0443\u043f\u043e\u043a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"AI Checklist", None))
        self.label_3.setText("")
        self.scan_pushbutton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.add_pushbutton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clear_pushbutton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

