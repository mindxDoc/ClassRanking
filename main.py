from PyQt6 import QtWidgets as qtw
from PyQt6 import uic
from PyQt6.QtGui import QColor
import sys
from add_form import AddForm
from show_new import ShowNew

class Dashboard(qtw.QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()
        uic.loadUi("main.ui", self)
        self.loadCurrentRank()

        self.detail = None
        self.addNew.clicked.connect(self.openAddForm)
    
    def loadCurrentRank(self):
        self.show_new = ShowNew()
        self.removeAllData()
        self.verticalLayout_4.addWidget(self.show_new)
        self.show_new.show()

    def openAddForm(self):
        self.detail = AddForm(self)
        self.detail.show()

    def removeAllData(self):
        layout = self.verticalLayout_4.layout()
        while layout.count():
            item = layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.deleteLater()

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = Dashboard()
    window.show()
    app.exec()