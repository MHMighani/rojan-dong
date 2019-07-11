import sys
import os
from addCollaborator_ui import Ui_MainWindow
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QApplication
import json


class AddCollaborator(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.getInformationDic()
        self.pushButton.clicked.connect(self.getInformation)


    def getInformationDic(self):
        if "information.json" not in os.listdir():
            self.dic = {}
            with open("information.json","w") as file:
                json.dump(self.dic,file)
        else:
            with open("information.json","r") as file:
                self.dic = json.load(file)

    def dumpInformation(self):
        with open("information.json","w") as file:
            json.dump(self.dic,file)

        self.close()

    def getInformation(self):
        name = self.lineEdit.text()
        lastName = self.lineEdit_2.text()
        informationDic = {"name":name,"lastName":lastName,"debt":0}
        self.saveInformation(informationDic)

    def saveInformation(self,informationDic):
        name = informationDic["name"]
        self.dic[name] = informationDic
        self.dumpInformation()






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = AddCollaborator()
    ex.show()
    sys.exit(app.exec_())
