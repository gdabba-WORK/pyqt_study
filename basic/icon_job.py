from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QToolTip, QMainWindow, QHBoxLayout, QVBoxLayout


class MyIcon(QWidget):
    def __init__(self):
        # super().__init__()
        # print(super())
        print(QWidget.__init__())
        print(super.__init__)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))
        self.setGeometry(300, 300, 300, 200)

        # button 생성 및 위치
        btn = QPushButton("quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn2 = QPushButton("setStatusMessage", self)
        btn2.move(150, 50)
        btn2.resize(btn2.sizeHint())
        # btn.resize(100, 100)
        # print(btn.sizeHint())

        # layout 지정(hbox, vbox 사용)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(btn)
        hbox.addWidget(btn2)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        # tooltip 표시
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.show()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon("web.png"))
        self.setGeometry(300, 300, 300, 200)

        self.statusBar().showMessage('Ready', 3000)

        # button 생성 및 위치
        btn = QPushButton("quit", self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn2 = QPushButton("setStatusMessage", self)
        btn2.move(150, 50)
        btn2.resize(btn2.sizeHint())
        # btn.resize(100, 100)
        # print(btn.sizeHint())


        # tooltip 표시
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # button sig&slot connect
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.clearStatus)
        btn2.clicked.connect(self.setStatusMsg)
        self.show()

    def setStatusMsg(self):
        self.statusBar().showMessage("set Message")

    def clearStatus(self):
        self.statusBar().clearMessage()


if __name__ == "__main__":
    app = QApplication([])
    # w = MyWindow()
    w = MyIcon()
    app.exec_()
