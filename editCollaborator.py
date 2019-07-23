import sys
from editCollaborator_ui import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication
import json


class editCollaborator(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.infoDicName = "information.json"
        self.addCollaboratorsToScrollArea()

        self.pushButton.clicked.connect(self.deleteSelectedCollaborators)

    #this function returns a dictionary from project directory
    def getInformationDic(self,name):
        with open(name,"r") as file:
            dic = json.load(file)
        return dic

    #Dumps new dictionary
    def dumpInformationDic(self,dic,name):
        with open(name,"w") as file:
            json.dump(dic,file)


    #shows collaborators in scrollArea
    def addCollaboratorsToScrollArea(self):
        information = self.getInformationDic(self.infoDicName)

        for key in information:
            self.horizontalLayout = QtWidgets.QHBoxLayout()
            self.horizontalLayout.setObjectName(key)
            self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
            self.checkBox.setText(key)
            self.checkBox.setObjectName(key)
            self.horizontalLayout.addWidget(self.checkBox)
            self.verticalLayout.addLayout(self.horizontalLayout)

    #This function deletes selected collaborators from informationDic
    def deleteSelectedCollaborators(self):
        informationDic = self.getInformationDic(self.infoDicName)
        informationDic2 = informationDic.copy()
        for key in informationDic:
            checkBox = self.findChild(QtWidgets.QCheckBox,key)
            if checkBox.isChecked():
                informationDic2.pop(key)
        self.dumpInformationDic(informationDic2,self.infoDicName)

        self.updateCollaborators()

    # Updates scrollArea and collaborators after deleting
    def updateCollaborators(self):
        information = self.getInformationDic(self.infoDicName)

        for i in reversed(range(self.verticalLayout.count())):
            horizentalBox = self.verticalLayout.takeAt(i)
            for j in reversed(range(horizentalBox.count())):
                item = horizentalBox.takeAt(j)
                if item is not None:
                    widget = item.widget()
                    widget.setParent(None)
        self.addCollaboratorsToScrollArea()

        
if __name__=="__main__":
    app = QApplication(sys.argv)
    ex = editCollaborator()
    ex.show()
    sys.exit(app.exec_())
