import sys
import os
from main_ui import Ui_MainWindow
from meal import AddMeal
from addCollaborator import AddCollaborator
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication
import json


class mainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pushButton_2.clicked.connect(self.showMealWindow)

    def showMealWindow(self):
        self.mealWindow = AddMeal()
        self.mealWindow.show()

    def showAddCollaboratorWindow(self):
        self.addCollaboratorWindow = AddCollaborator()
        self.addCollaboratorWindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainWindow()
    ex.show()
    sys.exit(app.exec_())
