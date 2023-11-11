# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uuid.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QSize(575, 225))
        font = QFont()
        font.setFamilies([u"gg sans"])
        font.setBold(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QIcon(QIcon.fromTheme(u"accessories-text-editor"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(114, 137, 218);\n"
"border: none;\n"
"padding: 5px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(560, 210))
        self.groupBox.setMaximumSize(QSize(560, 210))
        font1 = QFont()
        font1.setFamilies([u"gg sans"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"background-color: rgb(44, 47, 51);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(250, 70))
        font2 = QFont()
        font2.setFamilies([u"gg sans"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setUnderline(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: rgb(114, 137, 218);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"gg sans"])
        font3.setPointSize(17)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u043e\u0442 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c UUID", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  \u0414\u043b\u044f \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u0430 \u043a \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435 \u0432\u044b \u0434\u043e\u043b\u0436\u043d\u044b \u043f\u0440\u043e\u0439\u0442\u0438 \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0443 \u043e\u0442 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f.", None))
    # retranslateUi

