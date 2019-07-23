import sys
import os
from meal_ui import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication
import json


class AddMeal(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getInformationDic()
        self.startUpInformation()
        self.toggleValue = True
        self.pushButton.clicked.connect(self.calculateFunction)

    def getInformationDic(self):
        with open("information.json","r") as file:
            self.dic = json.load(file)

    def startUpInformation(self):
        for key in self.dic:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setSpacing(20)
            self.horizontalLayout.setObjectName(key)
            self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.checkBox.setEnabled(True)
            self.checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.checkBox.setObjectName(key)
            self.horizontalLayout.addWidget(self.checkBox)
            self.lineEdit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.lineEdit.setEnabled(False)
            self.lineEdit.setMaximumSize(QtCore.QSize(300, 16777215))
            self.lineEdit.setObjectName(key)
            self.horizontalLayout.addWidget(self.lineEdit)
            self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
            self.label_3.setAlignment(QtCore.Qt.AlignCenter)
            self.label_3.setObjectName(key)
            self.horizontalLayout.addWidget(self.label_3)
            self.verticalLayout.addLayout(self.horizontalLayout)
            self.checkBox.setText(key)
            self.label_3.setText(str(self.dic[key]["debt"]))

            self.checkBox.stateChanged.connect(self.checkBoxStateChange)
        self.verticalLayout.addStretch()

    def checkBoxStateChange(self):
        sendingCheckbox = self.sender()
        objectName = sendingCheckbox.objectName()
        lineEdit = self.findChild(QtWidgets.QLineEdit,objectName)
        if sendingCheckbox.isChecked():
            lineEdit.setEnabled(True)
        else:
            lineEdit.setEnabled(False)



    #this function gets lineEdit value and returns valid value
    def returnValidValue(self,value):
        try:
            validValue = int(value)
            return validValue
        except:
            validValue = 0
            return validValue

    #this functio calculates share of every one in a meal
    def calculateFunction(self):
        listOfCollaborators = {}
        sumValue = 0
        for key in self.dic:
            checkBox = self.findChild(QtWidgets.QCheckBox,key)
            lineEdit = self.findChild(QtWidgets.QLineEdit,key)
            if checkBox.isChecked():
                value = self.returnValidValue(lineEdit.text())
                sumValue+=value
                listOfCollaborators[key] = value
        numOfCollaborators = len(listOfCollaborators)

        self.saveMealInformation(listOfCollaborators)
        print(listOfCollaborators)

        for key in listOfCollaborators:
            shareOfEveryOne = sumValue/numOfCollaborators
            listOfCollaborators[key]-=shareOfEveryOne

        self.dumpNewInformation(listOfCollaborators)

    def dumpNewInformation(self,dic):
        with open("information.json",'r') as file:
            oldDic = json.load(file)
        for key in dic:
            oldDic[key]["debt"]+=dic[key]
        with open("information.json",'w') as file:
            json.dump(oldDic,file)
        self.setNewDebts(oldDic)

    #this function sets new debts in the related column
    def setNewDebts(self,newDic):
        for key in newDic:
            debtLabel = self.findChild(QtWidgets.QLabel,key)
            lineEdit = self.findChild(QtWidgets.QLineEdit,key)
            checkBox = self.findChild(QtWidgets.QCheckBox,key)
            debtLabel.setText(str(newDic[key]["debt"]))
            lineEdit.setText("")
            checkBox.setChecked(False)

    def saveMealInformation(self,listOfCollaborators):
        if "MealInformation.txt" not in os.listdir():
            with open("MealInformation.txt","w") as file:
                for key in listOfCollaborators:
                    state = key + "\t" + str(listOfCollaborators[key])
                    file.write(state)
                    file.write("\n")
        else:
            with open("MealInformation.txt","a") as file:
                file.write("\n"+"*"*100+"\n")
                for key in listOfCollaborators:
                    state = key + "\t" + str(listOfCollaborators[key])
                    file.write(state)
                    file.write("\n")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AddMeal()
    ex.show()
    sys.exit(app.exec_())
