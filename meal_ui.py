# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'meal.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 465)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color:white;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 673, 287))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setSpacing(20)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # self.checkBox.setEnabled(True)
        # self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        # self.checkBox.setObjectName("checkBox")
        # self.horizontalLayout.addWidget(self.checkBox)
        # self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        # self.lineEdit.setEnabled(True)
        # self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
        # self.lineEdit.setObjectName("lineEdit")
        # self.horizontalLayout.addWidget(self.lineEdit)
        # self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_3.setObjectName("label_3")
        # self.horizontalLayout.addWidget(self.label_3)
        # self.verticalLayout.addLayout(self.horizontalLayout)
        # spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 100))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border:0px;\n"
"    background-color:lightgrey;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:grey;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "مادر خرج ها"))
        self.label_4.setText(_translate("MainWindow", "میزان پول پرداخت شده"))
        self.label_2.setText(_translate("MainWindow", "بدهی/طلب"))
        # self.checkBox.setText(_translate("MainWindow", "تست"))
        # self.label_3.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", "محاسبه"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
