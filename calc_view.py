from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from functools import partial
import gui_design
import sys

class ExampleApp(QtWidgets.QMainWindow, gui_design.Ui_MainWindow):

    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

class CalcView:

    def __init__(self):
        self.app = QApplication(sys.argv)
        self.gui = ExampleApp()
        self.gui.show()
        self.setupButtons()

    def getInputText(self):
        return self.gui.txtInput.toPlainText()

    def addInputText(self, text):
        inputText = self.getInputText()
        self.gui.txtInput.setPlainText(inputText + text)

    def clearInputText(self):
        self.gui.txtInput.clear()

    def backspaceInputText(self):
        inputText = self.getInputText()
        self.gui.txtInput.setPlainText(inputText[0:-1])

    def setupButtons(self):
        for btn in self.gui.centralwidget.findChildren(QPushButton):
            if btn.text() not in ["C", "CE", "Ans", "="]:
                btn.clicked.connect(partial(self.addInputText, btn.text()))
        self.gui.btnC.clicked.connect(self.clearInputText)
        self.gui.btnCE.clicked.connect(self.backspaceInputText)

    

