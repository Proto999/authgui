# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'userpanel.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

class Ui_UserPanel(object):
    def setupUi(self, UserPanel):
        if not UserPanel.objectName():
            UserPanel.setObjectName(u"UserPanel")
        UserPanel.resize(1125, 850)
        UserPanel.setStyleSheet(u"background-color: rgb(83, 83, 92);")
        self.centralwidget = QWidget(UserPanel)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(317, 300))
        self.groupBox.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)

        self.tableWidget_2 = QTableWidget(self.groupBox)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setMinimumSize(QSize(300, 280))
        self.tableWidget_2.setMaximumSize(QSize(200, 16777215))
        self.tableWidget_2.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);")
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tableWidget_2)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)


        self.gridLayout.addWidget(self.groupBox, 0, 3, 4, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(380, 150))
        self.groupBox_4.setMaximumSize(QSize(505, 230))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setFamilies([u"gg sans"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setUnderline(True)
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_8, 2, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(250, 30))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_3, 5, 1, 1, 3)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 3, 4, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 4, 1, 1, 1)

        self.comboBox_5 = QComboBox(self.groupBox_4)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(170, 30))
        self.comboBox_5.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"font: 700 10pt \"gg sans\";")

        self.gridLayout_3.addWidget(self.comboBox_5, 3, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_17, 3, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 1, 1, 1, 1)

        self.comboBox_6 = QComboBox(self.groupBox_4)
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setMinimumSize(QSize(170, 30))
        self.comboBox_6.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"font: 700 10pt \"gg sans\";\n"
"color: rgb(38, 38, 38);")

        self.gridLayout_3.addWidget(self.comboBox_6, 3, 3, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_20, 3, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(290, 20))
        font3 = QFont()
        font3.setFamilies([u"gg sans"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.label_9.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_9, 0, 1, 1, 3)


        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

        UserPanel.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(UserPanel)
        self.statusbar.setObjectName(u"statusbar")
        UserPanel.setStatusBar(self.statusbar)

        self.retranslateUi(UserPanel)

        QMetaObject.connectSlotsByName(UserPanel)
    # setupUi

    def retranslateUi(self, UserPanel):
        UserPanel.setWindowTitle(QCoreApplication.translate("UserPanel", u"\u041f\u0430\u043d\u0435\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("UserPanel", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("UserPanel", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0444\u0430\u0439\u043b\u044b", None));
        self.groupBox_4.setTitle("")
        self.label_7.setText(QCoreApplication.translate("UserPanel", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("UserPanel", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b:", None))
        self.pushButton_3.setText(QCoreApplication.translate("UserPanel", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_9.setText(QCoreApplication.translate("UserPanel", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u0430\u0432 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043a \u0444\u0430\u0439\u043b\u0430\u043c", None))
    # retranslateUi

