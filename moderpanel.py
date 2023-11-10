# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'moderpanel.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_adminpanel1(object):
    def setupUi(self, adminpanel1):
        if not adminpanel1.objectName():
            adminpanel1.setObjectName(u"adminpanel1")
        adminpanel1.resize(1125, 850)
        adminpanel1.setStyleSheet(u"background-color: rgb(83, 83, 92);")
        self.centralwidget = QWidget(adminpanel1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(380, 150))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"gg sans"])
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.label_6, 2, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(250, 30))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.pushButton_2, 5, 1, 1, 3)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(290, 20))
        font2 = QFont()
        font2.setFamilies([u"gg sans"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 3)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 3, 4, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(170, 30))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"font: 700 10pt \"gg sans\";")

        self.gridLayout_2.addWidget(self.comboBox_3, 3, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.comboBox_4 = QComboBox(self.groupBox_3)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(170, 30))
        self.comboBox_4.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"font: 700 10pt \"gg sans\";\n"
"color: rgb(38, 38, 38);")

        self.gridLayout_2.addWidget(self.comboBox_4, 3, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 3, 2, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox_3, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(380, 150))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_8, 2, 3, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(250, 30))
        self.pushButton_3.setFont(font1)
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
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_9, 0, 1, 1, 3)


        self.gridLayout_4.addWidget(self.groupBox_4, 3, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 2, 1, 1, 1)

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

        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(300, 280))
        self.tableWidget.setMaximumSize(QSize(200, 16777215))
        self.tableWidget.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);")

        self.horizontalLayout.addWidget(self.tableWidget)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)


        self.gridLayout_4.addWidget(self.groupBox, 0, 3, 4, 1)

        adminpanel1.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(adminpanel1)
        self.statusbar.setObjectName(u"statusbar")
        adminpanel1.setStatusBar(self.statusbar)

        self.retranslateUi(adminpanel1)

        QMetaObject.connectSlotsByName(adminpanel1)
    # setupUi

    def retranslateUi(self, adminpanel1):
        adminpanel1.setWindowTitle(QCoreApplication.translate("adminpanel1", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0441\u0442\u0430\u0442\u0443\u0441:", None))
        self.pushButton_2.setText(QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("adminpanel1", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043a \u0441\u0438\u0441\u0442\u0435\u043c\u0435 ", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("adminpanel1", u"banned", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("adminpanel1", u"active", None))

        self.groupBox_4.setTitle("")
        self.label_7.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_8.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b:", None))
        self.pushButton_3.setText(QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_9.setText(QCoreApplication.translate("adminpanel1", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u0430\u0432 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043a \u0444\u0430\u0439\u043b\u0430\u043c", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("adminpanel1", u"\u0420\u043e\u043b\u0438", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("adminpanel1", u"\u0421\u0442\u0430\u0442\u0443\u0441", None));
    # retranslateUi

