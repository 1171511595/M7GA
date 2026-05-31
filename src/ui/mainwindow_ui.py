# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QListView,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(876, 761)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.actionSaveDou = QAction(MainWindow)
        self.actionSaveDou.setObjectName(u"actionSaveDou")
        self.actionluzhi = QAction(MainWindow)
        self.actionluzhi.setObjectName(u"actionluzhi")
        self.actionden_login_Blibili = QAction(MainWindow)
        self.actionden_login_Blibili.setObjectName(u"actionden_login_Blibili")
        self.actionden_login_Douyin = QAction(MainWindow)
        self.actionden_login_Douyin.setObjectName(u"actionden_login_Douyin")
        self.actionden_login_Kuaishou = QAction(MainWindow)
        self.actionden_login_Kuaishou.setObjectName(u"actionden_login_Kuaishou")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(600, 50, 256, 192))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(750, 20, 91, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 91, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(620, 270, 71, 21))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(780, 270, 71, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(590, 410, 141, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(600, 500, 141, 41))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 310, 100, 32))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(590, 360, 100, 32))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 570, 100, 32))
        self.tableWidget_normalMsg = QTableWidget(self.centralwidget)
        self.tableWidget_normalMsg.setObjectName(u"tableWidget_normalMsg")
        self.tableWidget_normalMsg.setGeometry(QRect(10, 20, 551, 541))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 876, 34))
        self.menu_basic_setting = QMenu(self.menubar)
        self.menu_basic_setting.setObjectName(u"menu_basic_setting")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_basic_setting.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menu_basic_setting.addAction(self.actionden_login_Blibili)
        self.menu_basic_setting.addAction(self.actionden_login_Douyin)
        self.menu_basic_setting.addAction(self.actionden_login_Kuaishou)
        self.menu_2.addAction(self.action)
        self.menu_2.addAction(self.actionSaveDou)
        self.menu_2.addAction(self.actionluzhi)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236B\u7ad9\u76f4\u64ad", None))
        self.actionSaveDou.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236\u6296\u97f3\u76f4\u64ad", None))
        self.actionluzhi.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236\u5feb\u624b\u76f4\u64ad", None))
        self.actionden_login_Blibili.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55B\u7ad9\u8d26\u53f7", None))
        self.actionden_login_Douyin.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u6296\u97f3\u8d26\u53f7", None))
        self.actionden_login_Kuaishou.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55\u5feb\u624b\u8d26\u53f7", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u878d\u5408\u5f39\u5e55\u663e\u793a\u533a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u70b9\u4fe1\u606f\u663e\u793a\u533a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u65e5\u603b\u6536\u76ca", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4eca\u65e5\u603b\u6536\u76ca", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u70b9\u4fe1\u606f\u663e\u793a\u533a\u5b57\u53f7\u8bbe\u7f6e", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u878d\u5408\u5f39\u5e55\u663e\u793a\u533a\u5b57\u53f7\u8bbe\u7f6e", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u7ebf\u7a0b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u7ebf\u7a0b", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6dfb\u52a0\u6570\u636e", None))
        self.menu_basic_setting.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u914d\u7f6e", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5f55\u5236", None))
        self.menu_3.setTitle(QCoreApplication.translate("MainWindow", u"\u7edf\u8ba1", None))
        self.menu_4.setTitle(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6", None))
    # retranslateUi

