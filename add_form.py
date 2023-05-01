import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import json

class AddForm(QDialog):

    def __init__(self, parent=None):
        super(AddForm, self).__init__(parent)
        with open("data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        uic.loadUi("add_form.ui", self)
        self.submit.clicked.connect(self.addNewData)

    def addNewData(self):
        self.name = self.name.text()
        self.pwd = self.pwd.text()
        self.new_entity = {"name": self.name, "pwd": self.pwd}
        self.data.append(self.new_entity)
        with open("data.json", "w", encoding="utf-8") as f:
            self.data = json.dump(self.data, f, indent=4, sort_keys=True, ensure_ascii=False)
        self.parent().loadCurrentRank()
        self.close()