import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import json

class ShowNew(QDialog):

    def __init__(self, parent=None):
        super(ShowNew, self).__init__(parent)
        with open("data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        uic.loadUi("show_new.ui", self)
        self.setupUi()

    def setupUi(self):
        for d in self.data:
            name = d["name"]
            pwd = d["pwd"]
            #add value for Name Column
            self.valueName = QLabel(self.nameCol)
            self.valueName.setObjectName(u"valueName")
            self.verticalLayout.addWidget(self.valueName, 0, Qt.AlignmentFlag.AlignHCenter)
            self.horizontalLayout.addWidget(self.nameCol)
            self.valueName.setText(name)

            #add value for Password column
            self.valuePwd = QLabel(self.pwdCol)
            self.valuePwd.setObjectName(u"valuePwd")
            self.verticalLayout_2.addWidget(self.valuePwd, 0, Qt.AlignmentFlag.AlignHCenter)
            self.horizontalLayout.addWidget(self.pwdCol)
            self.valuePwd.setText(pwd)