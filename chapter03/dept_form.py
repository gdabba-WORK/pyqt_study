from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QAbstractItemView, QHeaderView, QTableWidgetItem, QAction, \
    QMessageBox
from skimage.viewer.qt import Qt


class DepartUI(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("dept_form.ui")
        self.ui.show()

        self.tbl_widget = self.ui.tbl_widget
        self.tbl_widget.setHorizontalHeaderLabels(["부서번호", "부서명", "위치"])
        # row단위 선택
        self.tbl_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 테이블 직접 값 입력 불가 설정
        self.tbl_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 균일한 간격으로 열 재배치(Qt Designer에 해당 옵션이 존재하지 않아 코드로 직접 설정)
        self.tbl_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # signal & slot
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_del.clicked.connect(self.delete_item)
        self.ui.btn_init.clicked.connect(self.init_item)

        # 마우스 우클릭시 메뉴
        self.set_context_menu(self.tbl_widget)

        data = [(1, "마케팅", 8), (2, "개발", 10), (3, "인사", 20)]
        self.load_data(data)

    def load_data(self, data):
        for idx, (no, name, floor) in enumerate(data):
            item_no, item_name, item_floor = self.create_item(no, name, floor)
            nextIdx = self.tbl_widget.rowCount()
            self.tbl_widget.insertRow(nextIdx)
            self.tbl_widget.setItem(nextIdx, 0, item_no)
            self.tbl_widget.setItem(nextIdx, 1, item_name)
            self.tbl_widget.setItem(nextIdx, 2, item_floor)

    def set_context_menu(self, tv):
        tv.setContextMenuPolicy(Qt.ActionsContextMenu)
        update_action = QAction("수정", tv)
        delete_action = QAction("삭제", tv)
        tv.addAction(update_action)
        tv.addAction(delete_action)
        update_action.triggered.connect(self.__update)
        delete_action.triggered.connect(self.__delete)

    def __update(self):
        QMessageBox.information(self, 'Update', "확인", QMessageBox.Ok)

    def __delete(self):
        QMessageBox.information(self, 'Delete', "확인", QMessageBox.Ok)

    def add_item(self):
        item_no, item_name, item_floor = self.get_item_from_le()
        currentIdx = self.tbl_widget.rowCount()
        print(type(currentIdx))
        self.tbl_widget.insertRow(currentIdx)
        self.tbl_widget.setItem(currentIdx, 0, item_no)
        self.tbl_widget.setItem(currentIdx, 1, item_name)
        self.tbl_widget.setItem(currentIdx, 2, item_floor)
        self.init_item()

    def get_item_from_le(self):
        no = self.ui.le_no.text()
        name = self.ui.le_name.text()
        floor = self.ui.le_floor.text()

        item_no, item_name, item_floor = self.create_item(no, name, floor)

        return item_no, item_name, item_floor

    def create_item(self, no, name, floor):
        item_no = QTableWidgetItem()
        item_no.setTextAlignment(Qt.AlignCenter)
        item_no.setData(Qt.DisplayRole, no)
        item_name = QTableWidgetItem()
        item_name.setTextAlignment(Qt.AlignCenter)
        item_name.setData(Qt.DisplayRole, name)
        item_floor = QTableWidgetItem()
        item_floor.setTextAlignment(Qt.AlignCenter)
        item_floor.setData(Qt.DisplayRole, floor)
        return item_no, item_name, item_floor

    def update_item(self):
        pass

    def delete_item(self):
        # selectionIdxs = self.tbl_widget.selectedIndexes()[0]
        # print(selectionIdxs)
        # self.tbl_widget.removeRow(selectionIdxs.row())
        pass

    def init_item(self):
        self.ui.le_no.clear()
        self.ui.le_name.clear()
        self.ui.le_floor.clear()

if __name__ == "__main__":
    app = QApplication([])
    w = DepartUI()
    app.exec_()