from datetime import datetime
from PyQt5 import Qt
from PyQt5.QtWidgets import QDialog
from .get_statistic_markread_ui import Ui_Statistic
from .query_markread import select_all_query, select_exists_year_query, select_year_query
from .database_markread import init_database, get_all_data, get_exists_year


class Statistic(QDialog, Ui_Statistic):
    def __init__(self, parent):
        super(Statistic, self).__init__(parent)
        self.connection = init_database()
        self.setupUi(self)
        self.setWindowTitle("Статистика чтения")
        self.get_exists_year_and_fill_cmb()
        self.rdAllInBase.clicked.connect(self.activate_all)
        self.rdYear.clicked.connect(self.activate_year)
        self.btnGetReport.clicked.connect(self.get_report)
        self.btnPrint.clicked.connect(self.print_report)
        self.btnExit.clicked.connect(self.closeEvent)

    def get_exists_year_and_fill_cmb(self):
        exists_year = get_exists_year(self.connection, select_exists_year_query).fetchall()
        ls = []
        for year in exists_year:
            if year[0]:
                if year[0][:4] not in ls:
                    ls.append(year[0][:4])
        ls.sort()
        self.cmbYear.addItems(ls)

    def get_report(self):
        rows, titles = self.get_rows()
        d, num = {}, 1
        if self.chkDetails.isChecked():
            titles += ' (детальный вид)'
            for row in rows:
                author, title, status, operation, date_start, date_finish = row[0], row[1], row[2], row[3], row[4], row[
                    5]
                if status == 'Закончил':
                    d1 = datetime.strptime(date_start, "%Y.%m.%d")
                    d2 = datetime.strptime(date_finish, "%Y.%m.%d")
                    duration = (d2 - d1).days
                    if duration == 0:
                        duration = " (тот же день)"
                    else:
                        duration = ' (' + str((d2 - d1).days) + ' дня(ей))'
                    if date_start not in d:
                        d[date_start] = 'Начал ' + operation.lower() + ' ' + author + ' "' + title + '"'
                    else:
                        d[date_start] += '|Начал ' + operation.lower() + ' ' + author + ' "' + title + '"'
                    if date_finish not in d:
                        d[date_finish] = status + ' ' + operation.lower() + ' ' + author + ' "' + title + '"' + duration
                    else:
                        d[date_finish] += '|' + status + ' ' + operation.lower() + ' ' + author + ' "' + title + '"' + duration
                else:
                    if date_start not in d:
                        d[date_start] = status + ' ' + operation.lower() + ' ' + author + ' "' + title + '"'
                    else:
                        d[date_start] += '|' + status + ' ' + operation.lower() + ' ' + author + ' "' + title + '"'
            dd = sorted(d.items())
            t = '<b><font size="5" color="#D0312D">{0}</font></b><br>'.format(titles)
            for st in dd:
                t += '<br><font size="4" color="#D00045">{0}</font><br>'.format(datetime.strptime(st[0], '%Y.%m.%d').strftime('%d.%m.%Y'))
                if '|' in st[1]:
                    s = st[1].split('|')
                    for c in s:
                        t += '<font size="3">{0}</font><br>'.format(c)
                else:
                    t += '<font size="3">{0}</font><br>'.format(st[1])
        else:
            for row in rows:
                author, title, status, date_finish = row[0], row[1], row[2], row[5]
                if status == 'Закончил':
                    if date_finish not in d:
                        d[date_finish] = author + '. "' + title + '"'
                    else:
                        d[date_finish] += '|' + author + '. "' + title + '"'
            dd = sorted(d.items())
            t = '<b><font size="5" color="#D0312D">{0}</font></b><br><br>'.format(titles)
            for st in dd:
                if '|' in st[1]:
                    s = st[1].split('|')
                    for c in s:
                        t += '<font size="3">{0}. {1}</font><br>'.format(str(num), c)
                        num += 1
                else:
                    t += '<font size="3">{0}. {1}</font><br>'.format(str(num), st[1])
                    num += 1
        self.listReport.clear()
        self.listReport.setHtml(t)

    def get_rows(self):
        query, titles, alls = None, None, None
        if self.rdAllInBase.isChecked():
            query = select_all_query
            titles = "Все прочитанные и прослушанные книги"
            alls = get_all_data(self.connection, query)
        elif self.rdYear.isChecked():
            query = select_year_query
            titles = f"Все прочитанные и прослушанные книги за {self.cmbYear.currentText()} год"
            alls = get_all_data(self.connection, query, self.cmbYear.currentText() + '%')
        rows = alls.fetchall()
        return rows, titles

    def activate_year(self):
        self.cmbYear.setEnabled(True)

    def activate_all(self):
        self.cmbYear.setEnabled(False)

    def print_report(self):
        printer = Qt.QPrinter()
        print_dialog = Qt.QPrintDialog(printer)
        if print_dialog.exec() == Qt.QDialog.Accepted:
            self.listReport.print(printer)

    def closeEvent(self, e):
        self.connection.close()
        self.close()
