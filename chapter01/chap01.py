from PyQt5 import uic
from PyQt5.QtWidgets import QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chap01.ui")
        self.ui.btn_ok.clicked.connect(self.showProp)
        # self.ui.btn_01.clicked.connect(self.show_msg)
        self.ui.show()

    def showProp(self):
        print("red {} green {} blue {}".format(self.ui.spin_red.value(), self.ui.spin_green.value(), self.ui.spin_blue.value()))
        self.ui.spin_red.setValue(50)
        self.ui.spin_green.setValue(200)
        self.ui.spin_blue.setValue(200)
        print(dir(self.ui.spin_red))