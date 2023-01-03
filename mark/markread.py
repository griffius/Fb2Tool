import os.path
import re
import sqlite3
import datetime
import time
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox, QComboBox
from ebookmeta.myzipfile import ZipFile, ZIP_DEFLATED
from .config_mark import settings, new_simple, init, load, save, read_confs, add_conf, remove_conf, config_path
from .markread_ui import Ui_MarkRead
from .settingsdialog import SettingsDialog
from .addprofile import AddProfileDialog
from .setstatus import Status
from .database_markread import add_records
from .query_markread import add_records_query


class MarkRead(QtWidgets.QMainWindow, Ui_MarkRead):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowIcon(QIcon(':/icons/markread_32px.png'))
		init()
		load()
		self.profiles = Profiles(self.toolBar_profiles, self.fill_list_book, self.inpTotal, self.clearing,
								 self.onSettings, self.visible_control_profiles)
		self.db = Db(self.inpTotal)
		self.w = Worker(self.fill_list_book, self.fill_tags_book, self.lineSearch, self.listBase, self.inpTotal,
						self.inpWork, self.db.backup_db, self.profiles.get_current_profile)
		self.fill_list_book()
		self.listBase.itemDoubleClicked.connect(self.check_item)
		self.listBase.itemClicked.connect(self.fill_tags_book)
		self.lineSearch.textChanged.connect(self.w.search_text)
		self.actionSelectAll.triggered.connect(lambda: self.selection("select"))
		self.actionDeselectAll.triggered.connect(lambda: self.selection("deselect"))
		self.actionInvertSelection.triggered.connect(lambda: self.selection("inverse"))
		self.actionAddToWork.triggered.connect(self.w.add_books_to_worklist)
		self.actionDeleteFromWork.triggered.connect(self.w.del_books_from_worklist)
		self.actionShowWorkList.triggered.connect(self.w.show_worklist)
		self.actionShowAll.triggered.connect(self.w.show_alllist)
		self.actionMarkReadSelected.triggered.connect(self.w.mark_books)
		self.profiles.cmbProfiles.activated.connect(lambda: self.profiles.load_profile(
			self.profiles.get_current_profile()))
		self.actionAddProfile.triggered.connect(self.profiles.addProfileDialog)
		self.actionRemoveProfile.triggered.connect(self.profiles.removeCurrentProfile)
		self.visible_control_profiles()

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Return:
			self.listBase.setFocus()
			self.listBase.setCurrentRow(0)
			self.fill_tags_book(self.listBase.currentItem())
		elif event.key() == QtCore.Qt.Key_F3:
			self.clearing()
		elif event.key() == QtCore.Qt.Key_F9:
			self.profiles.toolbar_visible()
		elif event.key() == QtCore.Qt.Key_Escape:
			self.close()
		event.accept()

	def visible_control_profiles(self):
		if len(read_confs().keys()) > 1:
			self.profiles.cmbProfiles.setEnabled(True)
			self.actionRemoveProfile.setEnabled(True)
		else:
			self.profiles.cmbProfiles.setEnabled(False)
			self.actionRemoveProfile.setEnabled(False)

	def clearing(self, p=False):
		self.lineSearch.setFocus()
		self.inpAuthor.clear()
		self.inpTitle.clear()
		if p:
			self.inpWork.clear()
			self.w.worklist.clear()

	def fill_list_book(self):
		self.listBase.clear()
		try:
			book_in_base = self.db.open_sql()
			if book_in_base:
				for book in book_in_base:
					item = QtWidgets.QListWidgetItem()
					item.setText(book)
					item.setCheckState(QtCore.Qt.Unchecked)
					self.listBase.addItem(item)
				return True
		except:
			return False

	@staticmethod
	def check_item(item):
		if item.checkState() == QtCore.Qt.Checked:
			item.setCheckState(QtCore.Qt.Unchecked)
		else:
			item.setCheckState(QtCore.Qt.Checked)

	def fill_tags_book(self, item, s=1):
		if s == 1:
			tags_book = str(item.text()).split(' - ')
			self.inpAuthor.setText(tags_book[0])
			self.inpTitle.setText(tags_book[-1])
		else:
			self.inpAuthor.clear()
			self.inpTitle.clear()

	def selection(self, p):
		items = range(self.listBase.count())
		for index in items:
			if p == 'select':  # выбрать все
				self.listBase.item(index).setCheckState(QtCore.Qt.Checked)
			elif p == 'deselect':  # снять все
				self.listBase.item(index).setCheckState(QtCore.Qt.Unchecked)
			elif p == 'inverse':  # инвертировать выделение
				if self.listBase.item(index).checkState() == QtCore.Qt.Checked:
					self.listBase.item(index).setCheckState(QtCore.Qt.Unchecked)
				else:
					self.listBase.item(index).setCheckState(QtCore.Qt.Checked)

	def onSettings(self, flag_new=False):
		settingsDialog = SettingsDialog(self)
		if flag_new:
			param = new_simple
			flag = 'new'
			settingsDialog.textQueryMarkCalibre.clear()
		else:
			param = settings
			flag = 'exists'
		settingsDialog.pathBasesCollapsed = param.ui_path_bases_collapsed
		settingsDialog.queryBasesCollapsed = param.ui_query_bases_collapsed
		settingsDialog.backupBasesCollapsed = param.ui_backup_bases_collapsed
		settingsDialog.checker_Myhomelib = param.check_Myhomelib
		settingsDialog.myhomelib = param.myhomelib
		settingsDialog.checker_Calibre = param.check_Calibre
		settingsDialog.calibre = param.calibre
		settingsDialog.searchBase = param.search_base
		settingsDialog.searchQuery = param.search
		settingsDialog.markQueryMyhomelib = param.mark_myhomelib
		settingsDialog.checker_Backup = param.create_backup
		settingsDialog.count_Backup = param.count_backup
		settingsDialog.path_Backup = param.location_backup

		if settingsDialog.exec_():
			param.ui_path_bases_collapsed = settingsDialog.pathBasesCollapsed
			param.ui_query_bases_collapsed = settingsDialog.queryBasesCollapsed
			param.ui_backup_bases_collapsed = settingsDialog.backupBasesCollapsed
			param.check_Myhomelib = settingsDialog.checker_Myhomelib
			param.myhomelib = settingsDialog.myhomelib
			param.check_Calibre = settingsDialog.checker_Calibre
			param.calibre = settingsDialog.calibre
			param.search_base = settingsDialog.searchBase
			param.search = settingsDialog.searchQuery
			param.mark_myhomelib = settingsDialog.markQueryMyhomelib
			param.create_backup = settingsDialog.checker_Backup
			param.count_backup = settingsDialog.count_Backup
			param.location_backup = settingsDialog.path_Backup
		if settingsDialog.myclose:
			save(flag, self.profiles.get_current_profile())
			self.profiles.load_profile(self.profiles.get_current_profile())
			self.fill_list_book()

class Profiles:
	def __init__(self, toolbar, listbook, total, clear, sett, visible):
		super().__init__()
		self.cmbProfiles = None
		self.toolbar = toolbar
		self.fill_list_book = listbook
		self.total = total
		self.clear = clear
		self.sett = sett
		self.visible = visible
		self.toolbar.setVisible(False)
		self.cmb_create()

	def cmb_create(self):
		self.cmbProfiles = QComboBox()
		self.cmbProfiles.setFocusPolicy(Qt.NoFocus)
		self.toolbar.addWidget(self.cmbProfiles)
		self.cmb_fill()

	def cmb_fill(self):
		self.cmbProfiles.clear()
		conf_list = read_confs()
		self.cmbProfiles.addItems(conf_list.keys())

	def get_current_profile(self):
		return self.cmbProfiles.currentText()

	def load_profile(self, profile):
		self.clear(True)
		for key in read_confs()[profile]:
			settings.__dict__[key] = read_confs()[profile][key]
		if not self.fill_list_book():
			self.total.clear()

	def toolbar_visible(self):
		flags = not self.toolbar.isVisible()
		self.toolbar.setVisible(flags)

	def addProfileDialog(self):
		addPfofileDialog = AddProfileDialog(MarkRead())
		addPfofileDialog.exec_()
		if addPfofileDialog.myclose:
			profile = addPfofileDialog.lineEdit.text()
			add_conf(profile)
			self.visible()
			self.cmb_fill()
			self.total.clear()
			QMessageBox.warning(MarkRead(), "Ошибка", "Профиль необходимо настроить")
			self.cmbProfiles.setCurrentText(profile)
			self.sett(flag_new=True)

	def removeCurrentProfile(self):
		confs = read_confs()
		conf = self.get_current_profile()
		if conf == 'MarkRead':
			QMessageBox.warning(MarkRead(), "Ошибка", "Нельзя удалить основной профиль")
		else:
			reply = QMessageBox.question(MarkRead(), 'Удаление профиля', "Вы точно хотите удалить профиль " + conf +'?', QMessageBox.Yes, QMessageBox.No)
			if reply == QMessageBox.Yes:
				del confs[conf]
				remove_conf(confs)
				self.cmb_fill()
				self.load_profile(self.get_current_profile())
			else:
				return False

class Worker:
	def __init__(self, booklist, taglist, search, listbase, total, work, backup_db, profile):
		super().__init__()
		self.w = False
		self.worklist = []
		self.fill_list_book = booklist
		self.fill_tags_book = taglist
		self.search = search
		self.listbase = listbase
		self.total = total
		self.work = work
		self.backup_db = backup_db
		self.profile = profile

	def mark_books(self):
		values = self.get_selected_books()
		if len(values) > 0:
			if self.ex_status_enable():
				readed_books = []
				start_reading_books = []
				status = Status(MarkRead(), values)
				status.exec_()
				if status.myclose:
					dirs = os.path.join('backup_libraly_bases', 'diary reading')
					self.backup_db(os.path.join(config_path, 'status.db'), dirs)
					add_records(status.connection, add_records_query, status.datalist)
					for item in status.datalist:
						if item[2] == 'Закончил':
							readed_books.append(item[0] + ' - ' + item[1])
						else:
							start_reading_books.append(item[0] + ' - ' + item[1])
					if settings.check_Myhomelib:
						self.check_read_status_selected_books(readed_books, settings.myhomelib, 'MyHomeLib', settings.mark_myhomelib)
					if settings.check_Calibre:
						self.check_read_status_selected_books(readed_books, settings.calibre, 'calibre', settings.mark_calibre["query1"],
															  settings.mark_calibre["query2"])
					info = ''
					if len(readed_books) > 0:
						info += 'Отметки прочтения выставлены для книг\n:' + '\n'.join(readed_books)
					if len(start_reading_books) > 0:
						info += '\n' + 'Отметки начала чтения выставлены для книг\n' + '\n'.join(start_reading_books)
					QMessageBox.information(MarkRead(), 'Успешно', info)
					self.fill_list_book()
			else:
				if settings.check_Myhomelib:
					self.check_read_status_selected_books(values, settings.myhomelib, 'MyHomeLib', settings.mark_myhomelib)
				if settings.check_Calibre:
					self.check_read_status_selected_books(values, settings.calibre, 'calibre', settings.mark_calibre["query1"],
														  settings.mark_calibre["query2"])
				QMessageBox.information(MarkRead(), 'Успешно', 'Отметки прочтения выставлены для книг\n' + '\n'.join(values))
				self.fill_list_book()
		else:
			QMessageBox.critical(MarkRead(), 'Ошибка', 'Не выбраны книги')

	def ex_status_enable(self):
		if os.path.isfile(os.path.join(config_path, 'exstatus')) or os.path.isfile(os.path.join(config_path, 'alls')):
			flag = True
		else:
			flag = False
		return flag

	def get_selected_books(self):
		self.checkeditems = []
		book_count = self.listbase.count()
		for i in range(book_count):
			if self.listbase.item(i).checkState() == QtCore.Qt.Checked:
				self.checkeditems.append(self.listbase.item(i).text())
		return self.checkeditems

	def check_read_status_selected_books(self, values, db, program, query, subquery='', sqlite_connection=None):
		try:
			dirs = None
			dirs = os.path.join('backup_libraly_bases', self.profile(), program)
			self.backup_db(db, dirs)
			sqlite_connection = sqlite3.connect(db)
			cursor = sqlite_connection.cursor()
			for value in values:
				search = query + '"' + value.split(' - ')[1] + '";'
				if program == 'MyHomeLib':
					cursor.execute(search)
				elif program == 'calibre':
					cursor.execute(search)
					res_idx = cursor.fetchall()
					idx = str(res_idx[0][0])
					cursor.execute(subquery + idx + ', 1);')
				if self.w:
					self.del_books_from_worklist()
			sqlite_connection.commit()
		except sqlite3.Error:
			QMessageBox.critical(MarkRead(), 'Ошибка', 'Нет соединения с базой ' + db)
			return False
		finally:
			if sqlite_connection:
				sqlite_connection.close()

	# Процедура поиска по тексту с окна ввода
	def search_text(self):
		result_search = []
		self.fill_list_book()
		find_sql = self.search.text().lower()
		items_sql_count = self.listbase.count()
		items = self.listbase.findItems(find_sql, Qt.MatchContains)
		if len(items) > 0:
			for i in range(items_sql_count):
				if find_sql in self.listbase.item(i).text().lower():
					result_search.append(self.listbase.item(i).text())
			self.listbase.clear()
			for book in result_search:
				item = QtWidgets.QListWidgetItem()
				item.setText(book)
				item.setCheckState(QtCore.Qt.Unchecked)
				self.listbase.addItem(item)
			self.total.setText(str(len(result_search)))
		else:
			self.listbase.clear()
			self.total.setText('0')
		if find_sql == '':
			self.fill_list_book()

	# функции для работы с формированием и показом списков
	def add_books_to_worklist(self):
		for book in self.get_selected_books():
			if book not in self.worklist:
				self.worklist.append(book)
		self.work.setText(str(len(self.worklist)))

	def del_books_from_worklist(self):
		for book in self.get_selected_books():
			self.worklist.remove(book)
		self.show_worklist() if len(self.worklist) > 0 else self.show_alllist()

	def show_worklist(self):
		if len(self.worklist) > 0:
			self.listbase.clear()
			self.listbase.setStyleSheet('background-color: rgb(255, 250, 192);')
			for book in self.worklist:
				item = QtWidgets.QListWidgetItem()
				item.setText(book)
				item.setCheckState(QtCore.Qt.Unchecked)
				self.listbase.addItem(item)
			self.listbase.setCurrentRow(0)
			self.fill_tags_book(self.listbase.currentItem())
			self.total.setText(str(self.listbase.count()))
			self.work.setText(str(len(self.worklist)))
			self.w = True
		else:
			QMessageBox.warning(MarkRead(), 'Ошибка', 'Список для обработки пуст')

	def show_alllist(self):
		self.listbase.clear()
		self.listbase.setStyleSheet('background-color: rgb(255, 255, 255);')
		self.fill_list_book()
		self.total.setText(str(self.listbase.count()))
		self.work.setText(str(len(self.worklist)))
		self.w = False


class Db:
	def __init__(self, total):
		super().__init__()
		self.total = total

	def open_sql(self, sqlite_connection=None):
		book_in_base = []
		base = ''
		if settings.search_base == 'MyHomeLib':
			base = settings.myhomelib
		elif settings.search_base == 'Calibre':
			base = settings.calibre
		try:
			sqlite_connection = sqlite3.connect(base)
			cursor = sqlite_connection.cursor()
			cursor.execute(settings.search)
			results = cursor.fetchall()
			for book in results:
				if len(book) == 2:
					if '&' in book[0]:
						aAutors = book[0].split(' & ')
						for i in range(len(aAutors)):
							aAutors[i] = aAutors[i].strip()
							aAutors[i] = re.sub(r'(.*), (.*)', r'\2 \1', aAutors[i])
						sAuthors = ' & '.join(aAutors)
						book = sAuthors + ' - ' + book[1]
					else:
						sAuthors = re.sub(r'(.*), (.*)', r'\2 \1', book[0])
						book = sAuthors + ' - ' + book[1]
				else:
					book = re.sub(r'([^-]+)( - .*)?( - .*)? - (.*)', r'\1 - \4', book[0])
				book_in_base.append(book)
			self.total.setText(str(len(book_in_base)))
			return book_in_base
		except sqlite3.Error:
			return False
		finally:
			if sqlite_connection:
				sqlite_connection.close()

	def backup_db(self, db, directory):
		normal_path = os.path.normpath(os.path.join(settings.location_backup, directory))
		date_backup = time.strftime('%Y%m%d%H%M%S')
		name_backup = "{0}.zip".format(os.path.normpath(os.path.join(normal_path, 'Backup_' + date_backup)))
		if not os.path.exists(normal_path):
			os.mkdir(normal_path)
		aBackupList = os.listdir(normal_path)
		if len(aBackupList) > 0:
			aTablesBackup = []
			for i in range(len(aBackupList)):
				filename = os.path.normpath(os.path.join(normal_path, aBackupList[i]))
				date_create = os.path.getctime(filename)
				date = datetime.datetime.fromtimestamp(date_create).strftime('%Y%m%d%H%M%S')
				elem = (filename, date)
				aTablesBackup.append(elem)
			aTablesBackup.sort(key=lambda x: x[1], reverse=True)
			counter = len(aBackupList)
			if counter >= settings.count_backup:
				count = settings.count_backup - 1
				while counter > count:
					os.remove(aTablesBackup[-1][0])
					aTablesBackup.pop(-1)
					counter -= 1
					zipp = ZipFile(name_backup, mode='w', compression=ZIP_DEFLATED)
					zipp.write(db)
					zipp.close()
			else:
				zipp = ZipFile(name_backup, mode='w', compression=ZIP_DEFLATED)
				zipp.write(db, os.path.basename(db))
				zipp.close()
		else:
			zipp = ZipFile(name_backup, mode='w', compression=ZIP_DEFLATED)
			zipp.write(db)
			zipp.close()
