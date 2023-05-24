import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import uic
import json
from edit_form import EditForm

class ShowNew(QDialog):

    def __init__(self, dashboard, parent=None):
        super(ShowNew, self).__init__(parent)
        self.dashboard = dashboard
        with open("../ClassRanking/data.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        uic.loadUi("../ClassRanking/show_new.ui", self)
        self.setupUi()

    def setupUi(self):
        for i, d in enumerate(self.data):
            name = d["name"]
            pwd = d["pwd"]
            id = str(i)  # generate an identifier based on the index
            # add value for Name Column
            self.valueName = QLabel(self.nameCol)
            self.valueName.setObjectName(id)  # store the identifier in the objectName property
            self.verticalLayout_1.addWidget(self.valueName, 0, Qt.AlignmentFlag.AlignHCenter)
            self.horizontalLayout.addWidget(self.nameCol)
            self.valueName.setText(name)

            # add value for Password column
            self.valuePwd = QLabel(self.pwdCol)
            self.valuePwd.setObjectName(id)  # store the identifier in the objectName property
            self.verticalLayout_2.addWidget(self.valuePwd, 0, Qt.AlignmentFlag.AlignHCenter)
            self.horizontalLayout.addWidget(self.pwdCol)
            self.valuePwd.setText(pwd)

            # add Edit button column
            self.valueEdit = QPushButton(self.editCol)
            self.valueEdit.setObjectName(id)  # store the identifier in the objectName property
            iconEdit = QIcon()
            iconEdit.addFile(u"../ClassRanking/icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.valueEdit.setIcon(iconEdit)
            self.valueEdit.setIconSize(QSize(30, 30))
            self.verticalLayout_3.addWidget(self.valueEdit, 0, Qt.AlignmentFlag.AlignHCenter)
            self.horizontalLayout.addWidget(self.editCol)
            self.valueEdit.setText("")
            self.valueEdit.clicked.connect(self.editClicked)  # connect the clicked signal to a slot

            # add Delete button column
            self.valueDelete = QPushButton(self.deleteCol)
            self.valueDelete.setObjectName(id)  # store the identifier in the objectName property
            iconDelete = QIcon()
            iconDelete.addFile(u"../ClassRanking/icons/remove.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.valueDelete.setIcon(iconDelete)
            self.valueDelete.setIconSize(QSize(30, 30))
            self.verticalLayout_4.addWidget(self.valueDelete, 0, Qt.AlignmentFlag.AlignHCenter)
            self.horizontalLayout.addWidget(self.deleteCol)
            self.valueDelete.setText("")
            self.valueDelete.clicked.connect(self.deleteClicked)  # connect the clicked signal to a slot

    def editClicked(self):
        sender = self.sender()
        index = int(sender.objectName())
        self.editForm = EditForm(self, index, self.dashboard)
        self.editForm.show()

    def deleteClicked(self):
        sender = self.sender()
        index = int(sender.objectName())
        reply = QMessageBox.warning(self, "Warning", "Are you sure you want to delete this entry?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.data.pop(index)
            with open("../ClassRanking/data.json", "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=4, sort_keys=True, ensure_ascii=False)
            self.dashboard.loadCurrentRank()