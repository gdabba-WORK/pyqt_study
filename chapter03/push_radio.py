from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QAbstractItemView, QHeaderView
from skimage.viewer.qt import Qt


class PushRadioUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("push_radio_btns.ui")
        self.ui.show()

        self.ui.btn_ok.clicked.connect(self.clickshow)
        self.ui.btn_cancel.pressed.connect(self.clickshow2)
        self.ui.btn_cancel.clicked.connect(self.clickshow3)

        self.ui.rb_female.clicked.connect(self.female_check)
        self.ui.rb_male.clicked.connect(self.male_check)

        self.ui.rb_male.setChecked(True)

        # UI의 테이블에 직접 접근이 아닌 참조 객체 생성 후 접근
        self.tbl_widget = self.ui.tbl_widget
        self.tbl_widget.setItem(0, 0, QTableWidgetItem("cell(0,0)"))

        item = QTableWidgetItem("cell(0,1)")
        item.setTextAlignment(Qt.AlignCenter)
        self.tbl_widget.setItem(0, 1, item)

        item1 = QTableWidgetItem("cell(0,2)")
        item1.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
        self.tbl_widget.setItem(0, 2, item1)

        table_header = ["첫번째", "두번째", "세번째"]
        self.tbl_widget.setHorizontalHeaderLabels(table_header)
        # row단위 선택
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 테이블 직접 값 입력 불가 설정
        self.tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 균일한 간격으로 열 재배치(Qt Designer에 해당 옵션이 존재하지 않아 코드로 직접 설정)
        self.tbl_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.ui.btn_input.clicked.connect(self.input_table_item)
        self.ui.btn_del.clicked.connect(self.del_table_item)

    def del_table_item(self):
        selectionIdxs = self.tbl_widget.selectedIndexes()[0]
        print(selectionIdxs)
        self.tbl_widget.removeRow(selectionIdxs.row())

    def input_table_item(self):
        v1 = self.ui.le_01.text()
        v2 = self.ui.le_02.text()
        v3 = self.ui.le_03.text()

        item1 = QTableWidgetItem(v1)
        item2 = QTableWidgetItem(v2)
        item3 = QTableWidgetItem(v3)
        item1.setTextAlignment(Qt.AlignCenter)
        item2.setTextAlignment(Qt.AlignCenter)
        item3.setTextAlignment(Qt.AlignCenter)

        currentRowCount = self.tbl_widget.rowCount()
        print(currentRowCount)
        self.tbl_widget.insertRow(currentRowCount)

        self.tbl_widget.setItem(currentRowCount, 0, item1)
        self.tbl_widget.setItem(currentRowCount, 1, item2)
        self.tbl_widget.setItem(currentRowCount, 2, item3)

    def clickshow(self):
        self.ui.lbl_push_res.setText(self.ui.btn_ok.text())

    def clickshow2(self):
        self.ui.lbl_push_res.setText(self.ui.btn_cancel.text())

    def clickshow3(self):
        self.ui.lbl_push_res.setText("clicked!")

    def male_check(self):
        self.ui.btn_ok.setText(self.ui.rb_male.text())
        self.ui.lbl_rb_res.setText(self.ui.rb_male.text())

    def female_check(self):
        self.ui.btn_ok.setText(self.ui.rb_female.text())
        self.ui.lbl_rb_res.setText(self.ui.rb_female.text())


if __name__ =="__main__":
    app = QApplication([])
    w = PushRadioUI()
    app.exec_()

