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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

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
        self.pushButton_getBilibiliSESSDATA.setGeometry(QRect(20, 100, 111, 31))
        self.pushButton_closeBilibiliWinodw = QPushButton(WidgetLoginBilibili)
        self.pushButton_closeBilibiliWinodw.setObjectName(u"pushButton_closeBilibiliWinodw")
        self.pushButton_closeBilibiliWinodw.setGeometry(QRect(20, 190, 100, 32))

        self.retranslateUi(WidgetLoginBilibili)

        QMetaObject.connectSlotsByName(WidgetLoginBilibili)
    # setupUi

    def retranslateUi(self, WidgetLoginBilibili):
        WidgetLoginBilibili.setWindowTitle(QCoreApplication.translate("WidgetLoginBilibili", u"\u83b7\u53d6B\u7ad9\u767b\u5f55\u6001", None))
        self.pushButton_openBilibiliLogin.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u6253\u5f00\u767b\u5f55\u7a97\u53e3", None))
        self.pushButton_getBilibiliSESSDATA.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u83b7\u53d6\u7528\u6237\u767b\u5f55\u6001", None))
        self.pushButton_closeBilibiliWinodw.setText(QCoreApplication.translate("WidgetLoginBilibili", u"\u5173\u95ed\u7a97\u53e3", None))
    # retranslateUi

