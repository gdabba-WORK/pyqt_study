from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox


class LambdaUse(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("lambda_use.ui")
        self.ui.show()

        # 변수 stat에는 true가 assignment 된다.
        # ==QAbstractButton.py==
        # def clicked(self, bool=False):  # real signature unknown; restored from __doc__
        #     """ clicked(self, bool = False) [signal] """
        #     pass

        self.ui.btn_ok.clicked.connect(lambda stat, button=self.ui.btn_ok: self.showLabel1(stat, button))
        self.ui.btn_yes.clicked.connect(lambda stat, text=self.ui.btn_yes.text(): self.showLabelText(stat, text))
        self.ui.btn_yes.clicked.connect(self.showLabel2)

    def showLabelText(self, stat, text):
        QMessageBox.information(self, 'btn_yes', text, QMessageBox.Ok)

    def showLabel1(self, stat, button):
        message = self.ui.btn_ok.text()
        # QMessageBox.information(self, 'btn_ok', message, QMessageBox.Ok)
        self.ui.lbl_res.setText(message)

    def showLabel2(self):
        message = self.ui.btn_yes.text()
        # QMessageBox.information(self, 'btn_yes', message, QMessageBox.Ok)
        self.ui.lbl_res.setText(message)


if __name__ == "__main__":
    app = QApplication([])
    w  = LambdaUse()
    app.exec_()