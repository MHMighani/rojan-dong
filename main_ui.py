# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496, 302)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 30, 200, 50))
        self.pushButton.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:lightgreen;\n"
"    color:white;\n"
"    border:0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:green;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 120, 200, 50))
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 50))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:red;\n"
"    color:white;\n"
"    border:0px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:lightred;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "مشارکت کننده جدید"))
        self.pushButton_2.setText(_translate("MainWindow", "وعده جدید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

