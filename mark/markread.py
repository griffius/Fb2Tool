import re
import sqlite3

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

from .config_mark import settings, init, load, save
from .markread_ui import Ui_MarkRead
from .settingsdialog import SettingsDialog


class MarkRead(QtWidgets.QMainWindow, Ui_MarkRead):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setWindowIcon(QIcon(':/icons/markread_32px.png'))
		init()
		load()
		self.db = Db(self.inpTotal)
		self.w = Worker(self.fill_list_book, self.fill_tags_book, self.lineSearch, self.listBase, self.inpTotal,
						self.inpWork)
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

	def keyPressEvent(self, event):
		if event.key() == QtCore.Qt.Key_Return:
			self.listBase.setFocus()
			self.listBase.setCurrentRow(0)
			self.fill_tags_book(self.listBase.currentItem())
		elif event.key() == QtCore.Qt.Key_F3:
			self.lineSearch.setFocus()
			self.inpAuthor.setText('')
			self.inpTitle.setText('')
		event.accept()

	def fill_list_book(self):
		self.listBase.clear()
		book_in_base = self.db.open_sql()
		if book_in_base:
			for book in book_in_base:
				item = QtWidgets.QListWidgetItem()
				item.setText(book)
				item.setCheckState(QtCore.Qt.Unchecked)
				self.listBase.addItem(item)
			return True
		else:
			return False

	@staticmethod
	def check_item(item):
		if item.checkState() == QtCore.Qt.Checked:
			item.setCheckState(QtCore.Qt.Unchecked)
		else:
			item.setCheckState(QtCore.Qt.Checked)

	def fill_tags_book(self, item):
		tags_book = str(item.text()).split(' - ')
		self.inpAuthor.setText(tags_book[0])
		self.inpTitle.setText(tags_book[-1])

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

	def onSettings(self):
		settingsDialog = SettingsDialog(self)
		settingsDialog.checker_Myhomelib = settings.check_Myhomelib
		settingsDialog.myhomelib = settings.myhomelib
		settingsDialog.checker_Calibre = settings.check_Calibre
		settingsDialog.calibre = settings.calibre
		settingsDialog.searchBase = settings.search_base
		settingsDialog.searchQuery = settings.search
		settingsDialog.markQueryMyhomelib = settings.mark_myhomelib
		if settingsDialog.exec_():
			settings.check_Myhomelib = settingsDialog.checker_Myhomelib
			settings.myhomelib = settingsDialog.myhomelib
			settings.check_Calibre = settingsDialog.checker_Calibre
			settings.calibre = settingsDialog.calibre
			settings.search_base = settingsDialog.searchBase
			settings.search = settingsDialog.searchQuery
			settings.mark_myhomelib = settingsDialog.markQueryMyhomelib
		if settingsDialog.myclose:
			save()
			self.fill_list_book()


class Worker:
	def __init__(self, booklist, taglist, search, listbase, total, work):
		super().__init__()
		self.worklist = []
		self.fill_list_book = booklist
		self.fill_tags_book = taglist
		self.search = search
		self.listbase = listbase
		self.total = total
		self.work = work

	def mark_books(self):
		values = self.get_selected_books()
		self.check_read_status_selected_books(values, settings.myhomelib, 'MyHomeLib', settings.mark_myhomelib)
		QMessageBox.information(MarkRead(), 'Успешно', 'Отметки прочтения выставлены для книг\n' + '\n'.join(values))
		self.fill_list_book()

	def get_selected_books(self):
		self.checkeditems = []
		book_count = self.listbase.count()
		for i in range(book_count):
			if self.listbase.item(i).checkState() == QtCore.Qt.Checked:
				self.checkeditems.append(self.listbase.item(i).text())
		return self.checkeditems

	def check_read_status_selected_books(self, values, db, program, query, subquery='', sqlite_connection=None):
		try:
			sqlite_connection = sqlite3.connect(db)
			cursor = sqlite_connection.cursor()
			for value in values:
				search = query + '"' + value.split(' - ')[1] + '";'
				if program == 'MyHomeLib':
					cursor.execute(search)
				elif program == 'Calibre':
					pass
			sqlite_connection.commit()
		except sqlite3.Error:
			QMessageBox.critical(MarkRead(), 'Ошибка', 'Нет соединения с базой ' + db)
			return False
		finally:
			if sqlite_connection:
				sqlite_connection.close()

	# 				Case "calibre"
	# 					$iRval = _SQLite_GetTable2d($hDskDb, $search, $aResult, $iRows, $iColumns)
	# 					If $iRval = $SQLITE_OK Then
	# 						$id = $aResult[1][0]
	# 						_SQLite_Exec($hDskDb, $subquery & $id & ', 1);')
	# 					EndIf
	# 			EndSwitch
	# 		Next
	# 	EndIf
	# 	_SQLite_Close($hDskDb)
	# 	_SQLite_Shutdown()
	# EndFunc

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
		else:
			QMessageBox.warning(MarkRead(), 'Ошибка', 'Список для обработки пуст')

	def show_alllist(self):
		self.listbase.clear()
		self.listbase.setStyleSheet('background-color: rgb(255, 255, 255);')
		self.fill_list_book()
		self.listbase.setCurrentRow(0)
		self.fill_tags_book(self.listbase.currentItem())
		self.total.setText(str(self.listbase.count()))


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
					book = re.sub(r'([^-]+)( - .*)( - .*) - (.*)', r'\1 - \4', book[0])
				book_in_base.append(book)
			self.total.setText(str(len(book_in_base)))
			return book_in_base
		except sqlite3.Error:
			return False
		finally:
			if sqlite_connection:
				sqlite_connection.close()

# 	Func
# 	_FileBackups($sPathOriginal, $sPathBackup = '', $iCountCopies = 3, $iDiffSize = 0, $iDiffTime = 0, $sSuff = '')
# 	Local $aPath, $aTB, $aTO, $iDateCalc, $Success
# 	If $iCountCopies < 1
# 	Then
# 	Return
# 	SetError(2, 0, 0)
# 	If
# 	Not
# 	FileExists($sPathOriginal) Then
# 	Return
# 	SetError(3, 0, 0)
# 	$aPath = _FO_PathSplit($sPathOriginal)
# 	If
# 	Not $sPathBackup
# 	Then
# 	$sPathBackup = $aPath[0];
# 	если
# 	пустая
# 	строка
#
#
# ElseIf
# Not(StringRegExp($sPathBackup, '(?i)^[a-z]:[^/:*?"<>|]*$') Or
# StringInStr($sPathBackup, '\\')) Then;
# если
# не
# полный
# путь
# или
# не
# UNC
# If
# StringRegExp($sPathBackup, '[/:*?"<>|]') Then
# $sPathBackup = $aPath[0]
# Else
# $sPathBackup = StringReplace($aPath[0] & $sPathBackup & '\', '\\', '\') ; то относительный путь
# EndIf
# EndIf
# Switch $iDiffSize
# Case - 1
# $iDiffSize = 1
# Case
# 0
# $iDiffSize = 0
# Case
# Else
# $iDiffSize = (FileGetSize($sPathOriginal) <> FileGetSize($sPathBackup & $aPath[1] & '_1' & $aPath[2] &$sSuff))
# EndSwitch
# If $iDiffTime
# Then
# $aTO = FileGetTime($sPathOriginal)
# $aTB = FileGetTime($sPathBackup & $aPath[1] & '_1' & $aPath[2] &$sSuff)
# If
# Not @ error
# Then
# $iDateCalc = _DateDiff('s', $aTB[0] & '/' & $aTB[1] & '/' & $aTB[2] & ' ' & $aTB[3] & ':' & $aTB[4] & ':' & $aTB[5], $
# aTO[0] & '/' & $aTO[1] & '/' & $aTO[2] & ' ' & $aTO[3] & ':' & $aTO[4] & ':' & $aTO[5])
# $iDiffTime = ($iDateCalc > $iDiffTime)
# EndIf
# EndIf
# $sPathBackup &= $aPath[1]
# If
# Not
# FileExists($sPathBackup & '_1' & $aPath[2]) Or $iDiffSize
# Or $iDiffTime
# Then
# $Success = 1
# For $i = $iCountCopies
# To
# 2
# Step - 1
# If $Success
# And
# FileExists($sPathBackup & '_' & $i - 1 & $aPath[2] &$sSuff) Then $Success = FileMove($sPathBackup & '_' & $i - 1 & $
# aPath[2] &$sSuff, $sPathBackup & '_' & $i & $aPath[2] &$sSuff, 9)
# Next
# If $Success
# Then $Success = FileCopy($sPathOriginal, $sPathBackup & '_1' & $aPath[2] &$sSuff, 9)
# Return
# SetError(Not $Success, 0, $Success)
# EndIf
# Return
# SetError(0, 0, 0)
# EndFunc
