# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'redactor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_RedWindow(object):
    def setupUi(self, RedWindow):
        if not RedWindow.objectName():
            RedWindow.setObjectName(u"RedWindow")
        RedWindow.resize(1139, 867)
        font = QFont()
        font.setFamilies([u"gg sans"])
        font.setPointSize(12)
        font.setBold(True)
        RedWindow.setFont(font)
        RedWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(RedWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 50, 1098, 779))
        self.frame.setMinimumSize(QSize(1080, 700))
        self.frame.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(83, 83, 92);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(280, 225))
        self.groupBox_4.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_14, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(170, 35))
        font1 = QFont()
        font1.setFamilies([u"gg sans"])
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setUnderline(True)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_5.addWidget(self.pushButton_5, 3, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_15, 2, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_16, 4, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_4)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(170, 35))
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_5.addWidget(self.pushButton_6, 1, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(170, 35))
        font2 = QFont()
        font2.setFamilies([u"gg sans"])
        font2.setPointSize(10)
        font2.setUnderline(True)
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_5.addWidget(self.pushButton_4, 5, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_13, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_4, 2, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 3, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(800, 100))
        self.groupBox.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMinimumSize(QSize(800, 40))
        self.lineEdit_2.setBaseSize(QSize(0, 280))
        font3 = QFont()
        font3.setFamilies([u"gg sans"])
        font3.setPointSize(13)
        font3.setBold(True)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(210, 40))
        font4 = QFont()
        font4.setHintingPreference(QFont.PreferDefaultHinting)
        self.pushButton_8.setFont(font4)
        self.pushButton_8.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(210, 40))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(210, 40))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout.addWidget(self.pushButton_7, 3, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.gridLayout.addItem(self.verticalSpacer_6, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 4, 0, 1, 5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(1080, 50))
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_2.setLayoutDirection(Qt.LeftToRight)
        self.frame_2.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.pushButton_16 = QPushButton(self.frame_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setMinimumSize(QSize(40, 30))
        self.pushButton_16.setMaximumSize(QSize(40, 30))
        font5 = QFont()
        font5.setFamilies([u"gg sans"])
        font5.setPointSize(14)
        font5.setItalic(False)
        self.pushButton_16.setFont(font5)
        self.pushButton_16.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 15px;")

        self.horizontalLayout.addWidget(self.pushButton_16)

        self.pushButton_13 = QPushButton(self.frame_2)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(40, 30))
        self.pushButton_13.setMaximumSize(QSize(40, 30))
        font6 = QFont()
        font6.setPointSize(18)
        font6.setWeight(QFont.Thin)
        font6.setKerning(True)
        self.pushButton_13.setFont(font6)
        self.pushButton_13.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 15px;")

        self.horizontalLayout.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.frame_2)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(40, 30))
        self.pushButton_12.setMaximumSize(QSize(40, 30))
        font7 = QFont()
        font7.setFamilies([u"gg sans"])
        font7.setPointSize(15)
        font7.setBold(True)
        self.pushButton_12.setFont(font7)
        self.pushButton_12.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 15px;")

        self.horizontalLayout.addWidget(self.pushButton_12)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 5)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(280, 225))
        self.groupBox_2.setMaximumSize(QSize(280, 310))
        self.groupBox_2.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(170, 35))
        font8 = QFont()
        font8.setFamilies([u"gg sans"])
        font8.setPointSize(9)
        font8.setBold(True)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.pushButton, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 1, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMinimumSize(QSize(170, 35))
        font9 = QFont()
        font9.setFamilies([u"gg sans"])
        font9.setPointSize(11)
        font9.setBold(True)
        self.pushButton_10.setFont(font9)
        self.pushButton_10.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_10, 6, 1, 1, 1)

        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(140, 16))
        font10 = QFont()
        font10.setPointSize(12)
        font10.setBold(True)
        self.label.setFont(font10)
        self.label.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label, 2, 1, 1, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(170, 30))
        self.comboBox.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);")

        self.gridLayout_3.addWidget(self.comboBox, 3, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(260, 15))
        font11 = QFont()
        font11.setFamilies([u"gg sans"])
        font11.setPointSize(10)
        font11.setBold(True)
        self.label_3.setFont(font11)
        self.label_3.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.groupBox_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(170, 35))
        self.pushButton_9.setFont(font9)
        self.pushButton_9.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_3.addWidget(self.pushButton_9, 5, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_2, 2, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(280, 225))
        self.groupBox_3.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(260, 15))
        self.label_4.setFont(font11)
        self.label_4.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(170, 35))
        self.pushButton_11.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.pushButton_11, 6, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(170, 35))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.pushButton_2, 5, 0, 1, 1)

        self.lineEdit = QLineEdit(self.groupBox_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(170, 35))
        font12 = QFont()
        font12.setFamilies([u"gg sans"])
        font12.setPointSize(14)
        font12.setBold(True)
        self.lineEdit.setFont(font12)
        self.lineEdit.setStyleSheet(u"background-color: rgb(135, 135, 135);\n"
"color: rgb(38, 38, 38);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(140, 15))
        self.label_2.setFont(font10)
        self.label_2.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(135, 135, 135);\n"
"border-radius: 5px;")

        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox_3, 2, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 5, 0, 1, 1)

        RedWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RedWindow)

        QMetaObject.connectSlotsByName(RedWindow)
    # setupUi

    def retranslateUi(self, RedWindow):
        RedWindow.setWindowTitle(QCoreApplication.translate("RedWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440", None))
        self.groupBox_4.setTitle("")
        self.pushButton_5.setText(QCoreApplication.translate("RedWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c \u043c\u043e\u0434\u0435\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.pushButton_6.setText(QCoreApplication.translate("RedWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440\u0430", None))
        self.pushButton_4.setText(QCoreApplication.translate("RedWindow", u"\u041f\u0430\u043d\u0435\u043b\u044c \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.groupBox.setTitle("")
        self.pushButton_8.setText(QCoreApplication.translate("RedWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u0432 \u0437\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u043c \u0444\u043e\u0440\u043c\u0430\u0442\u0435", None))
        self.pushButton_3.setText(QCoreApplication.translate("RedWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.pushButton_7.setText(QCoreApplication.translate("RedWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0444\u0430\u0439\u043b \u0432 \u0437\u0430\u0449\u0438\u0449\u0435\u043d\u043d\u043e\u043c \u0430\u0440\u0445\u0438\u0432\u0435", None))
        self.pushButton_16.setText(QCoreApplication.translate("RedWindow", u"\u2014", None))
        self.pushButton_13.setText(QCoreApplication.translate("RedWindow", u"\ud83d\udf91", None))
        self.pushButton_12.setText(QCoreApplication.translate("RedWindow", u"X", None))
        self.groupBox_2.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("RedWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.pushButton_10.setText(QCoreApplication.translate("RedWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c .zip", None))
        self.label.setText(QCoreApplication.translate("RedWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0444\u0430\u0439\u043b:", None))
        self.label_3.setText(QCoreApplication.translate("RedWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.pushButton_9.setText(QCoreApplication.translate("RedWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c .secretextension", None))
        self.groupBox_3.setTitle("")
        self.label_4.setText(QCoreApplication.translate("RedWindow", u"C\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430 \u0434\u043b\u044f \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.pushButton_11.setText(QCoreApplication.translate("RedWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.pushButton_2.setText(QCoreApplication.translate("RedWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.label_2.setText(QCoreApplication.translate("RedWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0444\u0430\u0439\u043b\u0430:", None))
    # retranslateUi

