from calc_model import CalcModel
from calc_view import CalcView

class CalcController:

    def __init__(self):
        self.model = CalcModel()
        self.view = CalcView()
        self.view.gui.btnEq.clicked.connect(self.evalExpression)
        self.view.gui.btnAns.clicked.connect(self.prevAnswer)
        self.view.app.exec_()

    def evalExpression(self):
        expr = self.view.gui.txtInput.toPlainText()
        answer = self.model.evaluate(expr)
        self.view.clearInputText()
        self.view.addInputText(answer)

    def prevAnswer(self):
        prevAnswer = self.model.result
        self.view.addInputText(prevAnswer)


if __name__ == '__main__':
    CalcController()
