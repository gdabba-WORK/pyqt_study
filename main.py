import sys

from PyQt5 import uic

import hello_pyqt5

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("chapter01/chap01.ui")
        ok = self.ui.btn_ok.clicked.connect(self.showProp)
        # self.ui.btn_01.clicked.connect(self.show_msg)
        self.ui.show()

    def showProp(self):
        print("red {} green {} blue {}".format(self.ui.spin_red.value(), self.ui.spin_green.value(), self.ui.spin_blue.value()))
        self.ui.spin_red.setValue(50)
        self.ui.spin_green.setValue(200)
        self.ui.spin_blue.setValue(200)
        print(dir(self.ui.spin_red))


def ui_init1():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = hello_pyqt5.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


def ui_init2():
    app = QApplication([])
    MainWindow = MyApp()
    app.exec_()


if __name__ == "__main__":
    # ui_init1()
    ui_init2()