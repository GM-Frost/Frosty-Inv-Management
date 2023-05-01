# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1550, 986)
        MainWindow.setStyleSheet(u"\n"
"\n"
"*{\n"
"border:none;\n"
"background-color:transparent;\n"
"background:transparent;\n"
"padding:0;\n"
"margin:0;\n"
"color:#fff;\n"
"}\n"
"\n"
"QTableWidget::verticalScrollBar {\n"
"    background-color: #bcc1ce;\n"
"}\n"
"\n"
"QTableWidget::horizontalScrollBar {\n"
"    background-color: #bcc1ce;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color:#bcc1ce;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #bcc1ce;\n"
"}\n"
"#centralwidget{\n"
"background-color:#eaeced;\n"
"\n"
"}\n"
"#leftMenuSubContainer{\n"
"\n"
"background-color: #003854;\n"
"\n"
"}\n"
"\n"
"\n"
"#leftMenuSubContainer QPushButton{\n"
"text-align:left;\n"
"padding:5px 5px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"}\n"
"#frame_3 QPushButton:hover, #frame_2 QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(235,28,36,1), stop:1 rgba(44,49,60,1));\n"
"\n"
"}\n"
"#centerMenuSubContainer,#rightMenuSubContainer{\n"
"bac"
                        "kground-color: qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(54,90,108,1) stop:1 rgba(54,90,108,1));\n"
"}\n"
"#frame_4,#frame_8,#popupNotificationSubContainer,#popupNotificationInformationSubContainer{\n"
"background-color:#003854;\n"
"border-radius:10px;\n"
"}\n"
"#headerContainer,#footerContainer{\n"
"background-color:#003854;\n"
"}\n"
"\n"
"#QTabWidget{\n"
"background-color:#2c313c;\n"
"\n"
"}\n"
"\n"
"#restoreWindowsBtn:hover,#minimizeWindowsBtn:hover{\n"
"background-color:#16191d;\n"
"padding:10px;\n"
"}\n"
"#closeWindowsBtn:hover{\n"
"background-color:red;\n"
"padding:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/***** LOG OUT ******/\n"
"\n"
"\n"
"#logoutBtn{\n"
"padding:10px;\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background: #003854; \n"
"}\n"
" #logoutBtn:hover{\n"
"background: qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(20,140,194,1) , stop:1 rgba(125,204,240,1)); \n"
"\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 0))
        self.leftMenuContainer.setMaximumSize(QSize(43, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/Icons/Icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 0)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.homeBtn.setFont(font)
        self.homeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.homeBtn.setStyleSheet(u"background-color: qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(184,20,27,1), stop:1 rgba(0,0,0,1));")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.serverInvBtn = QPushButton(self.frame_2)
        self.serverInvBtn.setObjectName(u"serverInvBtn")
        self.serverInvBtn.setFont(font)
        self.serverInvBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Icons/server.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.serverInvBtn.setIcon(icon2)
        self.serverInvBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.serverInvBtn)

        self.inUseInvBtn = QPushButton(self.frame_2)
        self.inUseInvBtn.setObjectName(u"inUseInvBtn")
        self.inUseInvBtn.setFont(font)
        self.inUseInvBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/Icons/Icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.inUseInvBtn.setIcon(icon3)
        self.inUseInvBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.inUseInvBtn)

        self.sentForRepairBtn = QPushButton(self.frame_2)
        self.sentForRepairBtn.setObjectName(u"sentForRepairBtn")
        self.sentForRepairBtn.setFont(font)
        self.sentForRepairBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Icons/repeat.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sentForRepairBtn.setIcon(icon4)
        self.sentForRepairBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.sentForRepairBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.adminDashBtn = QPushButton(self.leftMenuSubContainer)
        self.adminDashBtn.setObjectName(u"adminDashBtn")
        self.adminDashBtn.setFont(font)
        self.adminDashBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Icons/admin-dash.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.adminDashBtn.setIcon(icon5)
        self.adminDashBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.adminDashBtn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 0)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setFont(font)
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon6)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.settingsBtn)

        self.informationBtn = QPushButton(self.frame_3)
        self.informationBtn.setObjectName(u"informationBtn")
        self.informationBtn.setFont(font)
        self.informationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/Icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.informationBtn.setIcon(icon7)
        self.informationBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.informationBtn)

        self.helpMenuBtn = QPushButton(self.frame_3)
        self.helpMenuBtn.setObjectName(u"helpMenuBtn")
        self.helpMenuBtn.setFont(font)
        self.helpMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/Icons/Icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpMenuBtn.setIcon(icon8)
        self.helpMenuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpMenuBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(300, 0))
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(300, 0))
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenuBtn = QPushButton(self.frame_4)
        self.closeCenterMenuBtn.setObjectName(u"closeCenterMenuBtn")
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenuBtn.setIcon(icon9)
        self.closeCenterMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeCenterMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.centerMenuPages = QCustomStackedWidget(self.centerMenuSubContainer)
        self.centerMenuPages.setObjectName(u"centerMenuPages")
        self.settingsPage = QWidget()
        self.settingsPage.setObjectName(u"settingsPage")
        self.settingsPage.setStyleSheet(u"\n"
"#adminProfileSettingBtn,#adminChangePasswordBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color: #003854;\n"
"}\n"
" #adminProfileSettingBtn:hover,#adminChangePasswordBtn:hover{\n"
"background-color:#eaeaeb;\n"
"border:1px solid #003854;\n"
"color:#003854;\n"
"}\n"
"\n"
"#adminPasswordWidget QLineEdit{\n"
"color:#fff;\n"
"background-color:#4a768b;\n"
"border:1px solid #4a768b;\n"
"border-radius:5px;\n"
"padding:5px 5px;\n"
"}\n"
"\n"
"#adminPasswordWidget QLineEdit:hover{\n"
"border-color:red;\n"
"}\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.settingsPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_16 = QLabel(self.settingsPage)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_16)

        self.adminPasswordWidget = QWidget(self.settingsPage)
        self.adminPasswordWidget.setObjectName(u"adminPasswordWidget")
        self.verticalLayout_66 = QVBoxLayout(self.adminPasswordWidget)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.widget_79 = QWidget(self.adminPasswordWidget)
        self.widget_79.setObjectName(u"widget_79")

        self.verticalLayout_66.addWidget(self.widget_79)

        self.widget_72 = QWidget(self.adminPasswordWidget)
        self.widget_72.setObjectName(u"widget_72")
        self.horizontalLayout_77 = QHBoxLayout(self.widget_72)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_39 = QLabel(self.widget_72)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font1)

        self.horizontalLayout_77.addWidget(self.label_39, 0, Qt.AlignLeft)

        self.adminSettingsID = QLineEdit(self.widget_72)
        self.adminSettingsID.setObjectName(u"adminSettingsID")
        self.adminSettingsID.setEnabled(False)

        self.horizontalLayout_77.addWidget(self.adminSettingsID, 0, Qt.AlignRight)


        self.verticalLayout_66.addWidget(self.widget_72)

        self.widget_73 = QWidget(self.adminPasswordWidget)
        self.widget_73.setObjectName(u"widget_73")
        self.horizontalLayout_78 = QHBoxLayout(self.widget_73)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.label_44 = QLabel(self.widget_73)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font1)

        self.horizontalLayout_78.addWidget(self.label_44, 0, Qt.AlignLeft)

        self.adminSettingsUsername = QLineEdit(self.widget_73)
        self.adminSettingsUsername.setObjectName(u"adminSettingsUsername")
        self.adminSettingsUsername.setEnabled(True)

        self.horizontalLayout_78.addWidget(self.adminSettingsUsername, 0, Qt.AlignRight)


        self.verticalLayout_66.addWidget(self.widget_73)

        self.widget_82 = QWidget(self.adminPasswordWidget)
        self.widget_82.setObjectName(u"widget_82")
        self.horizontalLayout_87 = QHBoxLayout(self.widget_82)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_51 = QLabel(self.widget_82)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font1)

        self.horizontalLayout_87.addWidget(self.label_51, 0, Qt.AlignLeft)

        self.adminSettingsFname = QLineEdit(self.widget_82)
        self.adminSettingsFname.setObjectName(u"adminSettingsFname")
        self.adminSettingsFname.setEnabled(True)

        self.horizontalLayout_87.addWidget(self.adminSettingsFname, 0, Qt.AlignRight)


        self.verticalLayout_66.addWidget(self.widget_82)

        self.widget_81 = QWidget(self.adminPasswordWidget)
        self.widget_81.setObjectName(u"widget_81")
        self.horizontalLayout_85 = QHBoxLayout(self.widget_81)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_49 = QLabel(self.widget_81)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font1)

        self.horizontalLayout_85.addWidget(self.label_49, 0, Qt.AlignLeft)

        self.adminSettingsLname = QLineEdit(self.widget_81)
        self.adminSettingsLname.setObjectName(u"adminSettingsLname")
        self.adminSettingsLname.setEnabled(True)

        self.horizontalLayout_85.addWidget(self.adminSettingsLname, 0, Qt.AlignRight)


        self.verticalLayout_66.addWidget(self.widget_81)

        self.widget_83 = QWidget(self.adminPasswordWidget)
        self.widget_83.setObjectName(u"widget_83")
        self.horizontalLayout_88 = QHBoxLayout(self.widget_83)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.label_52 = QLabel(self.widget_83)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font1)

        self.horizontalLayout_88.addWidget(self.label_52, 0, Qt.AlignLeft)

        self.adminSettingsEmail = QLineEdit(self.widget_83)
        self.adminSettingsEmail.setObjectName(u"adminSettingsEmail")
        self.adminSettingsEmail.setEnabled(True)

        self.horizontalLayout_88.addWidget(self.adminSettingsEmail, 0, Qt.AlignRight)


        self.verticalLayout_66.addWidget(self.widget_83)

        self.widget_76 = QWidget(self.adminPasswordWidget)
        self.widget_76.setObjectName(u"widget_76")
        self.horizontalLayout_81 = QHBoxLayout(self.widget_76)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.adminProfileSettingBtn = QPushButton(self.widget_76)
        self.adminProfileSettingBtn.setObjectName(u"adminProfileSettingBtn")
        self.adminProfileSettingBtn.setFont(font1)
        self.adminProfileSettingBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_81.addWidget(self.adminProfileSettingBtn)


        self.verticalLayout_66.addWidget(self.widget_76)

        self.widget_77 = QWidget(self.adminPasswordWidget)
        self.widget_77.setObjectName(u"widget_77")
        self.widget_77.setStyleSheet(u"#widget_77{\n"
"border-top:1px solid #979797;\n"
"}")
        self.verticalLayout_69 = QVBoxLayout(self.widget_77)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.verticalLayout_69.setContentsMargins(-1, 19, -1, 19)
        self.label_48 = QLabel(self.widget_77)
        self.label_48.setObjectName(u"label_48")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_48.setFont(font3)
        self.label_48.setAlignment(Qt.AlignCenter)

        self.verticalLayout_69.addWidget(self.label_48)

        self.widget_74 = QWidget(self.widget_77)
        self.widget_74.setObjectName(u"widget_74")
        self.horizontalLayout_79 = QHBoxLayout(self.widget_74)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_45 = QLabel(self.widget_74)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font1)

        self.horizontalLayout_79.addWidget(self.label_45, 0, Qt.AlignLeft)

        self.adminSettingsNewPass = QLineEdit(self.widget_74)
        self.adminSettingsNewPass.setObjectName(u"adminSettingsNewPass")
        self.adminSettingsNewPass.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.adminSettingsNewPass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_79.addWidget(self.adminSettingsNewPass, 0, Qt.AlignRight)


        self.verticalLayout_69.addWidget(self.widget_74)

        self.widget_75 = QWidget(self.widget_77)
        self.widget_75.setObjectName(u"widget_75")
        self.horizontalLayout_80 = QHBoxLayout(self.widget_75)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.label_46 = QLabel(self.widget_75)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font1)

        self.horizontalLayout_80.addWidget(self.label_46, 0, Qt.AlignLeft)

        self.adminSettingsReenterNewPass = QLineEdit(self.widget_75)
        self.adminSettingsReenterNewPass.setObjectName(u"adminSettingsReenterNewPass")
        self.adminSettingsReenterNewPass.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.adminSettingsReenterNewPass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_80.addWidget(self.adminSettingsReenterNewPass, 0, Qt.AlignRight)


        self.verticalLayout_69.addWidget(self.widget_75)

        self.adminChangePasswordBtn = QPushButton(self.widget_77)
        self.adminChangePasswordBtn.setObjectName(u"adminChangePasswordBtn")
        self.adminChangePasswordBtn.setFont(font1)
        self.adminChangePasswordBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_69.addWidget(self.adminChangePasswordBtn)


        self.verticalLayout_66.addWidget(self.widget_77)


        self.verticalLayout_8.addWidget(self.adminPasswordWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 329, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.widget_78 = QWidget(self.settingsPage)
        self.widget_78.setObjectName(u"widget_78")

        self.verticalLayout_8.addWidget(self.widget_78)

        self.centerMenuPages.addWidget(self.settingsPage)
        self.informationPage = QWidget()
        self.informationPage.setObjectName(u"informationPage")
        self.verticalLayout_7 = QVBoxLayout(self.informationPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_3 = QLabel(self.informationPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_3)

        self.scrollArea = QScrollArea(self.informationPage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 83, 69))
        self.scrollAreaWidgetContents_2.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_76 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents_2)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_76.addWidget(self.textBrowser, 0, Qt.AlignLeft)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_7.addWidget(self.scrollArea)

        self.centerMenuPages.addWidget(self.informationPage)
        self.helpMenuPage = QWidget()
        self.helpMenuPage.setObjectName(u"helpMenuPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpMenuPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.helpMenuPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.label_71 = QLabel(self.helpMenuPage)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_71)

        self.widget_110 = QWidget(self.helpMenuPage)
        self.widget_110.setObjectName(u"widget_110")
        self.horizontalLayout_104 = QHBoxLayout(self.widget_110)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(-1, 9, -1, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 844, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.horizontalLayout_104.addItem(self.verticalSpacer_3)


        self.verticalLayout_9.addWidget(self.widget_110)

        self.centerMenuPages.addWidget(self.helpMenuPage)

        self.verticalLayout_6.addWidget(self.centerMenuPages)


        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setMinimumSize(QSize(0, 0))
        self.mainBodyContainer.setToolTipDuration(-1)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setMaximumSize(QSize(170, 40))
        self.label_5.setPixmap(QPixmap(u":/Images/Images/title.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_5)


        self.horizontalLayout_5.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.notificationBtn = QPushButton(self.frame_6)
        self.notificationBtn.setObjectName(u"notificationBtn")
        self.notificationBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/Icons/Icons/bell.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.notificationBtn.setIcon(icon10)
        self.notificationBtn.setIconSize(QSize(24, 34))

        self.horizontalLayout_7.addWidget(self.notificationBtn)

        self.moreMenuBtn = QPushButton(self.frame_6)
        self.moreMenuBtn.setObjectName(u"moreMenuBtn")
        self.moreMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/Icons/Icons/more-horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.moreMenuBtn.setIcon(icon11)
        self.moreMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.moreMenuBtn)

        self.profileMenuBtn = QPushButton(self.frame_6)
        self.profileMenuBtn.setObjectName(u"profileMenuBtn")
        self.profileMenuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Normal, QIcon.On)
        icon12.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Active, QIcon.Off)
        icon12.addFile(u":/Icons/Icons/user-red.svg", QSize(), QIcon.Active, QIcon.On)
        icon12.addFile(u":/Icons/Icons/user.svg", QSize(), QIcon.Selected, QIcon.Off)
        icon12.addFile(u":/Icons/Icons/user-red.svg", QSize(), QIcon.Selected, QIcon.On)
        self.profileMenuBtn.setIcon(icon12)
        self.profileMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_7.addWidget(self.profileMenuBtn)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.minimizeWindowsBtn = QPushButton(self.frame_7)
        self.minimizeWindowsBtn.setObjectName(u"minimizeWindowsBtn")
        icon13 = QIcon()
        icon13.addFile(u":/Icons/Icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeWindowsBtn.setIcon(icon13)

        self.horizontalLayout_4.addWidget(self.minimizeWindowsBtn)

        self.restoreWindowsBtn = QPushButton(self.frame_7)
        self.restoreWindowsBtn.setObjectName(u"restoreWindowsBtn")
        icon14 = QIcon()
        icon14.addFile(u":/Icons/Icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreWindowsBtn.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.restoreWindowsBtn)

        self.closeWindowsBtn = QPushButton(self.frame_7)
        self.closeWindowsBtn.setObjectName(u"closeWindowsBtn")
        icon15 = QIcon()
        icon15.addFile(u":/Icons/Icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeWindowsBtn.setIcon(icon15)

        self.horizontalLayout_4.addWidget(self.closeWindowsBtn)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy2)
        self.mainBodyContent.setMinimumSize(QSize(1207, 795))
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.mainContentsContainer = QWidget(self.mainBodyContent)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.mainPages = QCustomStackedWidget(self.mainContentsContainer)
        self.mainPages.setObjectName(u"mainPages")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.homePage.setStyleSheet(u"\n"
"\n"
"#equipmentWidget,#inuseInvWidget,#sentforrepairWidget,#serverRoomWidget{\n"
"  background: #003854;\n"
"border-radius:10px;\n"
"  padding: 10px;\n"
"color:#FFBD59;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.verticalLayout_19 = QVBoxLayout(self.homePage)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.homeDashboardWidget = QWidget(self.homePage)
        self.homeDashboardWidget.setObjectName(u"homeDashboardWidget")
        self.homeDashboardWidget.setStyleSheet(u"#sendRepairtoServerGroupBox QGroupBox{\n"
"color:#4e5f8b;\n"
"border:1px dashed #4e5f8b;\n"
"}\n"
" #sendRepairtoUserGroupBox QGroupBox{\n"
"color:#4e5f8b;\n"
"border:1px dotted #4e5f8b;\n"
"}")
        self.verticalLayout_67 = QVBoxLayout(self.homeDashboardWidget)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_8 = QLabel(self.homeDashboardWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color:#003854;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_67.addWidget(self.label_8)

        self.widget_71 = QWidget(self.homeDashboardWidget)
        self.widget_71.setObjectName(u"widget_71")
        self.horizontalLayout_84 = QHBoxLayout(self.widget_71)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.homeDashboardTopWidget = QWidget(self.widget_71)
        self.homeDashboardTopWidget.setObjectName(u"homeDashboardTopWidget")
        sizePolicy.setHeightForWidth(self.homeDashboardTopWidget.sizePolicy().hasHeightForWidth())
        self.homeDashboardTopWidget.setSizePolicy(sizePolicy)
        self.homeDashboardTopWidget.setMinimumSize(QSize(0, 300))
        self.horizontalLayout_92 = QHBoxLayout(self.homeDashboardTopWidget)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.homeDashboardCountWidget = QWidget(self.homeDashboardTopWidget)
        self.homeDashboardCountWidget.setObjectName(u"homeDashboardCountWidget")
        self.verticalLayout_87 = QVBoxLayout(self.homeDashboardCountWidget)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.serverRoomWidget = QWidget(self.homeDashboardCountWidget)
        self.serverRoomWidget.setObjectName(u"serverRoomWidget")
        self.verticalLayout_68 = QVBoxLayout(self.serverRoomWidget)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_59 = QLabel(self.serverRoomWidget)
        self.label_59.setObjectName(u"label_59")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_59.setFont(font4)
        self.label_59.setStyleSheet(u"")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.label_59)

        self.horizontalSpacer_8 = QSpacerItem(172, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_68.addItem(self.horizontalSpacer_8)

        self.serverRoomDashCount = QLabel(self.serverRoomWidget)
        self.serverRoomDashCount.setObjectName(u"serverRoomDashCount")
        font5 = QFont()
        font5.setPointSize(30)
        font5.setBold(True)
        font5.setWeight(75)
        self.serverRoomDashCount.setFont(font5)
        self.serverRoomDashCount.setStyleSheet(u"\n"
"color:#fbf2b3;\n"
"")
        self.serverRoomDashCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_68.addWidget(self.serverRoomDashCount)


        self.verticalLayout_87.addWidget(self.serverRoomWidget)


        self.horizontalLayout_92.addWidget(self.homeDashboardCountWidget)

        self.widget_117 = QWidget(self.homeDashboardTopWidget)
        self.widget_117.setObjectName(u"widget_117")
        self.verticalLayout_82 = QVBoxLayout(self.widget_117)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.inuseInvWidget = QWidget(self.widget_117)
        self.inuseInvWidget.setObjectName(u"inuseInvWidget")
        self.verticalLayout_81 = QVBoxLayout(self.inuseInvWidget)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.label_65 = QLabel(self.inuseInvWidget)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font4)
        self.label_65.setStyleSheet(u"")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.label_65)

        self.horizontalSpacer_11 = QSpacerItem(132, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_81.addItem(self.horizontalSpacer_11)

        self.inuseRoomDashCount = QLabel(self.inuseInvWidget)
        self.inuseRoomDashCount.setObjectName(u"inuseRoomDashCount")
        self.inuseRoomDashCount.setFont(font5)
        self.inuseRoomDashCount.setStyleSheet(u"\n"
"color:#fbf2b3;\n"
"")
        self.inuseRoomDashCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_81.addWidget(self.inuseRoomDashCount)


        self.verticalLayout_82.addWidget(self.inuseInvWidget)


        self.horizontalLayout_92.addWidget(self.widget_117)

        self.widget_115 = QWidget(self.homeDashboardTopWidget)
        self.widget_115.setObjectName(u"widget_115")
        self.verticalLayout_89 = QVBoxLayout(self.widget_115)
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.equipmentWidget = QWidget(self.widget_115)
        self.equipmentWidget.setObjectName(u"equipmentWidget")
        self.verticalLayout_88 = QVBoxLayout(self.equipmentWidget)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.label_64 = QLabel(self.equipmentWidget)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font4)
        self.label_64.setStyleSheet(u"")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.label_64)

        self.horizontalSpacer_13 = QSpacerItem(83, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_88.addItem(self.horizontalSpacer_13)

        self.equipRoomCount = QLabel(self.equipmentWidget)
        self.equipRoomCount.setObjectName(u"equipRoomCount")
        self.equipRoomCount.setFont(font5)
        self.equipRoomCount.setStyleSheet(u"\n"
"color:#fbf2b3;\n"
"")
        self.equipRoomCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_88.addWidget(self.equipRoomCount)


        self.verticalLayout_89.addWidget(self.equipmentWidget)


        self.horizontalLayout_92.addWidget(self.widget_115)

        self.widget_80 = QWidget(self.homeDashboardTopWidget)
        self.widget_80.setObjectName(u"widget_80")
        self.verticalLayout_84 = QVBoxLayout(self.widget_80)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.sentforrepairWidget = QWidget(self.widget_80)
        self.sentforrepairWidget.setObjectName(u"sentforrepairWidget")
        self.verticalLayout_76 = QVBoxLayout(self.sentforrepairWidget)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_61 = QLabel(self.sentforrepairWidget)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font4)
        self.label_61.setStyleSheet(u"")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.label_61)

        self.horizontalSpacer_9 = QSpacerItem(119, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_76.addItem(self.horizontalSpacer_9)

        self.repairsRoomDashCount = QLabel(self.sentforrepairWidget)
        self.repairsRoomDashCount.setObjectName(u"repairsRoomDashCount")
        self.repairsRoomDashCount.setFont(font5)
        self.repairsRoomDashCount.setStyleSheet(u"\n"
"color:#fbf2b3;\n"
"")
        self.repairsRoomDashCount.setAlignment(Qt.AlignCenter)

        self.verticalLayout_76.addWidget(self.repairsRoomDashCount)


        self.verticalLayout_84.addWidget(self.sentforrepairWidget)


        self.horizontalLayout_92.addWidget(self.widget_80)


        self.horizontalLayout_84.addWidget(self.homeDashboardTopWidget)


        self.verticalLayout_67.addWidget(self.widget_71)

        self.widget_112 = QWidget(self.homeDashboardWidget)
        self.widget_112.setObjectName(u"widget_112")
        self.verticalLayout_83 = QVBoxLayout(self.widget_112)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_72 = QLabel(self.widget_112)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setPixmap(QPixmap(u":/Images/Images/Yamaha-WaterMark.png"))
        self.label_72.setScaledContents(True)
        self.label_72.setAlignment(Qt.AlignCenter)

        self.verticalLayout_83.addWidget(self.label_72, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_67.addWidget(self.widget_112)


        self.verticalLayout_19.addWidget(self.homeDashboardWidget)

        self.mainPages.addWidget(self.homePage)
        self.serverInvPage = QWidget()
        self.serverInvPage.setObjectName(u"serverInvPage")
        self.serverInvPage.setStyleSheet(u"\n"
"#serverRoomTabWidget::pane {\n"
"border: none;\n"
"background-color:#bbc0cd;\n"
"\n"
"} \n"
"\n"
"#serverRoomTabWidget QTabBar::tab {\n"
"	color:#fff;\n"
"  background: #003854;\n"
"	border-top-left-radius:10px;\n"
"border-top-right-radius:10px;\n"
"  padding: 10px;\n"
"} \n"
"\n"
"#serverRoomTabWidget QTabBar::tab:selected { \n"
"color:#003854;\n"
"  background:#ffbd59; \n"
"  margin-bottom: -1px; \n"
"}\n"
"#laptopTabPane QLineEdit,#laptopTabPane QComboBox{\n"
"color:#000;\n"
"background-color:#dcdcdd;\n"
"border:1px solid rgba(166,164,164,1);\n"
"border-radius:5px;\n"
"padding:5px 10px;\n"
"}\n"
"#laptopTabPane QLineEdit:hover,#laptopTabPane QComboBox:hover{\n"
"\n"
"border:1px solid red;\n"
"\n"
"}\n"
"#laptopTabPane QLineEdit:focus,#laptopTabPane QComboBox:focus{\n"
"\n"
"border:1px solid red;\n"
"\n"
"}\n"
"\n"
"#laptopRecordsButtons QPushButton,#FaultyLaptopRecordsButtons QPushButton{\n"
"padding:10px;\n"
"}\n"
" #addLaptopBtn:hover, #addFaultyLaptopBtn:hover{\n"
"background-color:#0eab1b;\n"
"}\n"
""
                        "#addLaptopBtn,#addFaultyLaptopBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#0c8724;\n"
"}\n"
"#updateLaptopBtn,#updateFaultyLaptopBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#d49348;\n"
"}\n"
"#updateLaptopBtn:hover,#updateFaultyLaptopBtn:hover{\n"
"background-color:#ad610a;\n"
"}\n"
"#deleteLaptopBtn,#deleteFaultyLaptopBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#d42626;\n"
"}\n"
"#deleteLaptopBtn:hover,#deleteFaultyLaptopBtn:hover{\n"
"background-color:#bd0d0d;\n"
"}\n"
"#serverRoomTabWidget QTableWidget{\n"
"color:#003854;\n"
"background-color:#eaeaeb;\n"
"border:1px solid #4e5f8b;\n"
"border-radius:3px;\n"
"}\n"
"#serverRoomTabWidget QHeaderView::section{\n"
"background: #003854;\n"
"border:1px solid #404d6f;\n"
"color:#fff;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"#serverRoomGroupBox{\n"
"color:#003854;\n"
"border:1px dashed #003854;\n"
"}\n"
"#serverRoomGroupBox QLabel{\n"
"color:#003854;\n"
"\n"
"}\n"
"\n"
"\n"
"#sendToRepair"
                        "Widget QPushButton{\n"
"padding:10px;\n"
"}\n"
"#sendToRepairBtn{\n"
"color:#003854;\n"
"border:1px solid #003854;\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"}\n"
" #sendToRepairBtn:hover{\n"
"background-color:#003854;\n"
"color:#fff;\n"
"\n"
"}\n"
"\n"
"#laptopRecordGenerateExcelBtn{\n"
"border:1px solid  #003854;\n"
"border-radius:2px;\n"
"padding:5px;\n"
"color:#003854;\n"
"}\n"
"#laptopRecordGenerateExcelBtn:hover{\n"
"background-color:#003854;\n"
"color:#fff;\n"
"}\n"
"")
        self.verticalLayout_18 = QVBoxLayout(self.serverInvPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.serverInvLabel = QLabel(self.serverInvPage)
        self.serverInvLabel.setObjectName(u"serverInvLabel")
        self.serverInvLabel.setFont(font2)
        self.serverInvLabel.setStyleSheet(u"color:#003854;")
        self.serverInvLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.serverInvLabel)

        self.serverRoomTabWidget = QTabWidget(self.serverInvPage)
        self.serverRoomTabWidget.setObjectName(u"serverRoomTabWidget")
        self.laptopTabPane = QWidget()
        self.laptopTabPane.setObjectName(u"laptopTabPane")
        self.verticalLayout_22 = QVBoxLayout(self.laptopTabPane)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget = QWidget(self.laptopTabPane)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_14 = QHBoxLayout(self.widget)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 30, 0, 0)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_25 = QVBoxLayout(self.widget_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_63 = QWidget(self.widget_3)
        self.widget_63.setObjectName(u"widget_63")
        self.horizontalLayout_44 = QHBoxLayout(self.widget_63)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.txtLaptopSerial = QLineEdit(self.widget_63)
        self.txtLaptopSerial.setObjectName(u"txtLaptopSerial")
        self.txtLaptopSerial.setInputMethodHints(Qt.ImhUppercaseOnly)

        self.horizontalLayout_44.addWidget(self.txtLaptopSerial)

        self.label_29 = QLabel(self.widget_63)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color:red;")

        self.horizontalLayout_44.addWidget(self.label_29)


        self.verticalLayout_25.addWidget(self.widget_63)

        self.widget_64 = QWidget(self.widget_3)
        self.widget_64.setObjectName(u"widget_64")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_64)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.txtModelNumber = QLineEdit(self.widget_64)
        self.txtModelNumber.setObjectName(u"txtModelNumber")

        self.horizontalLayout_61.addWidget(self.txtModelNumber)

        self.label_37 = QLabel(self.widget_64)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"color:red;")

        self.horizontalLayout_61.addWidget(self.label_37)


        self.verticalLayout_25.addWidget(self.widget_64)

        self.widget_65 = QWidget(self.widget_3)
        self.widget_65.setObjectName(u"widget_65")
        self.horizontalLayout_62 = QHBoxLayout(self.widget_65)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.txtLastUser = QLineEdit(self.widget_65)
        self.txtLastUser.setObjectName(u"txtLastUser")

        self.horizontalLayout_62.addWidget(self.txtLastUser)


        self.verticalLayout_25.addWidget(self.widget_65)

        self.widget_66 = QWidget(self.widget_3)
        self.widget_66.setObjectName(u"widget_66")
        self.horizontalLayout_63 = QHBoxLayout(self.widget_66)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.txtComboStatus = QComboBox(self.widget_66)
        self.txtComboStatus.addItem("")
        self.txtComboStatus.addItem("")
        self.txtComboStatus.addItem("")
        self.txtComboStatus.addItem("")
        self.txtComboStatus.addItem("")
        self.txtComboStatus.addItem("")
        self.txtComboStatus.addItem("")
        self.txtComboStatus.setObjectName(u"txtComboStatus")
        self.txtComboStatus.setStyleSheet(u"color:black;")

        self.horizontalLayout_63.addWidget(self.txtComboStatus)

        self.label_40 = QLabel(self.widget_66)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color:red;")

        self.horizontalLayout_63.addWidget(self.label_40)


        self.verticalLayout_25.addWidget(self.widget_66)

        self.laptopRecordsButtons = QWidget(self.widget_3)
        self.laptopRecordsButtons.setObjectName(u"laptopRecordsButtons")
        self.horizontalLayout_15 = QHBoxLayout(self.laptopRecordsButtons)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.addLaptopBtn = QPushButton(self.laptopRecordsButtons)
        self.addLaptopBtn.setObjectName(u"addLaptopBtn")
        self.addLaptopBtn.setFont(font3)
        self.addLaptopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/Icons/Icons/plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addLaptopBtn.setIcon(icon16)

        self.horizontalLayout_15.addWidget(self.addLaptopBtn)

        self.updateLaptopBtn = QPushButton(self.laptopRecordsButtons)
        self.updateLaptopBtn.setObjectName(u"updateLaptopBtn")
        self.updateLaptopBtn.setFont(font3)
        self.updateLaptopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/Icons/Icons/rotate-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updateLaptopBtn.setIcon(icon17)

        self.horizontalLayout_15.addWidget(self.updateLaptopBtn)

        self.deleteLaptopBtn = QPushButton(self.laptopRecordsButtons)
        self.deleteLaptopBtn.setObjectName(u"deleteLaptopBtn")
        self.deleteLaptopBtn.setFont(font3)
        self.deleteLaptopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon18 = QIcon()
        icon18.addFile(u":/Icons/Icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteLaptopBtn.setIcon(icon18)

        self.horizontalLayout_15.addWidget(self.deleteLaptopBtn)


        self.verticalLayout_25.addWidget(self.laptopRecordsButtons)


        self.horizontalLayout_14.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_2 = QSpacerItem(278, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_14.addWidget(self.widget_4)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_24 = QVBoxLayout(self.widget_5)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.serverRoomGroupBox = QGroupBox(self.widget_5)
        self.serverRoomGroupBox.setObjectName(u"serverRoomGroupBox")
        self.serverRoomGroupBox.setFont(font1)
        self.serverRoomGroupBox.setStyleSheet(u"")
        self.verticalLayout_60 = QVBoxLayout(self.serverRoomGroupBox)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.widget_94 = QWidget(self.serverRoomGroupBox)
        self.widget_94.setObjectName(u"widget_94")
        self.horizontalLayout_72 = QHBoxLayout(self.widget_94)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_54 = QLabel(self.widget_94)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font1)

        self.horizontalLayout_72.addWidget(self.label_54, 0, Qt.AlignLeft)

        self.sendforrepairSerial = QLineEdit(self.widget_94)
        self.sendforrepairSerial.setObjectName(u"sendforrepairSerial")

        self.horizontalLayout_72.addWidget(self.sendforrepairSerial, 0, Qt.AlignRight)


        self.verticalLayout_60.addWidget(self.widget_94)

        self.widget_95 = QWidget(self.serverRoomGroupBox)
        self.widget_95.setObjectName(u"widget_95")
        self.horizontalLayout_90 = QHBoxLayout(self.widget_95)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_58 = QLabel(self.widget_95)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font1)

        self.horizontalLayout_90.addWidget(self.label_58, 0, Qt.AlignLeft)

        self.sendforrepairStatus = QComboBox(self.widget_95)
        self.sendforrepairStatus.addItem("")
        self.sendforrepairStatus.addItem("")
        self.sendforrepairStatus.addItem("")
        self.sendforrepairStatus.addItem("")
        self.sendforrepairStatus.addItem("")
        self.sendforrepairStatus.addItem("")
        self.sendforrepairStatus.setObjectName(u"sendforrepairStatus")
        self.sendforrepairStatus.setStyleSheet(u"color:#404d6f;")

        self.horizontalLayout_90.addWidget(self.sendforrepairStatus, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_60.addWidget(self.widget_95)

        self.sendToRepairWidget = QWidget(self.serverRoomGroupBox)
        self.sendToRepairWidget.setObjectName(u"sendToRepairWidget")
        self.verticalLayout_64 = QVBoxLayout(self.sendToRepairWidget)
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.sendToRepairBtn = QPushButton(self.sendToRepairWidget)
        self.sendToRepairBtn.setObjectName(u"sendToRepairBtn")
        self.sendToRepairBtn.setFont(font1)
        self.sendToRepairBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_64.addWidget(self.sendToRepairBtn)


        self.verticalLayout_60.addWidget(self.sendToRepairWidget)


        self.verticalLayout_24.addWidget(self.serverRoomGroupBox)


        self.horizontalLayout_14.addWidget(self.widget_5)


        self.verticalLayout_22.addWidget(self.widget, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.laptopTabPane)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_23 = QVBoxLayout(self.widget_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_6 = QWidget(self.widget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setEnabled(False)
        self.txtLaptopID = QLineEdit(self.widget_7)
        self.txtLaptopID.setObjectName(u"txtLaptopID")
        self.txtLaptopID.setGeometry(QRect(40, 10, 41, 28))
        self.txtLaptopID.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"color:transparent;")
        self.txtLaptopID.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.txtLaptopID.setEchoMode(QLineEdit.NoEcho)

        self.horizontalLayout_17.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_43 = QVBoxLayout(self.widget_8)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(-1, 0, -1, 0)
        self.laptopRecordGenerateExcelBtn = QPushButton(self.widget_8)
        self.laptopRecordGenerateExcelBtn.setObjectName(u"laptopRecordGenerateExcelBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.laptopRecordGenerateExcelBtn.sizePolicy().hasHeightForWidth())
        self.laptopRecordGenerateExcelBtn.setSizePolicy(sizePolicy3)
        self.laptopRecordGenerateExcelBtn.setFont(font1)
        self.laptopRecordGenerateExcelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon19 = QIcon()
        icon19.addFile(u":/Icons/Icons/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.laptopRecordGenerateExcelBtn.setIcon(icon19)

        self.verticalLayout_43.addWidget(self.laptopRecordGenerateExcelBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_17.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_19 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.horizontalLayout_17.addWidget(self.widget_9, 0, Qt.AlignVCenter)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_18 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 9)
        self.txtLapInvSearch = QLineEdit(self.widget_10)
        self.txtLapInvSearch.setObjectName(u"txtLapInvSearch")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.txtLapInvSearch.sizePolicy().hasHeightForWidth())
        self.txtLapInvSearch.setSizePolicy(sizePolicy4)
        self.txtLapInvSearch.setMinimumSize(QSize(170, 0))
        self.txtLapInvSearch.setMaximumSize(QSize(170, 16777215))
        font6 = QFont()
        font6.setPointSize(10)
        self.txtLapInvSearch.setFont(font6)
        self.txtLapInvSearch.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.txtLapInvSearch, 0, Qt.AlignLeft)

        self.txtLapInvSearchCombo = QComboBox(self.widget_10)
        self.txtLapInvSearchCombo.addItem("")
        self.txtLapInvSearchCombo.addItem("")
        self.txtLapInvSearchCombo.addItem("")
        self.txtLapInvSearchCombo.setObjectName(u"txtLapInvSearchCombo")
        sizePolicy4.setHeightForWidth(self.txtLapInvSearchCombo.sizePolicy().hasHeightForWidth())
        self.txtLapInvSearchCombo.setSizePolicy(sizePolicy4)
        self.txtLapInvSearchCombo.setMinimumSize(QSize(170, 0))
        self.txtLapInvSearchCombo.setMaximumSize(QSize(170, 16777215))
        self.txtLapInvSearchCombo.setFont(font6)
        self.txtLapInvSearchCombo.setStyleSheet(u"color:rgb(0, 0, 0)")
        self.txtLapInvSearchCombo.setEditable(False)

        self.horizontalLayout_18.addWidget(self.txtLapInvSearchCombo)


        self.horizontalLayout_17.addWidget(self.widget_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_23.addWidget(self.widget_6)

        self.laptopRecordsTable = QTableWidget(self.widget_2)
        if (self.laptopRecordsTable.columnCount() < 7):
            self.laptopRecordsTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.laptopRecordsTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.laptopRecordsTable.setObjectName(u"laptopRecordsTable")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.laptopRecordsTable.sizePolicy().hasHeightForWidth())
        self.laptopRecordsTable.setSizePolicy(sizePolicy5)
        self.laptopRecordsTable.setMinimumSize(QSize(861, 334))
        self.laptopRecordsTable.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.laptopRecordsTable.setShowGrid(True)
        self.laptopRecordsTable.setSortingEnabled(False)
        self.laptopRecordsTable.horizontalHeader().setCascadingSectionResizes(False)
        self.laptopRecordsTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.laptopRecordsTable.horizontalHeader().setStretchLastSection(True)
        self.laptopRecordsTable.verticalHeader().setCascadingSectionResizes(False)
        self.laptopRecordsTable.verticalHeader().setMinimumSectionSize(24)
        self.laptopRecordsTable.verticalHeader().setProperty("showSortIndicator", False)
        self.laptopRecordsTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_23.addWidget(self.laptopRecordsTable)


        self.verticalLayout_22.addWidget(self.widget_2)

        self.serverRoomTabWidget.addTab(self.laptopTabPane, "")
        self.equipmentTabPane = QWidget()
        self.equipmentTabPane.setObjectName(u"equipmentTabPane")
        self.equipmentTabPane.setStyleSheet(u"#equipSpinWidget QLabel{\n"
"color:#003854;\n"
"}\n"
"#equipSpinWidget QSpinBox{\n"
"background-color:#003854;\n"
"border-color:#003854;\n"
"border-radius:5px;\n"
"font-weight:bold;\n"
"padding:5px;\n"
"}\n"
"#equipSpinWidget QSpinBox:hover{\n"
"border:1px solid red;\n"
"}\n"
"#updateEquipBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#d49348;\n"
"}\n"
"#updateEquipBtn:hover{\n"
"background-color:#ad610a;\n"
"}\n"
"#equipSpinSection{\n"
"border:1px dashed #003854;\n"
"border-radius:5px;\n"
"}\n"
"/** EXTRA EQUIP **/\n"
"\n"
"QGroupBox{\n"
"color:#003854;\n"
"border:1px dotted #003854;\n"
"}\n"
"#extraGroupBox QLabel{\n"
"color:#003854;\n"
"}\n"
"#extraGroupBox QSpinBox{\n"
"background-color:#003854;\n"
"border-color:#003854;\n"
"border-radius:5px;\n"
"font-weight:bold;\n"
"padding:5px;\n"
"}\n"
"#extraGroupBox QSpinBox:hover{\n"
"border:1px solid red;\n"
"}\n"
"\n"
"#extraGroupBox QComboBox{\n"
"color:#000000;\n"
"background-color:#dcdcdd;\n"
"border:1px solid rgba(166,164,164,1);\n"
""
                        "border-radius:5px;\n"
"padding:5px 10px;\n"
"}\n"
"#extraGroupBox QComboBox:hover{\n"
"border:1px solid red;\n"
"}\n"
"#extraEquipWidget QPushButton{\n"
"padding:5px;\n"
"}\n"
" #addExtraEquipBtn:hover{\n"
"background-color:#0eab1b;\n"
"}\n"
"#addExtraEquipBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#0c8724;\n"
"}\n"
"#updateExtraEquipBtn{\n"
"border-radius:5px;\n"
"padding: 5px;\n"
"background-color:#d49348;\n"
"}\n"
"#updateExtraEquipBtn:hover{\n"
"background-color:#ad610a;\n"
"}\n"
"#deleteExtraEquipBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#d42626;\n"
"}\n"
"#deleteExtraEquipBtn:hover{\n"
"background-color:#bd0d0d;\n"
"}\n"
"\n"
"\n"
"\n"
"#equipRecordGenerateExcelBtn{\n"
"border:1px solid #003854;\n"
"border-radius:2px;\n"
"padding:5px;\n"
"color:#003854;\n"
"}\n"
"#equipRecordGenerateExcelBtn:hover{\n"
"background-color:#003854;\n"
"color:#fff;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.equipmentTabPane)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_18 = QWidget(self.equipmentTabPane)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.equipSpinSection = QWidget(self.widget_18)
        self.equipSpinSection.setObjectName(u"equipSpinSection")
        self.verticalLayout_27 = QVBoxLayout(self.equipSpinSection)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.equipSpinWidget = QWidget(self.equipSpinSection)
        self.equipSpinWidget.setObjectName(u"equipSpinWidget")
        self.horizontalLayout_36 = QHBoxLayout(self.equipSpinWidget)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.widget_38 = QWidget(self.equipSpinWidget)
        self.widget_38.setObjectName(u"widget_38")
        self.verticalLayout_30 = QVBoxLayout(self.widget_38)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.widget_39 = QWidget(self.widget_38)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setFont(font1)
        self.horizontalLayout_37 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_9 = QLabel(self.widget_39)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_37.addWidget(self.label_9)

        self.txtEquipKeyboardSpin = QSpinBox(self.widget_39)
        self.txtEquipKeyboardSpin.setObjectName(u"txtEquipKeyboardSpin")

        self.horizontalLayout_37.addWidget(self.txtEquipKeyboardSpin, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.widget_39)

        self.widget_40 = QWidget(self.widget_38)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_14 = QLabel(self.widget_40)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_38.addWidget(self.label_14, 0, Qt.AlignLeft)

        self.txtEquipMouseSpin = QSpinBox(self.widget_40)
        self.txtEquipMouseSpin.setObjectName(u"txtEquipMouseSpin")

        self.horizontalLayout_38.addWidget(self.txtEquipMouseSpin, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.widget_40)

        self.widget_41 = QWidget(self.widget_38)
        self.widget_41.setObjectName(u"widget_41")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_17 = QLabel(self.widget_41)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.horizontalLayout_39.addWidget(self.label_17, 0, Qt.AlignLeft)

        self.txtEquipHeadphoneSpin = QSpinBox(self.widget_41)
        self.txtEquipHeadphoneSpin.setObjectName(u"txtEquipHeadphoneSpin")

        self.horizontalLayout_39.addWidget(self.txtEquipHeadphoneSpin, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.widget_41)


        self.horizontalLayout_36.addWidget(self.widget_38)

        self.widget_37 = QWidget(self.equipSpinWidget)
        self.widget_37.setObjectName(u"widget_37")
        self.verticalLayout_31 = QVBoxLayout(self.widget_37)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.widget_43 = QWidget(self.widget_37)
        self.widget_43.setObjectName(u"widget_43")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_43)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_19 = QLabel(self.widget_43)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.horizontalLayout_41.addWidget(self.label_19, 0, Qt.AlignLeft)

        self.txtEquipMonitorSpin = QSpinBox(self.widget_43)
        self.txtEquipMonitorSpin.setObjectName(u"txtEquipMonitorSpin")

        self.horizontalLayout_41.addWidget(self.txtEquipMonitorSpin, 0, Qt.AlignRight)


        self.verticalLayout_31.addWidget(self.widget_43)

        self.widget_42 = QWidget(self.widget_37)
        self.widget_42.setObjectName(u"widget_42")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_42)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_18 = QLabel(self.widget_42)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout_40.addWidget(self.label_18, 0, Qt.AlignLeft)

        self.txtEquipDockSpin = QSpinBox(self.widget_42)
        self.txtEquipDockSpin.setObjectName(u"txtEquipDockSpin")

        self.horizontalLayout_40.addWidget(self.txtEquipDockSpin, 0, Qt.AlignRight)


        self.verticalLayout_31.addWidget(self.widget_42)


        self.horizontalLayout_36.addWidget(self.widget_37)


        self.verticalLayout_27.addWidget(self.equipSpinWidget)

        self.updateEquip = QWidget(self.equipSpinSection)
        self.updateEquip.setObjectName(u"updateEquip")
        self.horizontalLayout_32 = QHBoxLayout(self.updateEquip)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.updateEquipBtn = QPushButton(self.updateEquip)
        self.updateEquipBtn.setObjectName(u"updateEquipBtn")
        self.updateEquipBtn.setFont(font3)
        self.updateEquipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateEquipBtn.setIcon(icon17)

        self.horizontalLayout_32.addWidget(self.updateEquipBtn)


        self.verticalLayout_27.addWidget(self.updateEquip)

        self.label_12 = QLabel(self.equipSpinSection)
        self.label_12.setObjectName(u"label_12")
        font7 = QFont()
        font7.setBold(False)
        font7.setItalic(True)
        font7.setWeight(50)
        self.label_12.setFont(font7)

        self.verticalLayout_27.addWidget(self.label_12)


        self.horizontalLayout_31.addWidget(self.equipSpinSection)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_3)

        self.widget_32 = QWidget(self.widget_18)
        self.widget_32.setObjectName(u"widget_32")
        font8 = QFont()
        font8.setBold(False)
        font8.setWeight(50)
        self.widget_32.setFont(font8)
        self.verticalLayout_42 = QVBoxLayout(self.widget_32)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.extraGroupBox = QGroupBox(self.widget_32)
        self.extraGroupBox.setObjectName(u"extraGroupBox")
        self.extraGroupBox.setFont(font1)
        self.verticalLayout_41 = QVBoxLayout(self.extraGroupBox)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.widget_46 = QWidget(self.extraGroupBox)
        self.widget_46.setObjectName(u"widget_46")
        self.widget_46.setFont(font1)
        self.horizontalLayout_45 = QHBoxLayout(self.widget_46)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_23 = QLabel(self.widget_46)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.horizontalLayout_45.addWidget(self.label_23, 0, Qt.AlignLeft)

        self.equipOtherItemCombo = QComboBox(self.widget_46)
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.addItem("")
        self.equipOtherItemCombo.setObjectName(u"equipOtherItemCombo")
        self.equipOtherItemCombo.setStyleSheet(u"color:#404d6f;")
        self.equipOtherItemCombo.setEditable(True)

        self.horizontalLayout_45.addWidget(self.equipOtherItemCombo, 0, Qt.AlignRight)


        self.verticalLayout_41.addWidget(self.widget_46)

        self.widget_47 = QWidget(self.extraGroupBox)
        self.widget_47.setObjectName(u"widget_47")
        self.widget_47.setFont(font1)
        self.horizontalLayout_46 = QHBoxLayout(self.widget_47)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_25 = QLabel(self.widget_47)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.horizontalLayout_46.addWidget(self.label_25, 0, Qt.AlignLeft)

        self.equipOtherItemSpinbox = QSpinBox(self.widget_47)
        self.equipOtherItemSpinbox.setObjectName(u"equipOtherItemSpinbox")

        self.horizontalLayout_46.addWidget(self.equipOtherItemSpinbox, 0, Qt.AlignRight)


        self.verticalLayout_41.addWidget(self.widget_47)

        self.extraEquipButtons = QWidget(self.extraGroupBox)
        self.extraEquipButtons.setObjectName(u"extraEquipButtons")
        self.horizontalLayout_47 = QHBoxLayout(self.extraEquipButtons)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.addExtraEquipBtn = QPushButton(self.extraEquipButtons)
        self.addExtraEquipBtn.setObjectName(u"addExtraEquipBtn")
        self.addExtraEquipBtn.setFont(font3)
        self.addExtraEquipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addExtraEquipBtn.setIcon(icon16)

        self.horizontalLayout_47.addWidget(self.addExtraEquipBtn)

        self.updateExtraEquipBtn = QPushButton(self.extraEquipButtons)
        self.updateExtraEquipBtn.setObjectName(u"updateExtraEquipBtn")
        self.updateExtraEquipBtn.setFont(font3)
        self.updateExtraEquipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateExtraEquipBtn.setIcon(icon17)

        self.horizontalLayout_47.addWidget(self.updateExtraEquipBtn)

        self.deleteExtraEquipBtn = QPushButton(self.extraEquipButtons)
        self.deleteExtraEquipBtn.setObjectName(u"deleteExtraEquipBtn")
        self.deleteExtraEquipBtn.setFont(font3)
        self.deleteExtraEquipBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.deleteExtraEquipBtn.setIcon(icon18)

        self.horizontalLayout_47.addWidget(self.deleteExtraEquipBtn)


        self.verticalLayout_41.addWidget(self.extraEquipButtons)


        self.verticalLayout_42.addWidget(self.extraGroupBox)


        self.horizontalLayout_31.addWidget(self.widget_32)

        self.widget_33 = QWidget(self.widget_18)
        self.widget_33.setObjectName(u"widget_33")
        self.verticalLayout_28 = QVBoxLayout(self.widget_33)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")

        self.horizontalLayout_31.addWidget(self.widget_33)

        self.widget_34 = QWidget(self.widget_18)
        self.widget_34.setObjectName(u"widget_34")
        self.verticalLayout_40 = QVBoxLayout(self.widget_34)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_40.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_31.addWidget(self.widget_34)


        self.verticalLayout_29.addWidget(self.widget_18)

        self.widget_11 = QWidget(self.equipmentTabPane)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_26 = QVBoxLayout(self.widget_11)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_12 = QWidget(self.widget_11)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_20 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        self.widget_13.setEnabled(False)
        self.txtLaptopID_2 = QLineEdit(self.widget_13)
        self.txtLaptopID_2.setObjectName(u"txtLaptopID_2")
        self.txtLaptopID_2.setGeometry(QRect(40, 10, 41, 28))
        self.txtLaptopID_2.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"color:transparent;")
        self.txtLaptopID_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.txtLaptopID_2.setEchoMode(QLineEdit.NoEcho)

        self.horizontalLayout_20.addWidget(self.widget_13)

        self.equipExcelWidget = QWidget(self.widget_12)
        self.equipExcelWidget.setObjectName(u"equipExcelWidget")
        self.verticalLayout_45 = QVBoxLayout(self.equipExcelWidget)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, 0, -1, 0)
        self.equipRecordGenerateExcelBtn = QPushButton(self.equipExcelWidget)
        self.equipRecordGenerateExcelBtn.setObjectName(u"equipRecordGenerateExcelBtn")
        self.equipRecordGenerateExcelBtn.setFont(font)
        self.equipRecordGenerateExcelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.equipRecordGenerateExcelBtn.setIcon(icon19)

        self.verticalLayout_45.addWidget(self.equipRecordGenerateExcelBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_20.addWidget(self.equipExcelWidget)

        self.widget_15 = QWidget(self.widget_12)
        self.widget_15.setObjectName(u"widget_15")
        self.widget_15.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")

        self.horizontalLayout_20.addWidget(self.widget_15, 0, Qt.AlignVCenter)

        self.widget_16 = QWidget(self.widget_12)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_22 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")

        self.horizontalLayout_20.addWidget(self.widget_16, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_26.addWidget(self.widget_12)

        self.equipRecordTable = QTableWidget(self.widget_11)
        if (self.equipRecordTable.columnCount() < 5):
            self.equipRecordTable.setColumnCount(5)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.equipRecordTable.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.equipRecordTable.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.equipRecordTable.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.equipRecordTable.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.equipRecordTable.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        self.equipRecordTable.setObjectName(u"equipRecordTable")
        sizePolicy5.setHeightForWidth(self.equipRecordTable.sizePolicy().hasHeightForWidth())
        self.equipRecordTable.setSizePolicy(sizePolicy5)
        self.equipRecordTable.setMinimumSize(QSize(861, 334))
        self.equipRecordTable.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.equipRecordTable.setShowGrid(True)
        self.equipRecordTable.setSortingEnabled(False)
        self.equipRecordTable.horizontalHeader().setCascadingSectionResizes(False)
        self.equipRecordTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.equipRecordTable.horizontalHeader().setStretchLastSection(True)
        self.equipRecordTable.verticalHeader().setCascadingSectionResizes(False)
        self.equipRecordTable.verticalHeader().setMinimumSectionSize(24)
        self.equipRecordTable.verticalHeader().setProperty("showSortIndicator", False)
        self.equipRecordTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_26.addWidget(self.equipRecordTable)


        self.verticalLayout_29.addWidget(self.widget_11)

        self.serverRoomTabWidget.addTab(self.equipmentTabPane, "")

        self.verticalLayout_18.addWidget(self.serverRoomTabWidget)

        self.mainPages.addWidget(self.serverInvPage)
        self.inUseInvPage = QWidget()
        self.inUseInvPage.setObjectName(u"inUseInvPage")
        self.inUseInvPage.setStyleSheet(u"#inUseInvTabWidget{\n"
"border: none;\n"
"background-color:#bbc0cd;\n"
"}\n"
"#inUseInvTabWidget QLineEdit,#inUseInvTabWidget QComboBox{\n"
"color:#000000;\n"
"background-color:#dcdcdd;\n"
"border:1px solid rgba(166,164,164,1);\n"
"border-radius:5px;\n"
"padding:5px 10px;\n"
"}\n"
"\n"
"#inUseInvTabWidget QLineEdit:hover,#inUseInvTabWidget QComboBox:hover{\n"
"\n"
"border:1px solid red;\n"
"\n"
"}\n"
"\n"
"QTableWidget::verticalScrollBar {\n"
"    background-color: #bcc1ce;\n"
"}\n"
"\n"
"QTableWidget::horizontalScrollBar {\n"
"    background-color: #bcc1ce;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"    background-color:#bcc1ce;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #bcc1ce;\n"
"}\n"
"\n"
"#InuseInvCrudBtn QPushButton{\n"
"padding:10px;\n"
"}\n"
" #addInuseInvBtn:hover{\n"
"background-color:#0eab1b;\n"
"}\n"
"#addInuseInvBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#0c8724;\n"
"}\n"
"#updateInuseInvBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px"
                        ";\n"
"background-color:#d49348;\n"
"}\n"
"#updateInuseInvBtn:hover{\n"
"background-color:#ad610a;\n"
"}\n"
"#clearInuseInvBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#148cc2;\n"
"}\n"
"#clearInuseInvBtn:hover{\n"
"background-color:#1cabeb;\n"
"}\n"
"\n"
"\n"
"#InUseTableWidget QHeaderView::section{\n"
"background: #003854;\n"
"border:1px solid qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(54,90,108,1) stop:1 rgba(54,90,108,1));\n"
"color:#fff;\n"
"font-weight:bold;\n"
"}\n"
"#InUseTableWidget{\n"
"color:#003854;\n"
"background-color:#eaeaeb;\n"
"border:1px solid #4e5f8b;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"\n"
"/** LABLES AND DETIALS **/\n"
"\n"
"#inUseInvTabWidget QLabel,#inUseInvTabWidget QCheckBox,#inUseInvTabWidget QRadioButton{\n"
"color:#003854;\n"
"}\n"
"#inUseInvTabWidget QSpinBox{\n"
"background-color:#003854;\n"
"border-color:#003854;\n"
"border-radius:5px;\n"
"font-weight:bold;\n"
"padding:5px;\n"
"}\n"
"#inUseInvTabWidget QSpinBox:hover{\n"
"border:1px"
                        " solid red;\n"
"}\n"
"#InuseInvGroupBox1,#InuseInvGroupBoxOfficeEquip,#InuseInvGroupBoxHomeEquip,#offboardingGroupBox,#sendRepairGroupBox{\n"
"color:#003854;\n"
"border:1px dashed #003854;\n"
"}\n"
"\n"
"#offboardingGroupBox,#sendRepairGroupBox {\n"
"padding:10p 10px;\n"
"}\n"
"\n"
"#offboardingGroupBox QPushButton,#sendRepairGroupBox QPushButton{\n"
"padding:10px;\n"
"color:#003854;\n"
"}\n"
"#offboardingBtn,#sendForRepairBtn{\n"
"border:1px solid #003854;\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"}\n"
" #offboardingBtn:hover,#sendForRepairBtn:hover{\n"
"background-color:#003854;\n"
"color:#fff;\n"
"\n"
"}\n"
"\n"
"#inuseInvGenerateExcelBtn{\n"
"border:1px solid #003854;\n"
"border-radius:2px;\n"
"padding:5px;\n"
"color:#003854;\n"
"\n"
"}\n"
"#inuseInvGenerateExcelBtn:hover{\n"
"background-color:#003854;\n"
"color:#fff;\n"
"}")
        self.verticalLayout_17 = QVBoxLayout(self.inUseInvPage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.inUseInvPage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color:#003854;")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10)

        self.widget_14 = QWidget(self.inUseInvPage)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setStyleSheet(u"")
        self.verticalLayout_54 = QVBoxLayout(self.widget_14)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.inUseInvTabWidget = QWidget(self.widget_14)
        self.inUseInvTabWidget.setObjectName(u"inUseInvTabWidget")
        self.inUseInvTabWidget.setStyleSheet(u"")
        self.verticalLayout_53 = QVBoxLayout(self.inUseInvTabWidget)
        self.verticalLayout_53.setSpacing(0)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.verticalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.widget_25 = QWidget(self.inUseInvTabWidget)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, -1, -1, 0)
        self.InuseInvWidget1 = QWidget(self.widget_25)
        self.InuseInvWidget1.setObjectName(u"InuseInvWidget1")
        self.InuseInvWidget1.setFont(font1)
        self.verticalLayout_56 = QVBoxLayout(self.InuseInvWidget1)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalLayout_56.setContentsMargins(-1, 0, -1, 0)
        self.InuseInvGroupBox1 = QGroupBox(self.InuseInvWidget1)
        self.InuseInvGroupBox1.setObjectName(u"InuseInvGroupBox1")
        self.InuseInvGroupBox1.setFont(font1)
        self.InuseInvGroupBox1.setStyleSheet(u"padding-top:10px;")
        self.verticalLayout_55 = QVBoxLayout(self.InuseInvGroupBox1)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.widget_53 = QWidget(self.InuseInvGroupBox1)
        self.widget_53.setObjectName(u"widget_53")
        self.horizontalLayout_68 = QHBoxLayout(self.widget_53)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.txtInuseLaptopSerial = QLineEdit(self.widget_53)
        self.txtInuseLaptopSerial.setObjectName(u"txtInuseLaptopSerial")
        self.txtInuseLaptopSerial.setContextMenuPolicy(Qt.NoContextMenu)
        self.txtInuseLaptopSerial.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.horizontalLayout_68.addWidget(self.txtInuseLaptopSerial)

        self.label_30 = QLabel(self.widget_53)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color:red;")

        self.horizontalLayout_68.addWidget(self.label_30, 0, Qt.AlignTop)


        self.verticalLayout_55.addWidget(self.widget_53)

        self.widget_54 = QWidget(self.InuseInvGroupBox1)
        self.widget_54.setObjectName(u"widget_54")
        self.horizontalLayout_69 = QHBoxLayout(self.widget_54)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.txtInuseLaptopModel = QLineEdit(self.widget_54)
        self.txtInuseLaptopModel.setObjectName(u"txtInuseLaptopModel")
        self.txtInuseLaptopModel.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_69.addWidget(self.txtInuseLaptopModel)

        self.label_31 = QLabel(self.widget_54)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"color:red;")

        self.horizontalLayout_69.addWidget(self.label_31, 0, Qt.AlignTop)


        self.verticalLayout_55.addWidget(self.widget_54)

        self.widget_69 = QWidget(self.InuseInvGroupBox1)
        self.widget_69.setObjectName(u"widget_69")
        self.horizontalLayout_70 = QHBoxLayout(self.widget_69)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.txtInuseUser = QLineEdit(self.widget_69)
        self.txtInuseUser.setObjectName(u"txtInuseUser")

        self.horizontalLayout_70.addWidget(self.txtInuseUser)

        self.label_32 = QLabel(self.widget_69)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"color:red;")

        self.horizontalLayout_70.addWidget(self.label_32, 0, Qt.AlignTop)


        self.verticalLayout_55.addWidget(self.widget_69)

        self.widget_70 = QWidget(self.InuseInvGroupBox1)
        self.widget_70.setObjectName(u"widget_70")
        self.verticalLayout_39 = QVBoxLayout(self.widget_70)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.txtInuseLaptopStatus = QLineEdit(self.widget_70)
        self.txtInuseLaptopStatus.setObjectName(u"txtInuseLaptopStatus")

        self.verticalLayout_39.addWidget(self.txtInuseLaptopStatus)


        self.verticalLayout_55.addWidget(self.widget_70)


        self.verticalLayout_56.addWidget(self.InuseInvGroupBox1)


        self.horizontalLayout_33.addWidget(self.InuseInvWidget1)

        self.InuseInvWidget2 = QWidget(self.widget_25)
        self.InuseInvWidget2.setObjectName(u"InuseInvWidget2")
        self.verticalLayout_47 = QVBoxLayout(self.InuseInvWidget2)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.InuseInvGroupBoxOfficeEquip = QGroupBox(self.InuseInvWidget2)
        self.InuseInvGroupBoxOfficeEquip.setObjectName(u"InuseInvGroupBoxOfficeEquip")
        self.InuseInvGroupBoxOfficeEquip.setFont(font1)
        self.InuseInvGroupBoxOfficeEquip.setStyleSheet(u"")
        self.verticalLayout_48 = QVBoxLayout(self.InuseInvGroupBoxOfficeEquip)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.officeKeyboardWidget = QWidget(self.InuseInvGroupBoxOfficeEquip)
        self.officeKeyboardWidget.setObjectName(u"officeKeyboardWidget")
        self.horizontalLayout_52 = QHBoxLayout(self.officeKeyboardWidget)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.officeKeyboardRadioNew = QRadioButton(self.officeKeyboardWidget)
        self.officeKeyboardRadioNew.setObjectName(u"officeKeyboardRadioNew")
        self.officeKeyboardRadioNew.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout_52.addWidget(self.officeKeyboardRadioNew)

        self.officeKeyboardRadioStocked = QRadioButton(self.officeKeyboardWidget)
        self.officeKeyboardRadioStocked.setObjectName(u"officeKeyboardRadioStocked")
        self.officeKeyboardRadioStocked.setContextMenuPolicy(Qt.DefaultContextMenu)

        self.horizontalLayout_52.addWidget(self.officeKeyboardRadioStocked)


        self.verticalLayout_48.addWidget(self.officeKeyboardWidget)

        self.officeMouseWidget = QWidget(self.InuseInvGroupBoxOfficeEquip)
        self.officeMouseWidget.setObjectName(u"officeMouseWidget")
        self.horizontalLayout_51 = QHBoxLayout(self.officeMouseWidget)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.officeMouseRadioNew = QRadioButton(self.officeMouseWidget)
        self.officeMouseRadioNew.setObjectName(u"officeMouseRadioNew")

        self.horizontalLayout_51.addWidget(self.officeMouseRadioNew)

        self.officeMouseRadioStocked = QRadioButton(self.officeMouseWidget)
        self.officeMouseRadioStocked.setObjectName(u"officeMouseRadioStocked")

        self.horizontalLayout_51.addWidget(self.officeMouseRadioStocked)


        self.verticalLayout_48.addWidget(self.officeMouseWidget)

        self.widget_44 = QWidget(self.InuseInvGroupBoxOfficeEquip)
        self.widget_44.setObjectName(u"widget_44")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_44)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.officeHeadphoneRadioNew = QRadioButton(self.widget_44)
        self.officeHeadphoneRadioNew.setObjectName(u"officeHeadphoneRadioNew")

        self.horizontalLayout_50.addWidget(self.officeHeadphoneRadioNew)

        self.officeHeadphoneRadioStocked = QRadioButton(self.widget_44)
        self.officeHeadphoneRadioStocked.setObjectName(u"officeHeadphoneRadioStocked")

        self.horizontalLayout_50.addWidget(self.officeHeadphoneRadioStocked)


        self.verticalLayout_48.addWidget(self.widget_44)

        self.widget_19 = QWidget(self.InuseInvGroupBoxOfficeEquip)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_49 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.officeDockRadioNew = QRadioButton(self.widget_19)
        self.officeDockRadioNew.setObjectName(u"officeDockRadioNew")

        self.horizontalLayout_49.addWidget(self.officeDockRadioNew)

        self.officeDockRadioStocked = QRadioButton(self.widget_19)
        self.officeDockRadioStocked.setObjectName(u"officeDockRadioStocked")

        self.horizontalLayout_49.addWidget(self.officeDockRadioStocked)


        self.verticalLayout_48.addWidget(self.widget_19)

        self.widget_55 = QWidget(self.InuseInvGroupBoxOfficeEquip)
        self.widget_55.setObjectName(u"widget_55")
        self.horizontalLayout_64 = QHBoxLayout(self.widget_55)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.widget_67 = QWidget(self.widget_55)
        self.widget_67.setObjectName(u"widget_67")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_67)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_21 = QLabel(self.widget_67)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font1)

        self.horizontalLayout_53.addWidget(self.label_21)

        self.officeEquipMonitorSpin = QSpinBox(self.widget_67)
        self.officeEquipMonitorSpin.setObjectName(u"officeEquipMonitorSpin")

        self.horizontalLayout_53.addWidget(self.officeEquipMonitorSpin)


        self.horizontalLayout_64.addWidget(self.widget_67)

        self.officeMonitorRadioNew = QRadioButton(self.widget_55)
        self.officeMonitorRadioNew.setObjectName(u"officeMonitorRadioNew")

        self.horizontalLayout_64.addWidget(self.officeMonitorRadioNew)

        self.officeMonitorRadioStocked = QRadioButton(self.widget_55)
        self.officeMonitorRadioStocked.setObjectName(u"officeMonitorRadioStocked")

        self.horizontalLayout_64.addWidget(self.officeMonitorRadioStocked)


        self.verticalLayout_48.addWidget(self.widget_55)

        self.widget_56 = QWidget(self.InuseInvGroupBoxOfficeEquip)
        self.widget_56.setObjectName(u"widget_56")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_56)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_20 = QLabel(self.widget_56)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font1)

        self.horizontalLayout_54.addWidget(self.label_20)

        self.extraEquipOffice = QLineEdit(self.widget_56)
        self.extraEquipOffice.setObjectName(u"extraEquipOffice")

        self.horizontalLayout_54.addWidget(self.extraEquipOffice)


        self.verticalLayout_48.addWidget(self.widget_56)


        self.verticalLayout_47.addWidget(self.InuseInvGroupBoxOfficeEquip)


        self.horizontalLayout_33.addWidget(self.InuseInvWidget2)

        self.InuseInvWidget3 = QWidget(self.widget_25)
        self.InuseInvWidget3.setObjectName(u"InuseInvWidget3")
        self.verticalLayout_49 = QVBoxLayout(self.InuseInvWidget3)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.InuseInvGroupBoxHomeEquip = QGroupBox(self.InuseInvWidget3)
        self.InuseInvGroupBoxHomeEquip.setObjectName(u"InuseInvGroupBoxHomeEquip")
        self.InuseInvGroupBoxHomeEquip.setFont(font1)
        self.InuseInvGroupBoxHomeEquip.setStyleSheet(u"")
        self.verticalLayout_50 = QVBoxLayout(self.InuseInvGroupBoxHomeEquip)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.widget_59 = QWidget(self.InuseInvGroupBoxHomeEquip)
        self.widget_59.setObjectName(u"widget_59")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_59)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.homeKeyboardRadioNew = QRadioButton(self.widget_59)
        self.homeKeyboardRadioNew.setObjectName(u"homeKeyboardRadioNew")

        self.horizontalLayout_57.addWidget(self.homeKeyboardRadioNew)

        self.homeKeyboardRadioStocked = QRadioButton(self.widget_59)
        self.homeKeyboardRadioStocked.setObjectName(u"homeKeyboardRadioStocked")

        self.horizontalLayout_57.addWidget(self.homeKeyboardRadioStocked)


        self.verticalLayout_50.addWidget(self.widget_59)

        self.widget_62 = QWidget(self.InuseInvGroupBoxHomeEquip)
        self.widget_62.setObjectName(u"widget_62")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_62)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.homeMouseRadioNew = QRadioButton(self.widget_62)
        self.homeMouseRadioNew.setObjectName(u"homeMouseRadioNew")

        self.horizontalLayout_60.addWidget(self.homeMouseRadioNew)

        self.homeMouseRadioStocked = QRadioButton(self.widget_62)
        self.homeMouseRadioStocked.setObjectName(u"homeMouseRadioStocked")

        self.horizontalLayout_60.addWidget(self.homeMouseRadioStocked)


        self.verticalLayout_50.addWidget(self.widget_62)

        self.widget_60 = QWidget(self.InuseInvGroupBoxHomeEquip)
        self.widget_60.setObjectName(u"widget_60")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_60)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.homeHeadphoneRadioNew = QRadioButton(self.widget_60)
        self.homeHeadphoneRadioNew.setObjectName(u"homeHeadphoneRadioNew")

        self.horizontalLayout_58.addWidget(self.homeHeadphoneRadioNew)

        self.homeHeadphoneRadioStocked = QRadioButton(self.widget_60)
        self.homeHeadphoneRadioStocked.setObjectName(u"homeHeadphoneRadioStocked")

        self.horizontalLayout_58.addWidget(self.homeHeadphoneRadioStocked)


        self.verticalLayout_50.addWidget(self.widget_60)

        self.widget_58 = QWidget(self.InuseInvGroupBoxHomeEquip)
        self.widget_58.setObjectName(u"widget_58")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_58)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.homeDockRadioNew = QRadioButton(self.widget_58)
        self.homeDockRadioNew.setObjectName(u"homeDockRadioNew")

        self.horizontalLayout_56.addWidget(self.homeDockRadioNew)

        self.homeDockRadioStocked = QRadioButton(self.widget_58)
        self.homeDockRadioStocked.setObjectName(u"homeDockRadioStocked")

        self.horizontalLayout_56.addWidget(self.homeDockRadioStocked)


        self.verticalLayout_50.addWidget(self.widget_58)

        self.widget_61 = QWidget(self.InuseInvGroupBoxHomeEquip)
        self.widget_61.setObjectName(u"widget_61")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_61)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.widget_68 = QWidget(self.widget_61)
        self.widget_68.setObjectName(u"widget_68")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_68)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_28 = QLabel(self.widget_68)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font1)

        self.horizontalLayout_59.addWidget(self.label_28)

        self.homeEquipMonitorSpin = QSpinBox(self.widget_68)
        self.homeEquipMonitorSpin.setObjectName(u"homeEquipMonitorSpin")

        self.horizontalLayout_59.addWidget(self.homeEquipMonitorSpin)


        self.horizontalLayout_65.addWidget(self.widget_68)

        self.homeMonitorRadioNew = QRadioButton(self.widget_61)
        self.homeMonitorRadioNew.setObjectName(u"homeMonitorRadioNew")

        self.horizontalLayout_65.addWidget(self.homeMonitorRadioNew)

        self.homeMonitorRadioStocked = QRadioButton(self.widget_61)
        self.homeMonitorRadioStocked.setObjectName(u"homeMonitorRadioStocked")

        self.horizontalLayout_65.addWidget(self.homeMonitorRadioStocked)


        self.verticalLayout_50.addWidget(self.widget_61)

        self.widget_57 = QWidget(self.InuseInvGroupBoxHomeEquip)
        self.widget_57.setObjectName(u"widget_57")
        self.horizontalLayout_55 = QHBoxLayout(self.widget_57)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.label_27 = QLabel(self.widget_57)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font1)

        self.horizontalLayout_55.addWidget(self.label_27)

        self.extraEquipHome = QLineEdit(self.widget_57)
        self.extraEquipHome.setObjectName(u"extraEquipHome")

        self.horizontalLayout_55.addWidget(self.extraEquipHome)


        self.verticalLayout_50.addWidget(self.widget_57)


        self.verticalLayout_49.addWidget(self.InuseInvGroupBoxHomeEquip)


        self.horizontalLayout_33.addWidget(self.InuseInvWidget3)

        self.widget_96 = QWidget(self.widget_25)
        self.widget_96.setObjectName(u"widget_96")
        self.verticalLayout_65 = QVBoxLayout(self.widget_96)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.widget_97 = QWidget(self.widget_96)
        self.widget_97.setObjectName(u"widget_97")
        self.verticalLayout_70 = QVBoxLayout(self.widget_97)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.offboardingGroupBox = QGroupBox(self.widget_97)
        self.offboardingGroupBox.setObjectName(u"offboardingGroupBox")
        self.offboardingGroupBox.setFont(font1)
        self.offboardingGroupBox.setStyleSheet(u"")
        self.verticalLayout_71 = QVBoxLayout(self.offboardingGroupBox)
        self.verticalLayout_71.setSpacing(0)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.verticalLayout_71.setContentsMargins(0, 0, 0, 0)
        self.offboardingLaptopSerial = QLineEdit(self.offboardingGroupBox)
        self.offboardingLaptopSerial.setObjectName(u"offboardingLaptopSerial")
        self.offboardingLaptopSerial.setEnabled(False)
        self.offboardingLaptopSerial.setStyleSheet(u"margin-top:10px;")

        self.verticalLayout_71.addWidget(self.offboardingLaptopSerial)

        self.offboardingBtn = QPushButton(self.offboardingGroupBox)
        self.offboardingBtn.setObjectName(u"offboardingBtn")
        self.offboardingBtn.setFont(font1)
        self.offboardingBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_71.addWidget(self.offboardingBtn)


        self.verticalLayout_70.addWidget(self.offboardingGroupBox)


        self.verticalLayout_65.addWidget(self.widget_97)

        self.widget_98 = QWidget(self.widget_96)
        self.widget_98.setObjectName(u"widget_98")
        self.verticalLayout_72 = QVBoxLayout(self.widget_98)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.sendRepairGroupBox = QGroupBox(self.widget_98)
        self.sendRepairGroupBox.setObjectName(u"sendRepairGroupBox")
        self.sendRepairGroupBox.setFont(font1)
        self.verticalLayout_73 = QVBoxLayout(self.sendRepairGroupBox)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.sendForRepairLaptopSerial = QLineEdit(self.sendRepairGroupBox)
        self.sendForRepairLaptopSerial.setObjectName(u"sendForRepairLaptopSerial")
        self.sendForRepairLaptopSerial.setEnabled(False)
        self.sendForRepairLaptopSerial.setStyleSheet(u"margin-top:10px;")

        self.verticalLayout_73.addWidget(self.sendForRepairLaptopSerial)

        self.widget_99 = QWidget(self.sendRepairGroupBox)
        self.widget_99.setObjectName(u"widget_99")
        self.horizontalLayout_91 = QHBoxLayout(self.widget_99)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.refreshSpareLaptop = QPushButton(self.widget_99)
        self.refreshSpareLaptop.setObjectName(u"refreshSpareLaptop")
        self.refreshSpareLaptop.setCursor(QCursor(Qt.PointingHandCursor))
        icon20 = QIcon()
        icon20.addFile(u":/Icons/Icons/refresh-ccw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshSpareLaptop.setIcon(icon20)

        self.horizontalLayout_91.addWidget(self.refreshSpareLaptop)

        self.spareCombo = QComboBox(self.widget_99)
        self.spareCombo.setObjectName(u"spareCombo")
        self.spareCombo.setStyleSheet(u"color:#003854;")

        self.horizontalLayout_91.addWidget(self.spareCombo)


        self.verticalLayout_73.addWidget(self.widget_99)

        self.sendForRepairBtn = QPushButton(self.sendRepairGroupBox)
        self.sendForRepairBtn.setObjectName(u"sendForRepairBtn")
        self.sendForRepairBtn.setFont(font1)
        self.sendForRepairBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_73.addWidget(self.sendForRepairBtn)


        self.verticalLayout_72.addWidget(self.sendRepairGroupBox)


        self.verticalLayout_65.addWidget(self.widget_98)


        self.horizontalLayout_33.addWidget(self.widget_96)


        self.verticalLayout_53.addWidget(self.widget_25)

        self.InuseInvCrudBtn = QWidget(self.inUseInvTabWidget)
        self.InuseInvCrudBtn.setObjectName(u"InuseInvCrudBtn")
        sizePolicy5.setHeightForWidth(self.InuseInvCrudBtn.sizePolicy().hasHeightForWidth())
        self.InuseInvCrudBtn.setSizePolicy(sizePolicy5)
        self.horizontalLayout_42 = QHBoxLayout(self.InuseInvCrudBtn)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, 0, -1, 0)
        self.addInuseInvBtn = QPushButton(self.InuseInvCrudBtn)
        self.addInuseInvBtn.setObjectName(u"addInuseInvBtn")
        self.addInuseInvBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon21 = QIcon()
        icon21.addFile(u":/Icons/Icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.addInuseInvBtn.setIcon(icon21)

        self.horizontalLayout_42.addWidget(self.addInuseInvBtn)

        self.updateInuseInvBtn = QPushButton(self.InuseInvCrudBtn)
        self.updateInuseInvBtn.setObjectName(u"updateInuseInvBtn")
        self.updateInuseInvBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateInuseInvBtn.setIcon(icon20)

        self.horizontalLayout_42.addWidget(self.updateInuseInvBtn)

        self.clearInuseInvBtn = QPushButton(self.InuseInvCrudBtn)
        self.clearInuseInvBtn.setObjectName(u"clearInuseInvBtn")
        self.clearInuseInvBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon22 = QIcon()
        icon22.addFile(u":/Icons/Icons/check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clearInuseInvBtn.setIcon(icon22)

        self.horizontalLayout_42.addWidget(self.clearInuseInvBtn)


        self.verticalLayout_53.addWidget(self.InuseInvCrudBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.widget_45 = QWidget(self.inUseInvTabWidget)
        self.widget_45.setObjectName(u"widget_45")
        self.verticalLayout_51 = QVBoxLayout(self.widget_45)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.widget_48 = QWidget(self.widget_45)
        self.widget_48.setObjectName(u"widget_48")
        self.widget_48.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_43 = QHBoxLayout(self.widget_48)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, -1)
        self.widget_49 = QWidget(self.widget_48)
        self.widget_49.setObjectName(u"widget_49")
        self.verticalLayout_52 = QVBoxLayout(self.widget_49)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(-1, 0, -1, 0)
        self.inuseInvGenerateExcelBtn = QPushButton(self.widget_49)
        self.inuseInvGenerateExcelBtn.setObjectName(u"inuseInvGenerateExcelBtn")
        self.inuseInvGenerateExcelBtn.setFont(font1)
        self.inuseInvGenerateExcelBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.inuseInvGenerateExcelBtn.setIcon(icon19)

        self.verticalLayout_52.addWidget(self.inuseInvGenerateExcelBtn)


        self.horizontalLayout_43.addWidget(self.widget_49)

        self.widget_50 = QWidget(self.widget_48)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_67 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.InuseLaptoSerialID = QLabel(self.widget_50)
        self.InuseLaptoSerialID.setObjectName(u"InuseLaptoSerialID")
        self.InuseLaptoSerialID.setEnabled(False)
        self.InuseLaptoSerialID.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"color:transparent;")

        self.horizontalLayout_67.addWidget(self.InuseLaptoSerialID)


        self.horizontalLayout_43.addWidget(self.widget_50)

        self.widget_51 = QWidget(self.widget_48)
        self.widget_51.setObjectName(u"widget_51")
        self.widget_51.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_66 = QHBoxLayout(self.widget_51)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.txtInuseSLNO = QLineEdit(self.widget_51)
        self.txtInuseSLNO.setObjectName(u"txtInuseSLNO")
        self.txtInuseSLNO.setEnabled(False)
        self.txtInuseSLNO.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"color:transparent;")
        self.txtInuseSLNO.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.txtInuseSLNO.setEchoMode(QLineEdit.NoEcho)

        self.horizontalLayout_66.addWidget(self.txtInuseSLNO)


        self.horizontalLayout_43.addWidget(self.widget_51)

        self.widget_52 = QWidget(self.widget_48)
        self.widget_52.setObjectName(u"widget_52")
        self.widget_52.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_48 = QHBoxLayout(self.widget_52)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(-1, 0, -1, 6)
        self.InUseRecordSearchTxt = QLineEdit(self.widget_52)
        self.InUseRecordSearchTxt.setObjectName(u"InUseRecordSearchTxt")
        sizePolicy4.setHeightForWidth(self.InUseRecordSearchTxt.sizePolicy().hasHeightForWidth())
        self.InUseRecordSearchTxt.setSizePolicy(sizePolicy4)
        self.InUseRecordSearchTxt.setMinimumSize(QSize(170, 0))
        self.InUseRecordSearchTxt.setMaximumSize(QSize(170, 16777215))
        self.InUseRecordSearchTxt.setFont(font6)
        self.InUseRecordSearchTxt.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.InUseRecordSearchTxt.setEchoMode(QLineEdit.Normal)
        self.InUseRecordSearchTxt.setAlignment(Qt.AlignCenter)
        self.InUseRecordSearchTxt.setClearButtonEnabled(True)

        self.horizontalLayout_48.addWidget(self.InUseRecordSearchTxt, 0, Qt.AlignRight)

        self.InUseRecordSearchCombo = QComboBox(self.widget_52)
        self.InUseRecordSearchCombo.addItem("")
        self.InUseRecordSearchCombo.addItem("")
        self.InUseRecordSearchCombo.addItem("")
        self.InUseRecordSearchCombo.setObjectName(u"InUseRecordSearchCombo")
        sizePolicy4.setHeightForWidth(self.InUseRecordSearchCombo.sizePolicy().hasHeightForWidth())
        self.InUseRecordSearchCombo.setSizePolicy(sizePolicy4)
        self.InUseRecordSearchCombo.setMinimumSize(QSize(170, 0))
        self.InUseRecordSearchCombo.setMaximumSize(QSize(170, 16777215))
        self.InUseRecordSearchCombo.setFont(font6)
        self.InUseRecordSearchCombo.setStyleSheet(u"color: #003854;")
        self.InUseRecordSearchCombo.setEditable(False)

        self.horizontalLayout_48.addWidget(self.InUseRecordSearchCombo, 0, Qt.AlignRight)


        self.horizontalLayout_43.addWidget(self.widget_52)


        self.verticalLayout_51.addWidget(self.widget_48)

        self.InUseTableWidget = QTableWidget(self.widget_45)
        if (self.InUseTableWidget.columnCount() < 22):
            self.InUseTableWidget.setColumnCount(22)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        icon23 = QIcon()
        icon23.addFile(u":/Icons/Icons/office.svg", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.Dense1Pattern)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        __qtablewidgetitem19.setForeground(brush);
        __qtablewidgetitem19.setIcon(icon23);
        self.InUseTableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setIcon(icon1);
        self.InUseTableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setIcon(icon23);
        self.InUseTableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setIcon(icon1);
        self.InUseTableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setIcon(icon23);
        self.InUseTableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setIcon(icon1);
        self.InUseTableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setIcon(icon23);
        self.InUseTableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setIcon(icon1);
        self.InUseTableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setIcon(icon23);
        self.InUseTableWidget.setHorizontalHeaderItem(15, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setIcon(icon1);
        self.InUseTableWidget.setHorizontalHeaderItem(16, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setIcon(icon23);
        self.InUseTableWidget.setHorizontalHeaderItem(17, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setIcon(icon1);
        self.InUseTableWidget.setHorizontalHeaderItem(18, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(19, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(20, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.InUseTableWidget.setHorizontalHeaderItem(21, __qtablewidgetitem33)
        self.InUseTableWidget.setObjectName(u"InUseTableWidget")
        sizePolicy5.setHeightForWidth(self.InUseTableWidget.sizePolicy().hasHeightForWidth())
        self.InUseTableWidget.setSizePolicy(sizePolicy5)
        self.InUseTableWidget.setMinimumSize(QSize(861, 334))
        self.InUseTableWidget.setStyleSheet(u"")
        self.InUseTableWidget.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.InUseTableWidget.setShowGrid(True)
        self.InUseTableWidget.setSortingEnabled(False)
        self.InUseTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.InUseTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.InUseTableWidget.horizontalHeader().setStretchLastSection(True)
        self.InUseTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.InUseTableWidget.verticalHeader().setMinimumSectionSize(24)
        self.InUseTableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.InUseTableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_51.addWidget(self.InUseTableWidget)


        self.verticalLayout_53.addWidget(self.widget_45)


        self.verticalLayout_54.addWidget(self.inUseInvTabWidget)


        self.verticalLayout_17.addWidget(self.widget_14)

        self.mainPages.addWidget(self.inUseInvPage)
        self.adminDashPage = QWidget()
        self.adminDashPage.setObjectName(u"adminDashPage")
        self.adminDashPage.setStyleSheet(u"\n"
"#adminDashboard{\n"
"border: none;\n"
"background-color:#bbc0cd;\n"
"} \n"
"\n"
"#EditAdminWidget,#RegisterAdminWidget{\n"
"background-color:#003854;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"\n"
"#RegisterAdminWidget QLineEdit,#EditAdminWidget QLineEdit,#RegisterAdminWidget QComboBox,#EditAdminWidget QComboBox{\n"
"color:#000;\n"
"background-color:#dcdcdd;\n"
"border:1px solid rgba(166,164,164,1);\n"
"border-radius:5px;\n"
"padding:5px 10px;\n"
"\n"
"}\n"
"\n"
"#RegisterAdminWidget QPushButton,#EditAdminWidget QPushButton{\n"
"padding:10px;\n"
"}\n"
"#editAdminInfoBtn,#registerAdminInfoBtn{\n"
"border:1px solid #fff;\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"}\n"
"\n"
"#deleteAdminInfoBtn{\n"
"border:1px solid red;\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"}\n"
"#deleteAdminInfoBtn:hover{\n"
"background:red;\n"
"color:#fff;\n"
"}\n"
"\n"
" #registerAdminInfoBtn:hover,#editAdminInfoBtn:hover{\n"
"background-color:#fff;\n"
"color:qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(54"
                        ",90,108,1) stop:1 rgba(54,90,108,1));\n"
"\n"
"}\n"
"#adminDashboard QTableWidget{\n"
"color:#003854;\n"
"background-color:#eaeaeb;\n"
"border:1px solid #4e5f8b;\n"
"border-radius:3px;\n"
"}\n"
"#adminDashboard QHeaderView::section{\n"
"background: #003854;\n"
"border:1px solid qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(54,90,108,1) stop:1 rgba(54,90,108,1));\n"
"color:#fff;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"")
        self.verticalLayout_79 = QVBoxLayout(self.adminDashPage)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.widget_84 = QWidget(self.adminDashPage)
        self.widget_84.setObjectName(u"widget_84")
        self.verticalLayout_57 = QVBoxLayout(self.widget_84)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_33 = QLabel(self.widget_84)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)
        self.label_33.setStyleSheet(u"color:#003854;")
        self.label_33.setAlignment(Qt.AlignCenter)

        self.verticalLayout_57.addWidget(self.label_33)

        self.adminDashboard = QWidget(self.widget_84)
        self.adminDashboard.setObjectName(u"adminDashboard")
        self.adminDashboard.setStyleSheet(u"#sendRepairtoServerGroupBox QGroupBox{\n"
"color:#4e5f8b;\n"
"border:1px dashed #4e5f8b;\n"
"}\n"
" #sendRepairtoUserGroupBox QGroupBox{\n"
"color:#4e5f8b;\n"
"border:1px dotted #4e5f8b;\n"
"}")
        self.verticalLayout_58 = QVBoxLayout(self.adminDashboard)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.widget_85 = QWidget(self.adminDashboard)
        self.widget_85.setObjectName(u"widget_85")
        self.horizontalLayout_71 = QHBoxLayout(self.widget_85)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalLayout_71.setContentsMargins(-1, 0, -1, 0)
        self.widget_88 = QWidget(self.widget_85)
        self.widget_88.setObjectName(u"widget_88")
        self.horizontalLayout_101 = QHBoxLayout(self.widget_88)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.label_69 = QLabel(self.widget_88)
        self.label_69.setObjectName(u"label_69")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy6)
        self.label_69.setPixmap(QPixmap(u":/Icons/Icons/admin-dash-icon.svg"))

        self.horizontalLayout_101.addWidget(self.label_69)


        self.horizontalLayout_71.addWidget(self.widget_88)

        self.EditAdminWidget = QWidget(self.widget_85)
        self.EditAdminWidget.setObjectName(u"EditAdminWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.EditAdminWidget.sizePolicy().hasHeightForWidth())
        self.EditAdminWidget.setSizePolicy(sizePolicy7)
        self.verticalLayout_59 = QVBoxLayout(self.EditAdminWidget)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_35 = QLabel(self.EditAdminWidget)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font4)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_59.addWidget(self.label_35)

        self.widget_90 = QWidget(self.EditAdminWidget)
        self.widget_90.setObjectName(u"widget_90")
        self.horizontalLayout_74 = QHBoxLayout(self.widget_90)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.label_41 = QLabel(self.widget_90)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font1)
        self.label_41.setScaledContents(True)

        self.horizontalLayout_74.addWidget(self.label_41, 0, Qt.AlignLeft)

        self.txtDashAdminID = QLineEdit(self.widget_90)
        self.txtDashAdminID.setObjectName(u"txtDashAdminID")
        self.txtDashAdminID.setEnabled(False)
        sizePolicy.setHeightForWidth(self.txtDashAdminID.sizePolicy().hasHeightForWidth())
        self.txtDashAdminID.setSizePolicy(sizePolicy)

        self.horizontalLayout_74.addWidget(self.txtDashAdminID)


        self.verticalLayout_59.addWidget(self.widget_90)

        self.widget_101 = QWidget(self.EditAdminWidget)
        self.widget_101.setObjectName(u"widget_101")
        self.horizontalLayout_89 = QHBoxLayout(self.widget_101)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_53 = QLabel(self.widget_101)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font1)

        self.horizontalLayout_89.addWidget(self.label_53, 0, Qt.AlignLeft)

        self.txtDashAdminFname = QLineEdit(self.widget_101)
        self.txtDashAdminFname.setObjectName(u"txtDashAdminFname")
        sizePolicy.setHeightForWidth(self.txtDashAdminFname.sizePolicy().hasHeightForWidth())
        self.txtDashAdminFname.setSizePolicy(sizePolicy)

        self.horizontalLayout_89.addWidget(self.txtDashAdminFname)


        self.verticalLayout_59.addWidget(self.widget_101)

        self.widget_100 = QWidget(self.EditAdminWidget)
        self.widget_100.setObjectName(u"widget_100")
        self.horizontalLayout_86 = QHBoxLayout(self.widget_100)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_50 = QLabel(self.widget_100)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font1)

        self.horizontalLayout_86.addWidget(self.label_50, 0, Qt.AlignLeft)

        self.txtDashAdminLname = QLineEdit(self.widget_100)
        self.txtDashAdminLname.setObjectName(u"txtDashAdminLname")
        sizePolicy.setHeightForWidth(self.txtDashAdminLname.sizePolicy().hasHeightForWidth())
        self.txtDashAdminLname.setSizePolicy(sizePolicy)

        self.horizontalLayout_86.addWidget(self.txtDashAdminLname)


        self.verticalLayout_59.addWidget(self.widget_100)

        self.widget_93 = QWidget(self.EditAdminWidget)
        self.widget_93.setObjectName(u"widget_93")
        self.horizontalLayout_83 = QHBoxLayout(self.widget_93)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.label_47 = QLabel(self.widget_93)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font1)

        self.horizontalLayout_83.addWidget(self.label_47, 0, Qt.AlignLeft)

        self.txtDashAdminUsername = QLineEdit(self.widget_93)
        self.txtDashAdminUsername.setObjectName(u"txtDashAdminUsername")
        sizePolicy.setHeightForWidth(self.txtDashAdminUsername.sizePolicy().hasHeightForWidth())
        self.txtDashAdminUsername.setSizePolicy(sizePolicy)

        self.horizontalLayout_83.addWidget(self.txtDashAdminUsername)


        self.verticalLayout_59.addWidget(self.widget_93)

        self.widget_92 = QWidget(self.EditAdminWidget)
        self.widget_92.setObjectName(u"widget_92")
        self.horizontalLayout_82 = QHBoxLayout(self.widget_92)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_43 = QLabel(self.widget_92)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font1)

        self.horizontalLayout_82.addWidget(self.label_43, 0, Qt.AlignLeft)

        self.txtDashAdminEmail = QLineEdit(self.widget_92)
        self.txtDashAdminEmail.setObjectName(u"txtDashAdminEmail")
        sizePolicy.setHeightForWidth(self.txtDashAdminEmail.sizePolicy().hasHeightForWidth())
        self.txtDashAdminEmail.setSizePolicy(sizePolicy)

        self.horizontalLayout_82.addWidget(self.txtDashAdminEmail)


        self.verticalLayout_59.addWidget(self.widget_92)

        self.widget_91 = QWidget(self.EditAdminWidget)
        self.widget_91.setObjectName(u"widget_91")
        self.horizontalLayout_75 = QHBoxLayout(self.widget_91)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_42 = QLabel(self.widget_91)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font1)

        self.horizontalLayout_75.addWidget(self.label_42, 0, Qt.AlignLeft)

        self.txtDashAdminStatusCombo = QComboBox(self.widget_91)
        self.txtDashAdminStatusCombo.addItem("")
        self.txtDashAdminStatusCombo.addItem("")
        self.txtDashAdminStatusCombo.addItem("")
        self.txtDashAdminStatusCombo.setObjectName(u"txtDashAdminStatusCombo")
        sizePolicy.setHeightForWidth(self.txtDashAdminStatusCombo.sizePolicy().hasHeightForWidth())
        self.txtDashAdminStatusCombo.setSizePolicy(sizePolicy)
        self.txtDashAdminStatusCombo.setStyleSheet(u"color:#404d6f;")

        self.horizontalLayout_75.addWidget(self.txtDashAdminStatusCombo)


        self.verticalLayout_59.addWidget(self.widget_91)

        self.widget_89 = QWidget(self.EditAdminWidget)
        self.widget_89.setObjectName(u"widget_89")
        self.horizontalLayout_73 = QHBoxLayout(self.widget_89)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_38 = QLabel(self.widget_89)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font1)

        self.horizontalLayout_73.addWidget(self.label_38, 0, Qt.AlignLeft)

        self.txtDashAdminFlagCombo = QComboBox(self.widget_89)
        self.txtDashAdminFlagCombo.addItem("")
        self.txtDashAdminFlagCombo.addItem("")
        self.txtDashAdminFlagCombo.addItem("")
        self.txtDashAdminFlagCombo.addItem("")
        self.txtDashAdminFlagCombo.setObjectName(u"txtDashAdminFlagCombo")
        sizePolicy.setHeightForWidth(self.txtDashAdminFlagCombo.sizePolicy().hasHeightForWidth())
        self.txtDashAdminFlagCombo.setSizePolicy(sizePolicy)
        self.txtDashAdminFlagCombo.setStyleSheet(u"color:#404d6f;")

        self.horizontalLayout_73.addWidget(self.txtDashAdminFlagCombo)


        self.verticalLayout_59.addWidget(self.widget_89)

        self.widget_102 = QWidget(self.EditAdminWidget)
        self.widget_102.setObjectName(u"widget_102")
        self.horizontalLayout_103 = QHBoxLayout(self.widget_102)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.horizontalLayout_103.setContentsMargins(-1, 0, -1, 0)
        self.editAdminInfoBtn = QPushButton(self.widget_102)
        self.editAdminInfoBtn.setObjectName(u"editAdminInfoBtn")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.editAdminInfoBtn.sizePolicy().hasHeightForWidth())
        self.editAdminInfoBtn.setSizePolicy(sizePolicy8)
        self.editAdminInfoBtn.setFont(font1)
        self.editAdminInfoBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_103.addWidget(self.editAdminInfoBtn)

        self.deleteAdminInfoBtn = QPushButton(self.widget_102)
        self.deleteAdminInfoBtn.setObjectName(u"deleteAdminInfoBtn")
        self.deleteAdminInfoBtn.setFont(font1)
        self.deleteAdminInfoBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_103.addWidget(self.deleteAdminInfoBtn)


        self.verticalLayout_59.addWidget(self.widget_102)


        self.horizontalLayout_71.addWidget(self.EditAdminWidget)

        self.RegisterAdminWidget = QWidget(self.widget_85)
        self.RegisterAdminWidget.setObjectName(u"RegisterAdminWidget")
        sizePolicy7.setHeightForWidth(self.RegisterAdminWidget.sizePolicy().hasHeightForWidth())
        self.RegisterAdminWidget.setSizePolicy(sizePolicy7)
        self.verticalLayout_61 = QVBoxLayout(self.RegisterAdminWidget)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_56 = QLabel(self.RegisterAdminWidget)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font4)
        self.label_56.setAlignment(Qt.AlignCenter)

        self.verticalLayout_61.addWidget(self.label_56)

        self.widget_106 = QWidget(self.RegisterAdminWidget)
        self.widget_106.setObjectName(u"widget_106")
        self.horizontalLayout_97 = QHBoxLayout(self.widget_106)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_60 = QLabel(self.widget_106)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font1)

        self.horizontalLayout_97.addWidget(self.label_60, 0, Qt.AlignLeft)

        self.txtDashRegAdminFname = QLineEdit(self.widget_106)
        self.txtDashRegAdminFname.setObjectName(u"txtDashRegAdminFname")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminFname.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminFname.setSizePolicy(sizePolicy)

        self.horizontalLayout_97.addWidget(self.txtDashRegAdminFname)


        self.verticalLayout_61.addWidget(self.widget_106)

        self.widget_109 = QWidget(self.RegisterAdminWidget)
        self.widget_109.setObjectName(u"widget_109")
        self.horizontalLayout_100 = QHBoxLayout(self.widget_109)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_68 = QLabel(self.widget_109)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font1)

        self.horizontalLayout_100.addWidget(self.label_68)

        self.txtDashRegAdminLname = QLineEdit(self.widget_109)
        self.txtDashRegAdminLname.setObjectName(u"txtDashRegAdminLname")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminLname.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminLname.setSizePolicy(sizePolicy)

        self.horizontalLayout_100.addWidget(self.txtDashRegAdminLname)


        self.verticalLayout_61.addWidget(self.widget_109)

        self.widget_103 = QWidget(self.RegisterAdminWidget)
        self.widget_103.setObjectName(u"widget_103")
        self.horizontalLayout_95 = QHBoxLayout(self.widget_103)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.label_55 = QLabel(self.widget_103)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font1)

        self.horizontalLayout_95.addWidget(self.label_55)

        self.txtDashRegAdminUsername = QLineEdit(self.widget_103)
        self.txtDashRegAdminUsername.setObjectName(u"txtDashRegAdminUsername")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminUsername.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminUsername.setSizePolicy(sizePolicy)

        self.horizontalLayout_95.addWidget(self.txtDashRegAdminUsername)


        self.verticalLayout_61.addWidget(self.widget_103)

        self.widget_111 = QWidget(self.RegisterAdminWidget)
        self.widget_111.setObjectName(u"widget_111")
        self.horizontalLayout_102 = QHBoxLayout(self.widget_111)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_70 = QLabel(self.widget_111)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font1)

        self.horizontalLayout_102.addWidget(self.label_70)

        self.txtDashRegAdminPassword = QLineEdit(self.widget_111)
        self.txtDashRegAdminPassword.setObjectName(u"txtDashRegAdminPassword")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminPassword.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminPassword.setSizePolicy(sizePolicy)
        self.txtDashRegAdminPassword.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_102.addWidget(self.txtDashRegAdminPassword)


        self.verticalLayout_61.addWidget(self.widget_111)

        self.widget_108 = QWidget(self.RegisterAdminWidget)
        self.widget_108.setObjectName(u"widget_108")
        self.horizontalLayout_99 = QHBoxLayout(self.widget_108)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_67 = QLabel(self.widget_108)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font1)

        self.horizontalLayout_99.addWidget(self.label_67)

        self.txtDashRegAdminEmail = QLineEdit(self.widget_108)
        self.txtDashRegAdminEmail.setObjectName(u"txtDashRegAdminEmail")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminEmail.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminEmail.setSizePolicy(sizePolicy)
        self.txtDashRegAdminEmail.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.horizontalLayout_99.addWidget(self.txtDashRegAdminEmail)


        self.verticalLayout_61.addWidget(self.widget_108)

        self.widget_105 = QWidget(self.RegisterAdminWidget)
        self.widget_105.setObjectName(u"widget_105")
        self.horizontalLayout_96 = QHBoxLayout(self.widget_105)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.label_57 = QLabel(self.widget_105)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font1)

        self.horizontalLayout_96.addWidget(self.label_57)

        self.txtDashRegAdminStatusCombo = QComboBox(self.widget_105)
        self.txtDashRegAdminStatusCombo.addItem("")
        self.txtDashRegAdminStatusCombo.addItem("")
        self.txtDashRegAdminStatusCombo.addItem("")
        self.txtDashRegAdminStatusCombo.setObjectName(u"txtDashRegAdminStatusCombo")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminStatusCombo.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminStatusCombo.setSizePolicy(sizePolicy)
        self.txtDashRegAdminStatusCombo.setStyleSheet(u"color:#404d6f;")

        self.horizontalLayout_96.addWidget(self.txtDashRegAdminStatusCombo)


        self.verticalLayout_61.addWidget(self.widget_105)

        self.widget_107 = QWidget(self.RegisterAdminWidget)
        self.widget_107.setObjectName(u"widget_107")
        self.horizontalLayout_98 = QHBoxLayout(self.widget_107)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_66 = QLabel(self.widget_107)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font1)

        self.horizontalLayout_98.addWidget(self.label_66)

        self.txtDashRegAdminFlagCombo = QComboBox(self.widget_107)
        self.txtDashRegAdminFlagCombo.addItem("")
        self.txtDashRegAdminFlagCombo.addItem("")
        self.txtDashRegAdminFlagCombo.addItem("")
        self.txtDashRegAdminFlagCombo.addItem("")
        self.txtDashRegAdminFlagCombo.setObjectName(u"txtDashRegAdminFlagCombo")
        sizePolicy.setHeightForWidth(self.txtDashRegAdminFlagCombo.sizePolicy().hasHeightForWidth())
        self.txtDashRegAdminFlagCombo.setSizePolicy(sizePolicy)
        self.txtDashRegAdminFlagCombo.setStyleSheet(u"color:#404d6f;")

        self.horizontalLayout_98.addWidget(self.txtDashRegAdminFlagCombo)


        self.verticalLayout_61.addWidget(self.widget_107)

        self.widget_104 = QWidget(self.RegisterAdminWidget)
        self.widget_104.setObjectName(u"widget_104")
        self.verticalLayout_78 = QVBoxLayout(self.widget_104)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(-1, 0, -1, 0)
        self.registerAdminInfoBtn = QPushButton(self.widget_104)
        self.registerAdminInfoBtn.setObjectName(u"registerAdminInfoBtn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.registerAdminInfoBtn.sizePolicy().hasHeightForWidth())
        self.registerAdminInfoBtn.setSizePolicy(sizePolicy9)
        self.registerAdminInfoBtn.setFont(font1)
        self.registerAdminInfoBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_78.addWidget(self.registerAdminInfoBtn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_61.addWidget(self.widget_104)


        self.horizontalLayout_71.addWidget(self.RegisterAdminWidget)

        self.widget_86 = QWidget(self.widget_85)
        self.widget_86.setObjectName(u"widget_86")
        self.verticalLayout_63 = QVBoxLayout(self.widget_86)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_63.addItem(self.horizontalSpacer)


        self.horizontalLayout_71.addWidget(self.widget_86)


        self.verticalLayout_58.addWidget(self.widget_85)

        self.widget_87 = QWidget(self.adminDashboard)
        self.widget_87.setObjectName(u"widget_87")
        self.verticalLayout_75 = QVBoxLayout(self.widget_87)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.adminDashTable = QTableWidget(self.widget_87)
        if (self.adminDashTable.columnCount() < 9):
            self.adminDashTable.setColumnCount(9)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(5, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(6, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(7, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.adminDashTable.setHorizontalHeaderItem(8, __qtablewidgetitem42)
        self.adminDashTable.setObjectName(u"adminDashTable")
        sizePolicy5.setHeightForWidth(self.adminDashTable.sizePolicy().hasHeightForWidth())
        self.adminDashTable.setSizePolicy(sizePolicy5)
        self.adminDashTable.setMinimumSize(QSize(861, 334))
        self.adminDashTable.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.adminDashTable.setShowGrid(True)
        self.adminDashTable.setSortingEnabled(False)
        self.adminDashTable.horizontalHeader().setCascadingSectionResizes(False)
        self.adminDashTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.adminDashTable.horizontalHeader().setStretchLastSection(True)
        self.adminDashTable.verticalHeader().setCascadingSectionResizes(False)
        self.adminDashTable.verticalHeader().setMinimumSectionSize(24)
        self.adminDashTable.verticalHeader().setProperty("showSortIndicator", False)
        self.adminDashTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_75.addWidget(self.adminDashTable)


        self.verticalLayout_58.addWidget(self.widget_87)


        self.verticalLayout_57.addWidget(self.adminDashboard)


        self.verticalLayout_79.addWidget(self.widget_84)

        self.mainPages.addWidget(self.adminDashPage)
        self.sentForRepairPage = QWidget()
        self.sentForRepairPage.setObjectName(u"sentForRepairPage")
        self.sentForRepairPage.setStyleSheet(u"\n"
"/** SENT FOR REPAIRS TAB PANE ******/\n"
"\n"
"#sentForRepairTabWidget{\n"
"border: none;\n"
"background-color:#bbc0cd;\n"
"} \n"
"\n"
"\n"
"#sentForRepairTabWidget QLineEdit,#sentForRepairTabWidget QComboBox{\n"
"color:#000000;\n"
"background-color:#dcdcdd;\n"
"border:1px solid rgba(166,164,164,1);\n"
"border-radius:5px;\n"
"padding:5px 10px;\n"
"}\n"
"\n"
"#sentForRepairTabWidget QLineEdit:hover,#sentForRepairTabWidget QComboBox:hover{\n"
"\n"
"border:1px solid red;\n"
"\n"
"}\n"
"\n"
"#sentForRepairTabWidget QLineEdit:focus,#sentForRepairTabWidget QComboBox:focus{\n"
"\n"
"border:1px solid red;\n"
"\n"
"}\n"
"\n"
"#sentForRepairButtons QPushButton{\n"
"padding:10px;\n"
"}\n"
" #addSentForRepairBtn:hover{\n"
"background-color:#0eab1b;\n"
"}\n"
"#addSentForRepairBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#0c8724;\n"
"}\n"
"#updateSentForRepairBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#d49348;\n"
"}\n"
"#updateSentForRepairBtn:hover{\n"
"backgroun"
                        "d-color:#ad610a;\n"
"}\n"
"#clearSentForRepairBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color:#148cc2;\n"
"}\n"
"#clearSentForRepairBtn:hover{\n"
"background-color:#1cabeb;\n"
"}\n"
"\n"
"\n"
"#ssrBtn,#ssuBtn,#repairSearchBtn{\n"
"padding:10px;\n"
"color:#d49348;\n"
"background-color:#003854;\n"
"border:1px solid #003854;\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"\n"
"}\n"
"#ssrBtn:hover,#ssuBtn:hover,#repairSearchBtn:hover{\n"
"background-color:#d49348;\n"
"border-color:#003854;\n"
"color:#003854;\n"
"\n"
"}\n"
"\n"
"#sentForRepairTabWidget QTableWidget{\n"
"color:#003854;\n"
"background-color:#eaeaeb;\n"
"border:1px solid #4e5f8b;\n"
"border-radius:3px;\n"
"}\n"
"#sentForRepairTabWidget QHeaderView::section{\n"
"background: #003854;\n"
"border:1px solid qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(54,90,108,1) stop:1 rgba(54,90,108,1));\n"
"color:#fff;\n"
"font-weight:bold;\n"
"\n"
"}\n"
"\n"
"#repairsGenerateCSVBtn{\n"
"border:1px solid #003854;\n"
"border-r"
                        "adius:2px;\n"
"padding:5px;\n"
"color:#003854;\n"
"\n"
"}\n"
"#repairsGenerateCSVBtn:hover{\n"
"background-color:#003854;\n"
"color:#fff;\n"
"}\n"
"\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.sentForRepairPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_11 = QLabel(self.sentForRepairPage)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color:#003854;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_11)

        self.widget_17 = QWidget(self.sentForRepairPage)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_32 = QVBoxLayout(self.widget_17)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.sentForRepairTabWidget = QWidget(self.widget_17)
        self.sentForRepairTabWidget.setObjectName(u"sentForRepairTabWidget")
        self.sentForRepairTabWidget.setStyleSheet(u"#sendRepairtoServerGroupBox QGroupBox{\n"
"color:#003854;\n"
"border:1px dashed #003854;\n"
"}\n"
" #sendRepairtoUserGroupBox QGroupBox{\n"
"color:#003854;\n"
"border:1px dotted #003854;\n"
"}")
        self.verticalLayout_33 = QVBoxLayout(self.sentForRepairTabWidget)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.widget_21 = QWidget(self.sentForRepairTabWidget)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.widget_23 = QWidget(self.widget_21)
        self.widget_23.setObjectName(u"widget_23")
        self.verticalLayout_35 = QVBoxLayout(self.widget_23)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.txtSentForRepairSerial = QLineEdit(self.widget_23)
        self.txtSentForRepairSerial.setObjectName(u"txtSentForRepairSerial")

        self.verticalLayout_35.addWidget(self.txtSentForRepairSerial)

        self.txtSentForRepairModel = QLineEdit(self.widget_23)
        self.txtSentForRepairModel.setObjectName(u"txtSentForRepairModel")

        self.verticalLayout_35.addWidget(self.txtSentForRepairModel)

        self.txtSentForRepairLastUser = QLineEdit(self.widget_23)
        self.txtSentForRepairLastUser.setObjectName(u"txtSentForRepairLastUser")
        self.txtSentForRepairLastUser.setContextMenuPolicy(Qt.NoContextMenu)
        self.txtSentForRepairLastUser.setCursorMoveStyle(Qt.LogicalMoveStyle)

        self.verticalLayout_35.addWidget(self.txtSentForRepairLastUser)

        self.txtSentForRepairStatus = QComboBox(self.widget_23)
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.addItem("")
        self.txtSentForRepairStatus.setObjectName(u"txtSentForRepairStatus")
        self.txtSentForRepairStatus.setStyleSheet(u"color:#003854;")

        self.verticalLayout_35.addWidget(self.txtSentForRepairStatus)

        self.sentForRepairButtons = QWidget(self.widget_23)
        self.sentForRepairButtons.setObjectName(u"sentForRepairButtons")
        self.horizontalLayout_24 = QHBoxLayout(self.sentForRepairButtons)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.addSentForRepairBtn = QPushButton(self.sentForRepairButtons)
        self.addSentForRepairBtn.setObjectName(u"addSentForRepairBtn")
        self.addSentForRepairBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.addSentForRepairBtn.setIcon(icon21)

        self.horizontalLayout_24.addWidget(self.addSentForRepairBtn)

        self.updateSentForRepairBtn = QPushButton(self.sentForRepairButtons)
        self.updateSentForRepairBtn.setObjectName(u"updateSentForRepairBtn")
        self.updateSentForRepairBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.updateSentForRepairBtn.setIcon(icon20)

        self.horizontalLayout_24.addWidget(self.updateSentForRepairBtn)

        self.clearSentForRepairBtn = QPushButton(self.sentForRepairButtons)
        self.clearSentForRepairBtn.setObjectName(u"clearSentForRepairBtn")
        self.clearSentForRepairBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.clearSentForRepairBtn.setIcon(icon22)

        self.horizontalLayout_24.addWidget(self.clearSentForRepairBtn)


        self.verticalLayout_35.addWidget(self.sentForRepairButtons)


        self.horizontalLayout_23.addWidget(self.widget_23)

        self.sendRepairtoServerGroupBox = QWidget(self.widget_21)
        self.sendRepairtoServerGroupBox.setObjectName(u"sendRepairtoServerGroupBox")
        self.verticalLayout_37 = QVBoxLayout(self.sendRepairtoServerGroupBox)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.groupBox = QGroupBox(self.sendRepairtoServerGroupBox)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_38 = QVBoxLayout(self.groupBox)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.txtSSRSerial = QLineEdit(self.groupBox)
        self.txtSSRSerial.setObjectName(u"txtSSRSerial")
        self.txtSSRSerial.setEnabled(False)
        self.txtSSRSerial.setStyleSheet(u"border:none;")

        self.verticalLayout_38.addWidget(self.txtSSRSerial)

        self.txtSSRStatus = QComboBox(self.groupBox)
        self.txtSSRStatus.addItem("")
        self.txtSSRStatus.addItem("")
        self.txtSSRStatus.addItem("")
        self.txtSSRStatus.addItem("")
        self.txtSSRStatus.setObjectName(u"txtSSRStatus")
        self.txtSSRStatus.setStyleSheet(u"border:none;\n"
"color:#404d6f;")

        self.verticalLayout_38.addWidget(self.txtSSRStatus)

        self.ssrBtn = QPushButton(self.groupBox)
        self.ssrBtn.setObjectName(u"ssrBtn")
        self.ssrBtn.setFont(font1)
        self.ssrBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ssrBtn.setStyleSheet(u"")
        self.ssrBtn.setIcon(icon2)

        self.verticalLayout_38.addWidget(self.ssrBtn)


        self.verticalLayout_37.addWidget(self.groupBox)


        self.horizontalLayout_23.addWidget(self.sendRepairtoServerGroupBox)

        self.sendRepairtoUserGroupBox = QWidget(self.widget_21)
        self.sendRepairtoUserGroupBox.setObjectName(u"sendRepairtoUserGroupBox")
        self.verticalLayout_36 = QVBoxLayout(self.sendRepairtoUserGroupBox)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.groupbox2 = QGroupBox(self.sendRepairtoUserGroupBox)
        self.groupbox2.setObjectName(u"groupbox2")
        self.groupbox2.setFont(font1)
        self.groupbox2.setStyleSheet(u"")
        self.verticalLayout_46 = QVBoxLayout(self.groupbox2)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.txtSSUSerial = QLineEdit(self.groupbox2)
        self.txtSSUSerial.setObjectName(u"txtSSUSerial")
        self.txtSSUSerial.setEnabled(False)
        self.txtSSUSerial.setStyleSheet(u"border:none;")

        self.verticalLayout_46.addWidget(self.txtSSUSerial)

        self.txtSSUSpare = QLineEdit(self.groupbox2)
        self.txtSSUSpare.setObjectName(u"txtSSUSpare")
        self.txtSSUSpare.setEnabled(False)

        self.verticalLayout_46.addWidget(self.txtSSUSpare)

        self.ssuBtn = QPushButton(self.groupbox2)
        self.ssuBtn.setObjectName(u"ssuBtn")
        self.ssuBtn.setFont(font1)
        self.ssuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ssuBtn.setStyleSheet(u"")
        icon24 = QIcon()
        icon24.addFile(u":/Icons/Icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ssuBtn.setIcon(icon24)

        self.verticalLayout_46.addWidget(self.ssuBtn)


        self.verticalLayout_36.addWidget(self.groupbox2)


        self.horizontalLayout_23.addWidget(self.sendRepairtoUserGroupBox)


        self.verticalLayout_33.addWidget(self.widget_21)

        self.widget_22 = QWidget(self.sentForRepairTabWidget)
        self.widget_22.setObjectName(u"widget_22")
        self.verticalLayout_34 = QVBoxLayout(self.widget_22)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.widget_20 = QWidget(self.widget_22)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_24 = QWidget(self.widget_20)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setEnabled(False)
        self.txtRepairLaptopID = QLineEdit(self.widget_24)
        self.txtRepairLaptopID.setObjectName(u"txtRepairLaptopID")
        self.txtRepairLaptopID.setEnabled(False)
        self.txtRepairLaptopID.setGeometry(QRect(9, 10, 128, 28))
        self.txtRepairLaptopID.setStyleSheet(u"background:transparent;\n"
"border:none;\n"
"color:transparent;")
        self.txtRepairLaptopID.setEchoMode(QLineEdit.NoEcho)
        self.txtRepairLaptopID.setReadOnly(True)

        self.horizontalLayout_25.addWidget(self.widget_24)

        self.widget_26 = QWidget(self.widget_20)
        self.widget_26.setObjectName(u"widget_26")
        self.verticalLayout_44 = QVBoxLayout(self.widget_26)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.repairsGenerateCSVBtn = QPushButton(self.widget_26)
        self.repairsGenerateCSVBtn.setObjectName(u"repairsGenerateCSVBtn")
        self.repairsGenerateCSVBtn.setFont(font1)
        self.repairsGenerateCSVBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.repairsGenerateCSVBtn.setIcon(icon19)

        self.verticalLayout_44.addWidget(self.repairsGenerateCSVBtn)


        self.horizontalLayout_25.addWidget(self.widget_26, 0, Qt.AlignHCenter)

        self.widget_27 = QWidget(self.widget_20)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_26 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")

        self.horizontalLayout_25.addWidget(self.widget_27, 0, Qt.AlignVCenter)

        self.widget_28 = QWidget(self.widget_20)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMinimumSize(QSize(0, 42))
        self.horizontalLayout_27 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.txtSearchRepairs = QLineEdit(self.widget_28)
        self.txtSearchRepairs.setObjectName(u"txtSearchRepairs")
        sizePolicy4.setHeightForWidth(self.txtSearchRepairs.sizePolicy().hasHeightForWidth())
        self.txtSearchRepairs.setSizePolicy(sizePolicy4)
        self.txtSearchRepairs.setMinimumSize(QSize(170, 0))
        self.txtSearchRepairs.setMaximumSize(QSize(170, 16777215))
        self.txtSearchRepairs.setFont(font6)
        self.txtSearchRepairs.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.txtSearchRepairs.setEchoMode(QLineEdit.Normal)
        self.txtSearchRepairs.setAlignment(Qt.AlignCenter)
        self.txtSearchRepairs.setClearButtonEnabled(True)

        self.horizontalLayout_27.addWidget(self.txtSearchRepairs, 0, Qt.AlignRight)

        self.repairLaptopSearchCombo = QComboBox(self.widget_28)
        self.repairLaptopSearchCombo.addItem("")
        self.repairLaptopSearchCombo.addItem("")
        self.repairLaptopSearchCombo.addItem("")
        self.repairLaptopSearchCombo.setObjectName(u"repairLaptopSearchCombo")
        sizePolicy4.setHeightForWidth(self.repairLaptopSearchCombo.sizePolicy().hasHeightForWidth())
        self.repairLaptopSearchCombo.setSizePolicy(sizePolicy4)
        self.repairLaptopSearchCombo.setMinimumSize(QSize(170, 0))
        self.repairLaptopSearchCombo.setMaximumSize(QSize(170, 16777215))
        self.repairLaptopSearchCombo.setFont(font6)
        self.repairLaptopSearchCombo.setStyleSheet(u"color: #404d6f;")
        self.repairLaptopSearchCombo.setEditable(False)

        self.horizontalLayout_27.addWidget(self.repairLaptopSearchCombo, 0, Qt.AlignRight)


        self.horizontalLayout_25.addWidget(self.widget_28, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_34.addWidget(self.widget_20)

        self.RepairsRecordTable = QTableWidget(self.widget_22)
        if (self.RepairsRecordTable.columnCount() < 10):
            self.RepairsRecordTable.setColumnCount(10)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(7, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(8, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.RepairsRecordTable.setHorizontalHeaderItem(9, __qtablewidgetitem52)
        self.RepairsRecordTable.setObjectName(u"RepairsRecordTable")
        sizePolicy5.setHeightForWidth(self.RepairsRecordTable.sizePolicy().hasHeightForWidth())
        self.RepairsRecordTable.setSizePolicy(sizePolicy5)
        self.RepairsRecordTable.setMinimumSize(QSize(861, 334))
        self.RepairsRecordTable.setEditTriggers(QAbstractItemView.AnyKeyPressed)
        self.RepairsRecordTable.setShowGrid(True)
        self.RepairsRecordTable.setSortingEnabled(False)
        self.RepairsRecordTable.horizontalHeader().setCascadingSectionResizes(False)
        self.RepairsRecordTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.RepairsRecordTable.horizontalHeader().setStretchLastSection(True)
        self.RepairsRecordTable.verticalHeader().setCascadingSectionResizes(False)
        self.RepairsRecordTable.verticalHeader().setMinimumSectionSize(24)
        self.RepairsRecordTable.verticalHeader().setProperty("showSortIndicator", False)
        self.RepairsRecordTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_34.addWidget(self.RepairsRecordTable)


        self.verticalLayout_33.addWidget(self.widget_22)


        self.verticalLayout_32.addWidget(self.sentForRepairTabWidget)


        self.verticalLayout_16.addWidget(self.widget_17)

        self.mainPages.addWidget(self.sentForRepairPage)

        self.verticalLayout_15.addWidget(self.mainPages)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(300, 0))
        self.rightMenuContainer.setMaximumSize(QSize(230, 777))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.rightMenuSubContainer.setMinimumSize(QSize(300, 0))
        self.verticalLayout_12 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.closeRightMenuBtn = QPushButton(self.frame_8)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        self.closeRightMenuBtn.setIcon(icon9)
        self.closeRightMenuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_8)

        self.rightMenuPages = QCustomStackedWidget(self.rightMenuSubContainer)
        self.rightMenuPages.setObjectName(u"rightMenuPages")
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.logoutBtn = QPushButton(self.profilePage)
        self.logoutBtn.setObjectName(u"logoutBtn")
        self.logoutBtn.setGeometry(QRect(100, 510, 131, 31))
        self.logoutBtn.setFont(font1)
        self.logoutBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.logoutBtn.setStyleSheet(u"\n"
"#logoutBtn{\n"
"border-radius:5px;\n"
"padding: 5px 10px;\n"
"background-color: #003854;\n"
"}\n"
" #logoutBtn:hover{\n"
"background-color:#eaeaeb;\n"
"border:1px solid #003854;\n"
"color:#003854;\n"
"}\n"
"")
        icon25 = QIcon()
        icon25.addFile(u":/Icons/Icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logoutBtn.setIcon(icon25)
        self.frame_11 = QFrame(self.profilePage)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(15, 136, 251, 351))
        self.frame_11.setStyleSheet(u"#frame_11{\n"
"border-top:1px solid #979797;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_29 = QWidget(self.frame_11)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_28 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_22 = QLabel(self.widget_29)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.horizontalLayout_28.addWidget(self.label_22)

        self.sessionUser = QLabel(self.widget_29)
        self.sessionUser.setObjectName(u"sessionUser")
        self.sessionUser.setFont(font1)

        self.horizontalLayout_28.addWidget(self.sessionUser)


        self.verticalLayout_13.addWidget(self.widget_29)

        self.widget_30 = QWidget(self.frame_11)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_29 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_24 = QLabel(self.widget_30)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.horizontalLayout_29.addWidget(self.label_24)

        self.sessionID = QLabel(self.widget_30)
        self.sessionID.setObjectName(u"sessionID")
        self.sessionID.setFont(font1)

        self.horizontalLayout_29.addWidget(self.sessionID)


        self.verticalLayout_13.addWidget(self.widget_30)

        self.widget_31 = QWidget(self.frame_11)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_26 = QLabel(self.widget_31)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.horizontalLayout_30.addWidget(self.label_26)

        self.sessionUsername = QLabel(self.widget_31)
        self.sessionUsername.setObjectName(u"sessionUsername")
        self.sessionUsername.setFont(font1)

        self.horizontalLayout_30.addWidget(self.sessionUsername)


        self.verticalLayout_13.addWidget(self.widget_31)

        self.widget_35 = QWidget(self.frame_11)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_34 = QLabel(self.widget_35)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font1)

        self.horizontalLayout_34.addWidget(self.label_34)

        self.sessionEmail = QLabel(self.widget_35)
        self.sessionEmail.setObjectName(u"sessionEmail")
        self.sessionEmail.setFont(font1)

        self.horizontalLayout_34.addWidget(self.sessionEmail)


        self.verticalLayout_13.addWidget(self.widget_35)

        self.widget_36 = QWidget(self.frame_11)
        self.widget_36.setObjectName(u"widget_36")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_36 = QLabel(self.widget_36)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font1)

        self.horizontalLayout_35.addWidget(self.label_36)

        self.sessionStatus = QLabel(self.widget_36)
        self.sessionStatus.setObjectName(u"sessionStatus")
        self.sessionStatus.setFont(font1)

        self.horizontalLayout_35.addWidget(self.sessionStatus)


        self.verticalLayout_13.addWidget(self.widget_36)

        self.label_2 = QLabel(self.profilePage)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 30, 91, 81))
        self.label_2.setMinimumSize(QSize(50, 50))
        self.label_2.setSizeIncrement(QSize(50, 50))
        self.label_2.setStyleSheet(u"")
        self.label_2.setPixmap(QPixmap(u":/Icons/Icons/people.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.rightMenuPages.addWidget(self.profilePage)
        self.moreMenuPage = QWidget()
        self.moreMenuPage.setObjectName(u"moreMenuPage")
        self.verticalLayout_14 = QVBoxLayout(self.moreMenuPage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_7 = QLabel(self.moreMenuPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_7)

        self.rightMenuPages.addWidget(self.moreMenuPage)

        self.verticalLayout_12.addWidget(self.rightMenuPages)


        self.verticalLayout_11.addWidget(self.rightMenuSubContainer)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer)


        self.verticalLayout_10.addWidget(self.mainBodyContent)

        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        self.popupNotificationContainer.setObjectName(u"popupNotificationContainer")
        self.verticalLayout_20 = QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.popupNotificationSubContainer = QWidget(self.popupNotificationContainer)
        self.popupNotificationSubContainer.setObjectName(u"popupNotificationSubContainer")
        self.verticalLayout_21 = QVBoxLayout(self.popupNotificationSubContainer)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_13 = QLabel(self.popupNotificationSubContainer)
        self.label_13.setObjectName(u"label_13")
        font9 = QFont()
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setWeight(75)
        self.label_13.setFont(font9)

        self.verticalLayout_21.addWidget(self.label_13)

        self.frame_9 = QFrame(self.popupNotificationSubContainer)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.notificationMsg = QLabel(self.frame_9)
        self.notificationMsg.setObjectName(u"notificationMsg")
        sizePolicy1.setHeightForWidth(self.notificationMsg.sizePolicy().hasHeightForWidth())
        self.notificationMsg.setSizePolicy(sizePolicy1)
        font10 = QFont()
        font10.setPointSize(9)
        font10.setBold(False)
        font10.setWeight(50)
        self.notificationMsg.setFont(font10)
        self.notificationMsg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.notificationMsg)

        self.closeNotificationBtn = QPushButton(self.frame_9)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        self.closeNotificationBtn.setIcon(icon9)
        self.closeNotificationBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.closeNotificationBtn, 0, Qt.AlignRight)


        self.verticalLayout_21.addWidget(self.frame_9)


        self.verticalLayout_20.addWidget(self.popupNotificationSubContainer)


        self.verticalLayout_10.addWidget(self.popupNotificationContainer)

        self.footerContainer = QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName(u"footerContainer")
        self.horizontalLayout_11 = QHBoxLayout(self.footerContainer)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.footerContainer)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.copyrightArea = QLabel(self.frame_10)
        self.copyrightArea.setObjectName(u"copyrightArea")
        self.copyrightArea.setFont(font1)

        self.horizontalLayout_12.addWidget(self.copyrightArea)


        self.horizontalLayout_11.addWidget(self.frame_10)

        self.connectionLabel = QLabel(self.footerContainer)
        self.connectionLabel.setObjectName(u"connectionLabel")

        self.horizontalLayout_11.addWidget(self.connectionLabel, 0, Qt.AlignRight)

        self.sizeGrip = QFrame(self.footerContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.sizeGrip)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.sizeGrip)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(18, 18))
        self.label_15.setMaximumSize(QSize(18, 18))
        self.label_15.setCursor(QCursor(Qt.SizeBDiagCursor))
        self.label_15.setLayoutDirection(Qt.RightToLeft)
        self.label_15.setPixmap(QPixmap(u":/Icons/Icons/maximize-2.svg"))
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_15)


        self.horizontalLayout_11.addWidget(self.sizeGrip, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.footerContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerMenuPages.setCurrentIndex(0)
        self.mainPages.setCurrentIndex(0)
        self.serverRoomTabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.serverInvBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Server Inventory", None))
#endif // QT_CONFIG(tooltip)
        self.serverInvBtn.setText(QCoreApplication.translate("MainWindow", u"Server Inventory", None))
#if QT_CONFIG(tooltip)
        self.inUseInvBtn.setToolTip(QCoreApplication.translate("MainWindow", u"In-Use Inventory", None))
#endif // QT_CONFIG(tooltip)
        self.inUseInvBtn.setText(QCoreApplication.translate("MainWindow", u"In-Use Inventory", None))
#if QT_CONFIG(tooltip)
        self.sentForRepairBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Sent for Repairs", None))
#endif // QT_CONFIG(tooltip)
        self.sentForRepairBtn.setText(QCoreApplication.translate("MainWindow", u"Sent for Repairs", None))
#if QT_CONFIG(tooltip)
        self.adminDashBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Admin Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.adminDashBtn.setText(QCoreApplication.translate("MainWindow", u"Admin Dashboard", None))
#if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.informationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.informationBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Help Menu", None))
#endif // QT_CONFIG(tooltip)
        self.helpMenuBtn.setText(QCoreApplication.translate("MainWindow", u"Help Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
#if QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeCenterMenuBtn.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Admin ID:", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Firstname:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Lastname:", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.adminProfileSettingBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Settings", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"New Password:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Re-Enter New Pass:", None))
        self.adminChangePasswordBtn.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">This Application</span> is a standalone inventory management application developed by <span style=\" font-weight:600; color:#dfc816;\">Nayan Bastola as a project for Yamaha Motor Canada</span><span style=\" color:#dfc816;\">.</span> The application utilizes MYSQL Server Management as its backend database, providing a reliable and robust platform for storing and managing inventory data. </p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-ri"
                        "ght:0px; -qt-block-indent:0; text-indent:0px;\">The application is designed exclusively for the <span style=\" font-weight:600;\">IT SERVICE DESK </span>and includes several key features. The main dashboard is divided into four main categories: <span style=\" font-style:italic;\">Server Inventory, In-Use Inventory, Repair Inventory, and Admin Dashboard.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dfc816;\">The Server Inventory: </span>category consists of two sub-categories: Laptop Records and Equipment Records. Each laptop record is assigned a unique serial number, and CRUD functions are provided to create, update, and delete laptop and equipment data as required. Equipment records provide a count of the available equipment in the inventory.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-i"
                        "ndent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dfc816;\">The In-Use Inventory:</span> category is dedicated to Laptops and Equipment assigned to individual users in the company. Each user is assigned a laptop and one or more equipment items for office and home use. CRUD operations are available to update and manage the data in this category, but deletion is not permitted. If a laptop needs to be returned to the inventory, or equipment needs to be restocked, the user's record must be updated accordingly.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dfc816;\">The Repair Inventory:</span> category is designed to keep track of laptops that are sent for repairs. This allows the IT department to keep track of which laptops are awaiting repairs, and to make note of the total inventory in the department.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px;"
                        " margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#dfc816;\">The Admin Dashboard</span> category provides administrators with the ability to view and manage user accounts. Admins can add or delete current admins who are using the application, ensuring that access to the application is secure and limited to authorized users.</p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic; color:#dfc816;\">Additional features of the application include a search function, which allows users to search for specific data within the inventory, the ability to generate Excel files, and the ability to change admin passwords.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Overall, this application is a powerful and u"
                        "ser-friendly inventory management system designed to meet the needs of the IT service desk. With its reliable <span style=\" font-weight:600; font-style:italic; text-decoration: underline; color:#dfc816;\">MYSQL Server Management backend</span> and intuitive user interface, the application provides a comprehensive solution for managing inventory data and streamlining inventory management processes.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help Menu", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Contact Nayan for Further Info.", None))
        self.label_5.setText("")
#if QT_CONFIG(tooltip)
        self.notificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.notificationBtn.setText("")
#if QT_CONFIG(tooltip)
        self.moreMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"More", None))
#endif // QT_CONFIG(tooltip)
        self.moreMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.profileMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profileMenuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeWindowsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize Window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeWindowsBtn.setText("")
#if QT_CONFIG(tooltip)
        self.restoreWindowsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Restore Window", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.closeWindowsBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Window", None))
#endif // QT_CONFIG(tooltip)
        self.closeWindowsBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dashboard Home", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Server Room Inventory", None))
        self.serverRoomDashCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"In-Use Inventory", None))
        self.inuseRoomDashCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Equipments", None))
        self.equipRoomCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Sent for Repairs", None))
        self.repairsRoomDashCount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_72.setText("")
        self.serverInvLabel.setText(QCoreApplication.translate("MainWindow", u"Server Inventory", None))
        self.txtLaptopSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial Number", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.txtModelNumber.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Model Number", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.txtLastUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Used By", None))
        self.txtComboStatus.setItemText(0, "")
        self.txtComboStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"New", None))
        self.txtComboStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"Spare", None))
        self.txtComboStatus.setItemText(3, QCoreApplication.translate("MainWindow", u"Reset", None))
        self.txtComboStatus.setItemText(4, QCoreApplication.translate("MainWindow", u"Re-Imaged", None))
        self.txtComboStatus.setItemText(5, QCoreApplication.translate("MainWindow", u"Stocked", None))
        self.txtComboStatus.setItemText(6, QCoreApplication.translate("MainWindow", u"Damaged", None))

        self.label_40.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.addLaptopBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateLaptopBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.deleteLaptopBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.serverRoomGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Send for Repairs", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.sendforrepairStatus.setItemText(0, "")
        self.sendforrepairStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Damaged Screen", None))
        self.sendforrepairStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"Damaged Keyboard", None))
        self.sendforrepairStatus.setItemText(3, QCoreApplication.translate("MainWindow", u"Damaged Charging Port", None))
        self.sendforrepairStatus.setItemText(4, QCoreApplication.translate("MainWindow", u"Internal Damaged", None))
        self.sendforrepairStatus.setItemText(5, QCoreApplication.translate("MainWindow", u"Others", None))

        self.sendToRepairBtn.setText(QCoreApplication.translate("MainWindow", u"Send For Repairs", None))
        self.laptopRecordGenerateExcelBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Excel Report", None))
        self.txtLapInvSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ...", None))
        self.txtLapInvSearchCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Serial (A-Z)", None))
        self.txtLapInvSearchCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Model (A-Z)", None))
        self.txtLapInvSearchCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Last User (A-Z)", None))

        self.txtLapInvSearchCombo.setCurrentText(QCoreApplication.translate("MainWindow", u"Serial (A-Z)", None))
        ___qtablewidgetitem = self.laptopRecordsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.laptopRecordsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None));
        ___qtablewidgetitem2 = self.laptopRecordsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Model Number", None));
        ___qtablewidgetitem3 = self.laptopRecordsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Last User", None));
        ___qtablewidgetitem4 = self.laptopRecordsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem5 = self.laptopRecordsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Updated By", None));
        ___qtablewidgetitem6 = self.laptopRecordsTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Change Date", None));
        self.serverRoomTabWidget.setTabText(self.serverRoomTabWidget.indexOf(self.laptopTabPane), QCoreApplication.translate("MainWindow", u"Laptop Records", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Keyboard", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Mouse ", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Headphones ", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Monitors", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Dock Station", None))
#if QT_CONFIG(tooltip)
        self.updateEquipBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Update Records", None))
#endif // QT_CONFIG(tooltip)
        self.updateEquipBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"* Single Item Update at a Time *", None))
        self.extraGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Extras", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Specify Others", None))
        self.equipOtherItemCombo.setItemText(0, "")
        self.equipOtherItemCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"HDMI Cable", None))
        self.equipOtherItemCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"DP Cable", None))
        self.equipOtherItemCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"VGA Cable", None))
        self.equipOtherItemCombo.setItemText(4, QCoreApplication.translate("MainWindow", u"DVI Cable", None))
        self.equipOtherItemCombo.setItemText(5, QCoreApplication.translate("MainWindow", u"Ethernet Cable", None))
        self.equipOtherItemCombo.setItemText(6, QCoreApplication.translate("MainWindow", u"USB Cables", None))
        self.equipOtherItemCombo.setItemText(7, QCoreApplication.translate("MainWindow", u"PS/2 Cable", None))
        self.equipOtherItemCombo.setItemText(8, QCoreApplication.translate("MainWindow", u"RCA Connectors", None))
        self.equipOtherItemCombo.setItemText(9, QCoreApplication.translate("MainWindow", u"Phone RJ11 Cable", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"No. of Items", None))
        self.addExtraEquipBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateExtraEquipBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.deleteExtraEquipBtn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.equipRecordGenerateExcelBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Excel Report", None))
        ___qtablewidgetitem7 = self.equipRecordTable.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Sl. No", None));
        ___qtablewidgetitem8 = self.equipRecordTable.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        ___qtablewidgetitem9 = self.equipRecordTable.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Count", None));
        ___qtablewidgetitem10 = self.equipRecordTable.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Updated By", None));
        ___qtablewidgetitem11 = self.equipRecordTable.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Change Date", None));
        self.serverRoomTabWidget.setTabText(self.serverRoomTabWidget.indexOf(self.equipmentTabPane), QCoreApplication.translate("MainWindow", u"Equipment Records", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"In-Use Inventory", None))
        self.InuseInvGroupBox1.setTitle(QCoreApplication.translate("MainWindow", u"Current Users", None))
#if QT_CONFIG(tooltip)
        self.txtInuseLaptopSerial.setToolTip(QCoreApplication.translate("MainWindow", u"Laptop Model", None))
#endif // QT_CONFIG(tooltip)
        self.txtInuseLaptopSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(tooltip)
        self.txtInuseLaptopModel.setToolTip(QCoreApplication.translate("MainWindow", u"Laptop Serial", None))
#endif // QT_CONFIG(tooltip)
        self.txtInuseLaptopModel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Model Number", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(tooltip)
        self.txtInuseUser.setToolTip(QCoreApplication.translate("MainWindow", u"Laptop User", None))
#endif // QT_CONFIG(tooltip)
        self.txtInuseUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop User", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"*", None))
#if QT_CONFIG(tooltip)
        self.txtInuseLaptopStatus.setToolTip(QCoreApplication.translate("MainWindow", u"Current Status", None))
#endif // QT_CONFIG(tooltip)
        self.txtInuseLaptopStatus.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Current Status", None))
        self.InuseInvGroupBoxOfficeEquip.setTitle(QCoreApplication.translate("MainWindow", u"In-Office Equipments Supply", None))
        self.officeKeyboardRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Keyboard", None))
        self.officeKeyboardRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Keyboard", None))
        self.officeMouseRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Mouse", None))
        self.officeMouseRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Mouse", None))
        self.officeHeadphoneRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Headphone", None))
        self.officeHeadphoneRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Headphone", None))
        self.officeDockRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Dock", None))
        self.officeDockRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Dock", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.officeMonitorRadioNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.officeMonitorRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Extras", None))
        self.InuseInvGroupBoxHomeEquip.setTitle(QCoreApplication.translate("MainWindow", u"Home Equipments Supply", None))
        self.homeKeyboardRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Keyboard", None))
        self.homeKeyboardRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Keyboard", None))
        self.homeMouseRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Mouse", None))
        self.homeMouseRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Mouse", None))
        self.homeHeadphoneRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Headphone", None))
        self.homeHeadphoneRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Headphone", None))
        self.homeDockRadioNew.setText(QCoreApplication.translate("MainWindow", u"New Dock", None))
        self.homeDockRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked Dock", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Monitor", None))
        self.homeMonitorRadioNew.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.homeMonitorRadioStocked.setText(QCoreApplication.translate("MainWindow", u"Stocked", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Extras", None))
        self.offboardingGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Offboarding Request", None))
        self.offboardingLaptopSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial", None))
        self.offboardingBtn.setText(QCoreApplication.translate("MainWindow", u"Offboarding", None))
        self.sendRepairGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Send for Repairs", None))
        self.sendForRepairLaptopSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial", None))
        self.refreshSpareLaptop.setText("")
        self.sendForRepairBtn.setText(QCoreApplication.translate("MainWindow", u"Send for Repairs", None))
        self.addInuseInvBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateInuseInvBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.clearInuseInvBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.inuseInvGenerateExcelBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Excel", None))
        self.InuseLaptoSerialID.setText("")
        self.InUseRecordSearchTxt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ...", None))
        self.InUseRecordSearchCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Serial (A-Z)", None))
        self.InUseRecordSearchCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Model (A-Z)", None))
        self.InUseRecordSearchCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Last User (A-Z)", None))

        self.InUseRecordSearchCombo.setCurrentText(QCoreApplication.translate("MainWindow", u"Serial (A-Z)", None))
        ___qtablewidgetitem12 = self.InUseTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Sl.No", None));
        ___qtablewidgetitem13 = self.InUseTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"User", None));
        ___qtablewidgetitem14 = self.InUseTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Laptop Serial", None));
        ___qtablewidgetitem15 = self.InUseTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Model Number", None));
        ___qtablewidgetitem16 = self.InUseTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Previous Laptop Serial", None));
        ___qtablewidgetitem17 = self.InUseTableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Current Status", None));
        ___qtablewidgetitem18 = self.InUseTableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Keyboard", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem18.setToolTip(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem18.setWhatsThis(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem19 = self.InUseTableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Keyboard", None));
        ___qtablewidgetitem20 = self.InUseTableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Mouse", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem20.setToolTip(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem20.setWhatsThis(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem21 = self.InUseTableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Mouse", None));
        ___qtablewidgetitem22 = self.InUseTableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Headphone", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem22.setToolTip(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem22.setWhatsThis(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem23 = self.InUseTableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Headphone", None));
        ___qtablewidgetitem24 = self.InUseTableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Monitor", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem24.setToolTip(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem24.setWhatsThis(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem25 = self.InUseTableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Monitor", None));
        ___qtablewidgetitem26 = self.InUseTableWidget.horizontalHeaderItem(15)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Dock", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem26.setToolTip(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem26.setWhatsThis(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem27 = self.InUseTableWidget.horizontalHeaderItem(16)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Dock", None));
        ___qtablewidgetitem28 = self.InUseTableWidget.horizontalHeaderItem(17)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Extras", None));
#if QT_CONFIG(tooltip)
        ___qtablewidgetitem28.setToolTip(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        ___qtablewidgetitem28.setWhatsThis(QCoreApplication.translate("MainWindow", u"Office Equip", None));
#endif // QT_CONFIG(whatsthis)
        ___qtablewidgetitem29 = self.InUseTableWidget.horizontalHeaderItem(18)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Extras", None));
        ___qtablewidgetitem30 = self.InUseTableWidget.horizontalHeaderItem(20)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Updated By", None));
        ___qtablewidgetitem31 = self.InUseTableWidget.horizontalHeaderItem(21)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Change Date", None));
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"ADMIN DASHBOARD", None))
        self.label_69.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Edit Admin Details", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Admin ID", None))
#if QT_CONFIG(tooltip)
        self.txtDashAdminID.setToolTip(QCoreApplication.translate("MainWindow", u"Admin ID", None))
#endif // QT_CONFIG(tooltip)
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Admin Status", None))
        self.txtDashAdminStatusCombo.setItemText(0, "")
        self.txtDashAdminStatusCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Active", None))
        self.txtDashAdminStatusCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"In-Active", None))

        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Admin Flag", None))
        self.txtDashAdminFlagCombo.setItemText(0, "")
        self.txtDashAdminFlagCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Super Admin", None))
        self.txtDashAdminFlagCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Main Admin", None))
        self.txtDashAdminFlagCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Admin", None))

#if QT_CONFIG(tooltip)
        self.editAdminInfoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Edit Admin Details", None))
#endif // QT_CONFIG(tooltip)
        self.editAdminInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Edit Admin Info", None))
        self.deleteAdminInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Delete Admin", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Register New Admin", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Admin Status", None))
        self.txtDashRegAdminStatusCombo.setItemText(0, "")
        self.txtDashRegAdminStatusCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Active", None))
        self.txtDashRegAdminStatusCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"In-Active", None))

        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Admin Flag", None))
        self.txtDashRegAdminFlagCombo.setItemText(0, "")
        self.txtDashRegAdminFlagCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Super Admin", None))
        self.txtDashRegAdminFlagCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Main Admin", None))
        self.txtDashRegAdminFlagCombo.setItemText(3, QCoreApplication.translate("MainWindow", u"Admin", None))

#if QT_CONFIG(tooltip)
        self.registerAdminInfoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Register Admin", None))
#endif // QT_CONFIG(tooltip)
        self.registerAdminInfoBtn.setText(QCoreApplication.translate("MainWindow", u"Register Admin", None))
        ___qtablewidgetitem32 = self.adminDashTable.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Admin ID", None));
        ___qtablewidgetitem33 = self.adminDashTable.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"First Name", None));
        ___qtablewidgetitem34 = self.adminDashTable.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Last Name", None));
        ___qtablewidgetitem35 = self.adminDashTable.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem36 = self.adminDashTable.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem37 = self.adminDashTable.horizontalHeaderItem(5)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem38 = self.adminDashTable.horizontalHeaderItem(6)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Flag", None));
        ___qtablewidgetitem39 = self.adminDashTable.horizontalHeaderItem(7)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Updated By", None));
        ___qtablewidgetitem40 = self.adminDashTable.horizontalHeaderItem(8)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Change Date", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"FOR REPAIRS", None))
        self.txtSentForRepairSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial Number *", None))
        self.txtSentForRepairModel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Model Number *", None))
        self.txtSentForRepairLastUser.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Last Used By", None))
        self.txtSentForRepairStatus.setItemText(0, "")
        self.txtSentForRepairStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Repair Screen", None))
        self.txtSentForRepairStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"Repair Keyboard", None))
        self.txtSentForRepairStatus.setItemText(3, QCoreApplication.translate("MainWindow", u"Repair Trackpad", None))
        self.txtSentForRepairStatus.setItemText(4, QCoreApplication.translate("MainWindow", u"Repair Charging Port", None))
        self.txtSentForRepairStatus.setItemText(5, "")
        self.txtSentForRepairStatus.setItemText(6, QCoreApplication.translate("MainWindow", u"Other Repairs", None))

        self.addSentForRepairBtn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.updateSentForRepairBtn.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.clearSentForRepairBtn.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Send to Server Room", None))
        self.txtSSRSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial", None))
        self.txtSSRStatus.setItemText(0, "")
        self.txtSSRStatus.setItemText(1, QCoreApplication.translate("MainWindow", u"Repair Success", None))
        self.txtSSRStatus.setItemText(2, QCoreApplication.translate("MainWindow", u"Faulty", None))
        self.txtSSRStatus.setItemText(3, QCoreApplication.translate("MainWindow", u"Damaged", None))

        self.ssrBtn.setText(QCoreApplication.translate("MainWindow", u" Send to Server Room", None))
        self.groupbox2.setTitle(QCoreApplication.translate("MainWindow", u"Send Back to User", None))
        self.txtSSUSerial.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Laptop Serial", None))
        self.txtSSUSpare.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Spare Provided", None))
        self.ssuBtn.setText(QCoreApplication.translate("MainWindow", u"Send to User", None))
        self.repairsGenerateCSVBtn.setText(QCoreApplication.translate("MainWindow", u"Generate Excel", None))
        self.txtSearchRepairs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search ...", None))
        self.repairLaptopSearchCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Serial (A-Z)", None))
        self.repairLaptopSearchCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Model (A-Z)", None))
        self.repairLaptopSearchCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"Last User (A-Z)", None))

        self.repairLaptopSearchCombo.setCurrentText(QCoreApplication.translate("MainWindow", u"Serial (A-Z)", None))
        ___qtablewidgetitem41 = self.RepairsRecordTable.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"No.", None));
        ___qtablewidgetitem42 = self.RepairsRecordTable.horizontalHeaderItem(1)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Serial Number", None));
        ___qtablewidgetitem43 = self.RepairsRecordTable.horizontalHeaderItem(2)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Model Number", None));
        ___qtablewidgetitem44 = self.RepairsRecordTable.horizontalHeaderItem(3)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Last User", None));
        ___qtablewidgetitem45 = self.RepairsRecordTable.horizontalHeaderItem(4)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Spare Provided", None));
        ___qtablewidgetitem46 = self.RepairsRecordTable.horizontalHeaderItem(5)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Spare Model No.", None));
        ___qtablewidgetitem47 = self.RepairsRecordTable.horizontalHeaderItem(6)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Source", None));
        ___qtablewidgetitem48 = self.RepairsRecordTable.horizontalHeaderItem(7)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem49 = self.RepairsRecordTable.horizontalHeaderItem(8)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Updated By", None));
        ___qtablewidgetitem50 = self.RepairsRecordTable.horizontalHeaderItem(9)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Change Date", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
#if QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Menu", None))
#endif // QT_CONFIG(tooltip)
        self.closeRightMenuBtn.setText("")
        self.logoutBtn.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Admin Name :", None))
        self.sessionUser.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Admin ID :", None))
        self.sessionID.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Username :", None))
        self.sessionUsername.setText("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.sessionEmail.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Status:", None))
        self.sessionStatus.setText("")
        self.label_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Notification", None))
        self.notificationMsg.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
#if QT_CONFIG(tooltip)
        self.closeNotificationBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close Notification", None))
#endif // QT_CONFIG(tooltip)
        self.closeNotificationBtn.setText("")
        self.copyrightArea.setText("")
        self.connectionLabel.setText("")
        self.label_15.setText("")
    # retranslateUi

