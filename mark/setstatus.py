from datetime import datetime
from PyQt5.QtWidgets import QDialog, QMessageBox
from .set_status_markread_ui import Ui_SetMarkStatus
from .database_markread import init_database

class Status(QDialog, Ui_SetMarkStatus):
    def __init__(self, parent, lst):
        self.connection = init_database()
        super(Status, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Установить отметки")
        self.list = lst
        self.myclose = True
        self.calendarWidget.setVisible(False)
        self.btnPrevios.setEnabled(False)
        self.lblIcon.setVisible(False)
        self.adjustSize()
        self.idx_start = 0
        self.datalist = []
        self.load_elem(self.idx_start)
        self.btnNext.clicked.connect(self.next_elem)
        self.btnPrevios.clicked.connect(self.prev_elem)
        self.btnSetStatus.clicked.connect(self.set_status_current_book)
        self.inpDate.setText(str(datetime.now().strftime("%Y.%m.%d")))
        self.btnCalendVis.clicked.connect(self.calendar_visible)
        self.calendarWidget.clicked['QDate'].connect(self.select_date_in_edit)

    def load_elem(self, num):
        self.inpAuthor_st.setText(self.list[num].split(' - ')[0])
        self.inpTitle_st.setText(self.list[num].split(' - ')[1])

    def next_elem(self):
        self.idx_start += 1
        self.btnPrevios.setEnabled(True)
        if self.idx_start == len(self.list) - 1:
            self.btnNext.setEnabled(False)
        self.load_elem(self.idx_start)
        flag = True if self.get_status_book(self.inpTitle_st.text()) else False
        self.lblIcon.setVisible(flag)

    def prev_elem(self):
        self.idx_start -= 1
        self.btnNext.setEnabled(True)
        if self.idx_start == 0:
            self.btnPrevios.setEnabled(False)
        self.load_elem(self.idx_start)
        flag = True if self.get_status_book(self.inpTitle_st.text()) else False
        self.lblIcon.setVisible(flag)

    def set_status_current_book(self):
        book_status = (self.inpAuthor_st.text(), self.inpTitle_st.text(), self.cmbStatus.currentText(),
                       self.cmbOperation.currentText(), self.inpDate.text())
        self.datalist.append(book_status)
        self.lblIcon.setVisible(True)

    def get_status_book(self, book):
        for c in self.datalist:
            if book in c:
                return True
        return False

    def calendar_visible(self):
        if self.btnCalendVis.text() == '▼':
            self.btnCalendVis.setText('▲')
            self.calendarWidget.setVisible(True)
        else:
            self.btnCalendVis.setText('▼')
            self.calendarWidget.setVisible(False)
        self.adjustSize()

    def select_date_in_edit(self):
        date = self.calendarWidget.selectedDate()
        self.inpDate.setText(date.toString('yyyy.MM.dd'))

    def accept(self):
        if len(self.datalist) == 0:
            QMessageBox.critical(self, 'Ошибка', 'Список пуст, вы не внесли никаких отметок')
            return False
        return super().accept()

    def reject(self):
        self.myclose = False
        self.close()

    def closeEvent(self, e):
        self.myclose = False
        self.close()