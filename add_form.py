import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import json

class AddForm(QDialog):

    def __init__(self, parent=None):
        super(AddForm, self).__init__(parent)
        with open("../ClassRanking/data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        uic.loadUi("../ClassRanking/add_form.ui", self)
        self.submit.clicked.connect(self.addNewData)

    def addNewData(self):
        self.nameInput = self.name.text()
        self.pwdInput = self.pwd.text()
        if len(self.nameInput)==0 or len(self.pwdInput)==0:
            self.error.setText("Vui lòng nhập số liệu hợp lệ")
        else:
            self.new_entity = {"name": self.nameInput, "pwd": self.pwdInput}
            self.data.append(self.new_entity)
            with open("../ClassRanking/data.json", "w", encoding="utf-8") as f:
                self.data = json.dump(self.data, f, indent=4, sort_keys=True, ensure_ascii=False)
            self.parent().loadCurrentRank()
            self.close()