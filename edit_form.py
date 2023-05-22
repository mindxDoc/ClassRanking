import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import uic
import json

class EditForm(QDialog):

    def __init__(self, parent, index, dashboard): #gọi parent để có quyền access các function của widget trong main.py
        super(EditForm, self).__init__(parent)
        self.index = index
        with open("data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        uic.loadUi("add_form.ui", self) #tận dụng UI và add value từ json vào để thêm quyền edit
        self.name.setText(self.data[self.index]["name"])
        self.pwd.setText(self.data[self.index]["pwd"])
        self.submit.clicked.connect(self.updateData)
        self.dashboard = dashboard

    def updateData(self):
        self.data[self.index]["name"] = self.name.text()
        self.data[self.index]["pwd"] = self.pwd.text()
        if len(self.data[self.index]["name"])==0 or len(self.data[self.index]["pwd"])==0:
            self.error.setText("Vui lòng nhập số liệu hợp lệ")
        else:
            with open("data.json", "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, sort_keys=True, ensure_ascii=False)
            self.dashboard.loadCurrentRank() #gọi từ class Dashboard ở main.py
            self.close()