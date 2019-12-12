from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class UserForm(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("user_form.ui")
        # self.ui.btn_ok.clicked.connect(self.showProp)
        # self.ui.btn_01.clicked.connect(self.show_msg)
        self.ui.show()