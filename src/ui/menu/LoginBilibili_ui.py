# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginBilibili.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_WidgetLoginBilibili(object):
    def setupUi(self, WidgetLoginBilibili):
        if not WidgetLoginBilibili.objectName():
            WidgetLoginBilibili.setObjectName(u"WidgetLoginBilibili")
        WidgetLoginBilibili.resize(480, 640)
        self.pushButton_openBilibiliLogin = QPushButton(WidgetLoginBilibili)
        self.pushButton_openBilibiliLogin.setObjectName(u"pushButton_openBilibiliLogin")
        self.pushButton_openBilibiliLogin.setGeometry(QRect(20, 20, 100, 32))
        self.pushButton_getBilibiliSESSDATA = QPushButton(WidgetLoginBilibili)
        self.pushButton_getBilibiliSESSDATA.setObjectName(u"pushButton_getBilibiliSESSDATA")
        self.pushButton_getBilibiliSESSDATA.setGeometry(QRect(20, 60, 231, 31))
        self.pushButton_closeBilibiliWinodw = QPushButton(WidgetLoginBilibili)
        self.pushButton_closeBilibiliWinodw.setObjectName(u"pushButton_closeBilibiliWinodw")
        self.pushButton_closeBilibiliWinodw.setGeometry(QRect(360, 580, 100, 32))
        self.pushButton_inputRoomID = QPushButton(WidgetLoginBilibili)
        self.pushButton_inputRoomID.setObjectName(u"pushButton_inputRoomID")
        self.pushButton_inputRoomID.setGeometry(QRect(350, 20, 100, 32))
        self.lineEdit_inputRoomID = QLineEdit(WidgetLoginBilibili)
        self.lineEdit_inputRoomID.setObjectName(u"lineEdit_inputRoomID")
        self.lineEdit_inputRoomID.setGeometry(QRect(230, 20, 113, 21))
        self.label_inputRoomID = QLabel(WidgetLoginBilibili)
        self.label_inputRoomID.setObjectName(u"label_inputRoomID")
        self.label_inputRoomID.setGeometry(QRect(170, 20, 58, 16))
        self.pushButton_fileGetBilibiliSESSDATA = QPushButton(WidgetLoginBilibili)
        self.pushButton_fileGetBilibiliSESSDATA.setObjectName(u"pushButton_fileGetBilibiliSESSDATA")
        self.pushButton_fileGetBilibiliSESSDATA.setGeometry(QRect(20, 100, 231, 31))

        self.retranslateUi(WidgetLoginBilibili)

        QMetaObject.connectSlotsByName(WidgetLoginBilibili)
    # setupUi

    def retranslateUi(self, WidgetLoginBilibili):
        WidgetLoginBilibili.setWindowTitle(QCoreApplication.translate("WidgetLoginBilibili", u"\u83b7\u53d6B\u7ad9\u767b\u5f55\u6001", None))
        self.pushButton_openBilibiliLogin.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u6253\u5f00\u767b\u5f55\u7a97\u53e3", None))
        self.pushButton_getBilibiliSESSDATA.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u4ece\u7f51\u7ad9\u83b7\u53d6\u7528\u6237\u767b\u5f55\u6001", None))
        self.pushButton_closeBilibiliWinodw.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u5173\u95ed\u7a97\u53e3", None))
        self.pushButton_inputRoomID.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u786e\u8ba4\u623f\u95f4ID", None))
        self.label_inputRoomID.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u623f\u95f4ID", None))
        self.pushButton_fileGetBilibiliSESSDATA.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u4ece\u7f13\u5b58\u83b7\u53d6\u7528\u6237\u767b\u5f55\u6001", None))
    # retranslateUi

