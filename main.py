import sys

from basic import hello_pyqt5

from PyQt5.QtWidgets import QApplication, QMainWindow

from chapter01.chap01 import MyApp

from chapter02.user_form import UserForm


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


def ui_init3():
    app = QApplication([])
    w = UserForm()
    app.exec_()


if __name__ == "__main__":
    # ui_init1()
    # ui_init2()
    ui_init3()
