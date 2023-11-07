# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminpanel2.ui'
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
        adminpanel1.resize(946, 842)
        adminpanel1.setStyleSheet(u"background-color: rgb(83, 83, 92);")
        self.centralwidget = QWidget(adminpanel1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(260, 300))
        self.groupBox.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_18)

        self.tableWidget = QTableWidget(self.groupBox)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setMinimumSize(QSize(200, 280))
        self.tableWidget.setMaximumSize(QSize(200, 16777215))
        self.tableWidget.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);")

        self.horizontalLayout.addWidget(self.tableWidget)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_19)


        self.gridLayout_3.addWidget(self.groupBox, 0, 3, 3, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 1, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(380, 150))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboBox_2 = QComboBox(self.groupBox_2)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(170, 30))
        self.comboBox_2.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"font: 700 10pt \"gg sans\";")

        self.gridLayout.addWidget(self.comboBox_2, 3, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"gg sans"])
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(260, 20))
        font1 = QFont()
        font1.setFamilies([u"gg sans"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(170, 30))
        self.comboBox.setMaximumSize(QSize(170, 16777215))
        self.comboBox.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"font: 700 10pt \"gg sans\";")

        self.gridLayout.addWidget(self.comboBox, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(250, 30))
        font2 = QFont()
        font2.setFamilies([u"gg sans"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.pushButton, 5, 1, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(380, 150))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.comboBox_4 = QComboBox(self.groupBox_3)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(170, 30))
        self.comboBox_4.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"font: 700 10pt \"gg sans\";\n"
"color: rgb(38, 38, 38);")

        self.gridLayout_2.addWidget(self.comboBox_4, 3, 3, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_15, 3, 2, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(170, 30))
        self.comboBox_3.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"font: 700 10pt \"gg sans\";")

        self.gridLayout_2.addWidget(self.comboBox_3, 3, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_13, 3, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_14, 3, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(250, 30))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.pushButton_2, 5, 1, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 4, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(290, 20))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 3)

        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
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


        self.gridLayout_3.addWidget(self.groupBox_3, 2, 1, 1, 1)

        adminpanel1.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(adminpanel1)
        self.statusbar.setObjectName(u"statusbar")
        adminpanel1.setStatusBar(self.statusbar)

        self.retranslateUi(adminpanel1)

        QMetaObject.connectSlotsByName(adminpanel1)
    # setupUi

    def retranslateUi(self, adminpanel1):
        adminpanel1.setWindowTitle(QCoreApplication.translate("adminpanel1", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0438", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("adminpanel1", u"\u0420\u043e\u043b\u0438", None));
        self.groupBox_2.setTitle("")
        self.comboBox_2.setItemText(0, QCoreApplication.translate("adminpanel1", u"\u041c\u043e\u0434\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("adminpanel1", u"\u0413\u043e\u0441\u0442\u044c", None))

        self.label_3.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label.setText(QCoreApplication.translate("adminpanel1", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0440\u043e\u043b\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_5.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0440\u043e\u043b\u044c:", None))
        self.groupBox_3.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("adminpanel1", u"\u041f\u043e\u0434\u0442\u0432\u0435\u0440\u0434\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("adminpanel1", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u043f\u0440\u0430\u0432 \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043a \u0444\u0430\u0439\u043b\u0430\u043c", None))
        self.label_4.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f:", None))
        self.label_6.setText(QCoreApplication.translate("adminpanel1", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b:", None))
    # retranslateUi

