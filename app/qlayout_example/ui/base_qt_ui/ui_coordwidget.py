# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_coordwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_CoordWidget(object):
    def setupUi(self, CoordWidget):
        if not CoordWidget.objectName():
            CoordWidget.setObjectName(u"CoordWidget")
        CoordWidget.resize(460, 103)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CoordWidget.sizePolicy().hasHeightForWidth())
        CoordWidget.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        CoordWidget.setFont(font)
        self.verticalLayout = QVBoxLayout(CoordWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(CoordWidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        font2 = QFont()
        font2.setPointSize(9)
        self.lineEdit.setFont(font2)
        self.lineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.lineEdit)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        icon = QIcon()
        icon.addFile(u":/icon/free-icon-pen-4546497.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(40, 40))
        self.pushButton.setStyleSheet(u"border-radius:20px;\n"
"background-color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icon/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(CoordWidget)

        QMetaObject.connectSlotsByName(CoordWidget)
    # setupUi

    def retranslateUi(self, CoordWidget):
        CoordWidget.setWindowTitle(QCoreApplication.translate("CoordWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("CoordWidget", u"GroupBox", None))
        self.lineEdit.setText(QCoreApplication.translate("CoordWidget", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0434\u0443\u043a\u0442\u0430...", None))
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi

