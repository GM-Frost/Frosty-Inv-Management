# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(841, 729)
        Dialog.setStyleSheet(u"#dialogBtn QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"\n"
"background-color:#eaeced;\n"
"border-radius: 10px;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setMouseTracking(True)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(400, 90, 391, 611))
        self.widget_3.setStyleSheet(u"background-color:#003854;\n"
"border-radius:20px;\n"
"")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 51, 41))
        self.label.setStyleSheet(u"background:transparent;")
        self.label.setPixmap(QPixmap(u":/Icons/Icons/log-in.svg"))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 40, 391, 61))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color:#E88D25;\n"
"color: white;\n"
"border-radius:5px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.loginUsername = QLineEdit(self.widget_3)
        self.loginUsername.setObjectName(u"loginUsername")
        self.loginUsername.setGeometry(QRect(50, 150, 301, 71))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(True)
        self.loginUsername.setFont(font1)
        self.loginUsername.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:#fff;\n"
"padding-bottom:7px;\n"
"")
        self.loginPassword = QLineEdit(self.widget_3)
        self.loginPassword.setObjectName(u"loginPassword")
        self.loginPassword.setGeometry(QRect(50, 240, 301, 71))
        self.loginPassword.setFont(font1)
        self.loginPassword.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:#fff;\n"
"padding-bottom:7px;\n"
"")
        self.loginPassword.setEchoMode(QLineEdit.Password)
        self.loginBtn = QPushButton(self.widget_3)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(70, 380, 261, 51))
        font2 = QFont()
        font2.setFamily(u"Terminal")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        font2.setWeight(50)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.loginBtn.setFont(font2)
        self.loginBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.loginBtn.setStyleSheet(u"QPushButton#loginBtn{\n"
"background-color: qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(184,20,27,1), stop:1 rgba(0,0,0,1));\n"
"color:rgba(255,255,255,230);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#loginBtn:hover{\n"
"background-color:qlineargradient(spread:pad, x1:0,y1:0.505682,x2:1,y2:0.477,stop:0 rgba(22,20,20,1),stop:1  rgba(233,7,15,1));\n"
"color:rgba(255,255,255,230);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#loginBtn:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(105,118,132,200);\n"
"}")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(70, 520, 261, 21))
        self.label_3.setStyleSheet(u"color: #fff;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 550, 141, 20))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color:#ed1c24;\n"
"\n"
"background:transparent;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 550, 31, 31))
        self.label_4.setStyleSheet(u"background:transparent;")
        self.label_4.setPixmap(QPixmap(u":/Icons/Icons/phone-forwarded.svg"))
        self.txtLoginError = QLabel(self.widget_3)
        self.txtLoginError.setObjectName(u"txtLoginError")
        self.txtLoginError.setGeometry(QRect(40, 120, 311, 20))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setWeight(75)
        self.txtLoginError.setFont(font4)
        self.txtLoginError.setStyleSheet(u"color: rgb(223, 0, 0);\n"
"background-color:transparent;")
        self.txtLoginError.setAlignment(Qt.AlignCenter)
        self.txtUserError = QLabel(self.widget_3)
        self.txtUserError.setObjectName(u"txtUserError")
        self.txtUserError.setGeometry(QRect(350, 190, 21, 21))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setWeight(75)
        self.txtUserError.setFont(font5)
        self.txtUserError.setStyleSheet(u"background-color:transparent;\n"
"color:red;")
        self.txtUserError.setAlignment(Qt.AlignCenter)
        self.txtPasswordError = QLabel(self.widget_3)
        self.txtPasswordError.setObjectName(u"txtPasswordError")
        self.txtPasswordError.setGeometry(QRect(350, 280, 21, 21))
        self.txtPasswordError.setFont(font5)
        self.txtPasswordError.setStyleSheet(u"#txtPasswordError{\n"
"color:red;\n"
"background-color:transparent;\n"
"}")
        self.txtPasswordError.setAlignment(Qt.AlignCenter)
        self.label_2.raise_()
        self.loginUsername.raise_()
        self.loginPassword.raise_()
        self.loginBtn.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.label_4.raise_()
        self.label.raise_()
        self.txtLoginError.raise_()
        self.txtUserError.raise_()
        self.txtPasswordError.raise_()
        self.headerLogin = QWidget(self.widget)
        self.headerLogin.setObjectName(u"headerLogin")
        self.headerLogin.setGeometry(QRect(0, 0, 821, 71))
        self.headerLogin.setStyleSheet(u"background-color:#003854;")
        self.horizontalLayout = QHBoxLayout(self.headerLogin)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.headerLogin)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(35, 35))
        self.label_9.setMaximumSize(QSize(35, 35))
        self.label_9.setPixmap(QPixmap(u":/Images/Images/Yamaha-Logo.ico"))
        self.label_9.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_9)

        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_10.setFont(font6)
        self.label_10.setStyleSheet(u"color:#E88D25;")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.label_10)


        self.horizontalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.headerLogin)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalSpacer = QSpacerItem(499, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_4.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)

        self.dialogBtn = QFrame(self.headerLogin)
        self.dialogBtn.setObjectName(u"dialogBtn")
        self.dialogBtn.setStyleSheet(u"#closeWindowsBtn:hover{\n"
"background-color:red;\n"
"\n"
"}\n"
"#minimizeWindowsBtn:hover,#restoreWindowsBtn:hover{\n"
"background-color: #24262b;\n"
"}")
        self.dialogBtn.setFrameShape(QFrame.StyledPanel)
        self.dialogBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.dialogBtn)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.minimizeWindowsBtn = QPushButton(self.dialogBtn)
        self.minimizeWindowsBtn.setObjectName(u"minimizeWindowsBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.minimizeWindowsBtn.sizePolicy().hasHeightForWidth())
        self.minimizeWindowsBtn.setSizePolicy(sizePolicy)
        self.minimizeWindowsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeWindowsBtn.setStyleSheet(u"border-radius:none;")
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindowsBtn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.minimizeWindowsBtn)

        self.restoreWindowsBtn = QPushButton(self.dialogBtn)
        self.restoreWindowsBtn.setObjectName(u"restoreWindowsBtn")
        sizePolicy.setHeightForWidth(self.restoreWindowsBtn.sizePolicy().hasHeightForWidth())
        self.restoreWindowsBtn.setSizePolicy(sizePolicy)
        self.restoreWindowsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.restoreWindowsBtn.setStyleSheet(u"border-radius:none;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindowsBtn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.restoreWindowsBtn)

        self.closeWindowsBtn = QPushButton(self.dialogBtn)
        self.closeWindowsBtn.setObjectName(u"closeWindowsBtn")
        sizePolicy.setHeightForWidth(self.closeWindowsBtn.sizePolicy().hasHeightForWidth())
        self.closeWindowsBtn.setSizePolicy(sizePolicy)
        self.closeWindowsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeWindowsBtn.setStyleSheet(u"border-radius:none;")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindowsBtn.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.closeWindowsBtn)


        self.horizontalLayout.addWidget(self.dialogBtn)

        self.txtDatabaseconnection = QLabel(self.widget)
        self.txtDatabaseconnection.setObjectName(u"txtDatabaseconnection")
        self.txtDatabaseconnection.setGeometry(QRect(20, 680, 251, 16))
        font7 = QFont()
        font7.setBold(True)
        font7.setWeight(75)
        self.txtDatabaseconnection.setFont(font7)
        self.txtDatabaseconnection.setStyleSheet(u"color:#2c313c;")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 260, 341, 251))
        self.label_6.setPixmap(QPixmap(u":/Images/Images/App-Logo-Main.png"))
        self.label_6.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.loginUsername.setPlaceholderText(QCoreApplication.translate("Dialog", u"User Name", None))
        self.loginPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
        self.loginBtn.setText(QCoreApplication.translate("Dialog", u"Log In", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Forgot your User Name | Password ?", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Contact: Me", None))
        self.label_4.setText("")
        self.txtLoginError.setText("")
        self.txtUserError.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.txtPasswordError.setText(QCoreApplication.translate("Dialog", u"X", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Dialog", u"INVENTORY PROJECT", None))
#if QT_CONFIG(tooltip)
        self.minimizeWindowsBtn.setToolTip(QCoreApplication.translate("Dialog", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeWindowsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreWindowsBtn.setToolTip(QCoreApplication.translate("Dialog", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.closeWindowsBtn.setToolTip(QCoreApplication.translate("Dialog", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeWindowsBtn.setText("")
        self.txtDatabaseconnection.setText("")
        self.label_6.setText("")
    # retranslateUi

