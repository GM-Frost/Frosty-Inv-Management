/********************************************************************************
** Form generated from reading UI file 'loginSxSwqU.ui'
**
** Created by: Qt User Interface Compiler version 5.11.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef LOGINSXSWQU_H
#define LOGINSXSWQU_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QFrame *frame;
    QVBoxLayout *verticalLayout_2;
    QWidget *widget;
    QWidget *widget_3;
    QLabel *label;
    QLabel *label_2;
    QLineEdit *loginUsername;
    QLineEdit *loginPassword;
    QPushButton *loginBtn;
    QLabel *label_3;
    QLabel *label_5;
    QLabel *label_4;
    QLabel *txtLoginError;
    QLabel *txtUserError;
    QLabel *txtPasswordError;
    QLabel *label_8;
    QWidget *headerLogin;
    QHBoxLayout *horizontalLayout;
    QFrame *frame_2;
    QHBoxLayout *horizontalLayout_2;
    QWidget *widget_2;
    QHBoxLayout *horizontalLayout_3;
    QLabel *label_9;
    QLabel *label_10;
    QFrame *frame_3;
    QVBoxLayout *verticalLayout_4;
    QSpacerItem *horizontalSpacer;
    QFrame *dialogBtn;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *minimizeWindowsBtn;
    QPushButton *restoreWindowsBtn;
    QPushButton *closeWindowsBtn;
    QLabel *txtDatabaseconnection;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QStringLiteral("Dialog"));
        Dialog->resize(841, 729);
        Dialog->setStyleSheet(QLatin1String("#dialogBtn QPushButton{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
""));
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        frame = new QFrame(Dialog);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setStyleSheet(QLatin1String("\n"
"background-color:#eaeced;\n"
"border-radius: 10px;\n"
""));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);
        widget = new QWidget(frame);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setMouseTracking(true);
        widget_3 = new QWidget(widget);
        widget_3->setObjectName(QStringLiteral("widget_3"));
        widget_3->setGeometry(QRect(400, 90, 391, 611));
        widget_3->setStyleSheet(QLatin1String("background-color:qlineargradient(spread:pad,  x1:0 y1:0, x2:1 y2:0, stop:0 rgba(78,95,139,1) stop:1 rgba(78,95,139,1));\n"
"border-radius:20px;"));
        label = new QLabel(widget_3);
        label->setObjectName(QStringLiteral("label"));
        label->setGeometry(QRect(70, 50, 51, 41));
        label->setStyleSheet(QStringLiteral("background:transparent;"));
        label->setPixmap(QPixmap(QString::fromUtf8(":/Icons/Icons/log-in.svg")));
        label->setScaledContents(true);
        label_2 = new QLabel(widget_3);
        label_2->setObjectName(QStringLiteral("label_2"));
        label_2->setGeometry(QRect(0, 40, 391, 61));
        QFont font;
        font.setPointSize(24);
        font.setBold(true);
        font.setWeight(75);
        label_2->setFont(font);
        label_2->setStyleSheet(QLatin1String("background-color:#404d6f;\n"
"color: white;\n"
"border-radius:5px;"));
        label_2->setAlignment(Qt::AlignCenter);
        loginUsername = new QLineEdit(widget_3);
        loginUsername->setObjectName(QStringLiteral("loginUsername"));
        loginUsername->setGeometry(QRect(50, 150, 301, 71));
        QFont font1;
        font1.setPointSize(10);
        font1.setItalic(true);
        loginUsername->setFont(font1);
        loginUsername->setStyleSheet(QLatin1String("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:#fff;\n"
"padding-bottom:7px;\n"
""));
        loginPassword = new QLineEdit(widget_3);
        loginPassword->setObjectName(QStringLiteral("loginPassword"));
        loginPassword->setGeometry(QRect(50, 240, 301, 71));
        loginPassword->setFont(font1);
        loginPassword->setStyleSheet(QLatin1String("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color:#fff;\n"
"padding-bottom:7px;\n"
""));
        loginBtn = new QPushButton(widget_3);
        loginBtn->setObjectName(QStringLiteral("loginBtn"));
        loginBtn->setGeometry(QRect(70, 380, 261, 51));
        QFont font2;
        font2.setFamily(QStringLiteral("Terminal"));
        font2.setPointSize(12);
        font2.setBold(false);
        font2.setItalic(false);
        font2.setUnderline(false);
        font2.setWeight(50);
        font2.setStrikeOut(false);
        font2.setKerning(true);
        loginBtn->setFont(font2);
        loginBtn->setCursor(QCursor(Qt::PointingHandCursor));
        loginBtn->setStyleSheet(QLatin1String("QPushButton#loginBtn{\n"
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
"}"));
        label_3 = new QLabel(widget_3);
        label_3->setObjectName(QStringLiteral("label_3"));
        label_3->setGeometry(QRect(70, 520, 261, 21));
        label_3->setStyleSheet(QStringLiteral("color: #fff;"));
        label_3->setAlignment(Qt::AlignCenter);
        label_5 = new QLabel(widget_3);
        label_5->setObjectName(QStringLiteral("label_5"));
        label_5->setGeometry(QRect(140, 550, 141, 20));
        QFont font3;
        font3.setPointSize(9);
        font3.setBold(true);
        font3.setItalic(true);
        font3.setUnderline(false);
        font3.setWeight(75);
        font3.setStrikeOut(false);
        label_5->setFont(font3);
        label_5->setStyleSheet(QLatin1String("color:#ed1c24;\n"
"\n"
"background:transparent;"));
        label_5->setAlignment(Qt::AlignCenter);
        label_4 = new QLabel(widget_3);
        label_4->setObjectName(QStringLiteral("label_4"));
        label_4->setGeometry(QRect(110, 550, 31, 31));
        label_4->setStyleSheet(QStringLiteral("background:transparent;"));
        label_4->setPixmap(QPixmap(QString::fromUtf8(":/Icons/Icons/phone-forwarded.svg")));
        txtLoginError = new QLabel(widget_3);
        txtLoginError->setObjectName(QStringLiteral("txtLoginError"));
        txtLoginError->setGeometry(QRect(40, 120, 311, 20));
        QFont font4;
        font4.setPointSize(9);
        font4.setBold(true);
        font4.setWeight(75);
        txtLoginError->setFont(font4);
        txtLoginError->setStyleSheet(QLatin1String("color: rgb(223, 0, 0);\n"
"background-color:transparent;"));
        txtLoginError->setAlignment(Qt::AlignCenter);
        txtUserError = new QLabel(widget_3);
        txtUserError->setObjectName(QStringLiteral("txtUserError"));
        txtUserError->setGeometry(QRect(350, 190, 21, 21));
        QFont font5;
        font5.setPointSize(10);
        font5.setBold(true);
        font5.setWeight(75);
        txtUserError->setFont(font5);
        txtUserError->setStyleSheet(QLatin1String("background-color:transparent;\n"
"color:red;"));
        txtUserError->setAlignment(Qt::AlignCenter);
        txtPasswordError = new QLabel(widget_3);
        txtPasswordError->setObjectName(QStringLiteral("txtPasswordError"));
        txtPasswordError->setGeometry(QRect(350, 280, 21, 21));
        txtPasswordError->setFont(font5);
        txtPasswordError->setStyleSheet(QLatin1String("#txtPasswordError{\n"
"color:red;\n"
"background-color:transparent;\n"
"}"));
        txtPasswordError->setAlignment(Qt::AlignCenter);
        label_2->raise();
        loginUsername->raise();
        loginPassword->raise();
        loginBtn->raise();
        label_3->raise();
        label_5->raise();
        label_4->raise();
        label->raise();
        txtLoginError->raise();
        txtUserError->raise();
        txtPasswordError->raise();
        label_8 = new QLabel(widget);
        label_8->setObjectName(QStringLiteral("label_8"));
        label_8->setGeometry(QRect(30, 280, 351, 141));
        label_8->setPixmap(QPixmap(QString::fromUtf8(":/Images/Images/Yamaha-WaterMark.png")));
        label_8->setScaledContents(true);
        headerLogin = new QWidget(widget);
        headerLogin->setObjectName(QStringLiteral("headerLogin"));
        headerLogin->setGeometry(QRect(0, 0, 821, 71));
        headerLogin->setStyleSheet(QStringLiteral("background-color:#404d6f;"));
        horizontalLayout = new QHBoxLayout(headerLogin);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        frame_2 = new QFrame(headerLogin);
        frame_2->setObjectName(QStringLiteral("frame_2"));
        frame_2->setStyleSheet(QStringLiteral(""));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(frame_2);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        widget_2 = new QWidget(frame_2);
        widget_2->setObjectName(QStringLiteral("widget_2"));
        horizontalLayout_3 = new QHBoxLayout(widget_2);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        label_9 = new QLabel(widget_2);
        label_9->setObjectName(QStringLiteral("label_9"));
        label_9->setMinimumSize(QSize(35, 35));
        label_9->setMaximumSize(QSize(35, 35));
        label_9->setPixmap(QPixmap(QString::fromUtf8(":/Images/Images/Yamaha-Logo.ico")));
        label_9->setScaledContents(true);

        horizontalLayout_3->addWidget(label_9);

        label_10 = new QLabel(widget_2);
        label_10->setObjectName(QStringLiteral("label_10"));
        QFont font6;
        font6.setPointSize(12);
        label_10->setFont(font6);
        label_10->setStyleSheet(QStringLiteral("color:red;"));
        label_10->setAlignment(Qt::AlignRight|Qt::AlignTrailing|Qt::AlignVCenter);

        horizontalLayout_3->addWidget(label_10);


        horizontalLayout_2->addWidget(widget_2);


        horizontalLayout->addWidget(frame_2);

        frame_3 = new QFrame(headerLogin);
        frame_3->setObjectName(QStringLiteral("frame_3"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        verticalLayout_4 = new QVBoxLayout(frame_3);
        verticalLayout_4->setObjectName(QStringLiteral("verticalLayout_4"));
        horizontalSpacer = new QSpacerItem(499, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        verticalLayout_4->addItem(horizontalSpacer);


        horizontalLayout->addWidget(frame_3);

        dialogBtn = new QFrame(headerLogin);
        dialogBtn->setObjectName(QStringLiteral("dialogBtn"));
        dialogBtn->setStyleSheet(QLatin1String("#closeWindowsBtn:hover{\n"
"background-color:red;\n"
"\n"
"}\n"
"#minimizeWindowsBtn:hover,#restoreWindowsBtn:hover{\n"
"background-color: #24262b;\n"
"}"));
        dialogBtn->setFrameShape(QFrame::StyledPanel);
        dialogBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(dialogBtn);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(-1, 0, -1, 0);
        minimizeWindowsBtn = new QPushButton(dialogBtn);
        minimizeWindowsBtn->setObjectName(QStringLiteral("minimizeWindowsBtn"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(minimizeWindowsBtn->sizePolicy().hasHeightForWidth());
        minimizeWindowsBtn->setSizePolicy(sizePolicy);
        minimizeWindowsBtn->setCursor(QCursor(Qt::PointingHandCursor));
        minimizeWindowsBtn->setStyleSheet(QStringLiteral("border-radius:none;"));
        QIcon icon;
        icon.addFile(QStringLiteral(":/Icons/Icons/minus.svg"), QSize(), QIcon::Normal, QIcon::Off);
        minimizeWindowsBtn->setIcon(icon);

        horizontalLayout_4->addWidget(minimizeWindowsBtn);

        restoreWindowsBtn = new QPushButton(dialogBtn);
        restoreWindowsBtn->setObjectName(QStringLiteral("restoreWindowsBtn"));
        sizePolicy.setHeightForWidth(restoreWindowsBtn->sizePolicy().hasHeightForWidth());
        restoreWindowsBtn->setSizePolicy(sizePolicy);
        restoreWindowsBtn->setCursor(QCursor(Qt::PointingHandCursor));
        restoreWindowsBtn->setStyleSheet(QStringLiteral("border-radius:none;"));
        QIcon icon1;
        icon1.addFile(QStringLiteral(":/Icons/Icons/square.svg"), QSize(), QIcon::Normal, QIcon::Off);
        restoreWindowsBtn->setIcon(icon1);

        horizontalLayout_4->addWidget(restoreWindowsBtn);

        closeWindowsBtn = new QPushButton(dialogBtn);
        closeWindowsBtn->setObjectName(QStringLiteral("closeWindowsBtn"));
        sizePolicy.setHeightForWidth(closeWindowsBtn->sizePolicy().hasHeightForWidth());
        closeWindowsBtn->setSizePolicy(sizePolicy);
        closeWindowsBtn->setCursor(QCursor(Qt::PointingHandCursor));
        closeWindowsBtn->setStyleSheet(QStringLiteral("border-radius:none;"));
        QIcon icon2;
        icon2.addFile(QStringLiteral(":/Icons/Icons/x.svg"), QSize(), QIcon::Normal, QIcon::Off);
        closeWindowsBtn->setIcon(icon2);

        horizontalLayout_4->addWidget(closeWindowsBtn);


        horizontalLayout->addWidget(dialogBtn);

        txtDatabaseconnection = new QLabel(widget);
        txtDatabaseconnection->setObjectName(QStringLiteral("txtDatabaseconnection"));
        txtDatabaseconnection->setGeometry(QRect(20, 680, 251, 16));
        QFont font7;
        font7.setBold(true);
        font7.setWeight(75);
        txtDatabaseconnection->setFont(font7);
        txtDatabaseconnection->setStyleSheet(QStringLiteral("color:#2c313c;"));

        verticalLayout_2->addWidget(widget);


        verticalLayout->addWidget(frame);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", nullptr));
        label->setText(QString());
        label_2->setText(QApplication::translate("Dialog", "LOG IN", nullptr));
        loginUsername->setPlaceholderText(QApplication::translate("Dialog", "User Name", nullptr));
        loginPassword->setPlaceholderText(QApplication::translate("Dialog", "Password", nullptr));
        loginBtn->setText(QApplication::translate("Dialog", "Log In", nullptr));
        label_3->setText(QApplication::translate("Dialog", "Forgot your User Name | Password ?", nullptr));
        label_5->setText(QApplication::translate("Dialog", "YMCA - IT Service Desk", nullptr));
        label_4->setText(QString());
        txtLoginError->setText(QString());
        txtUserError->setText(QApplication::translate("Dialog", "X", nullptr));
        txtPasswordError->setText(QApplication::translate("Dialog", "X", nullptr));
        label_8->setText(QString());
        label_9->setText(QString());
        label_10->setText(QApplication::translate("Dialog", "YMCA INVENTORY ", nullptr));
#ifndef QT_NO_TOOLTIP
        minimizeWindowsBtn->setToolTip(QApplication::translate("Dialog", "Minimize Window", nullptr));
#endif // QT_NO_TOOLTIP
        minimizeWindowsBtn->setText(QString());
#ifndef QT_NO_TOOLTIP
        restoreWindowsBtn->setToolTip(QApplication::translate("Dialog", "Restore Window", nullptr));
#endif // QT_NO_TOOLTIP
#ifndef QT_NO_TOOLTIP
        closeWindowsBtn->setToolTip(QApplication::translate("Dialog", "Close Window", nullptr));
#endif // QT_NO_TOOLTIP
        closeWindowsBtn->setText(QString());
        txtDatabaseconnection->setText(QString());
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // LOGINSXSWQU_H
