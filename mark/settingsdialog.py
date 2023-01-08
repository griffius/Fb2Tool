import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog
from .config_mark import settings
from .setting_markread_ui import Ui_settings_mark


class SettingsDialog(QDialog, Ui_settings_mark):
	def __init__(self, parent):
		super(SettingsDialog, self).__init__(parent)
		self.setupUi(self)
		self.myclose = True
		if self.load_query_calibre('query1'):
			self.textQueryMarkCalibre.setPlainText(self.load_query_calibre('query1'))
		self.checkMyhomelib.stateChanged.connect(self.OnIsCheckedMyhomelib)
		self.toolMyhomelib.clicked.connect(self.OnToolMyhomelibBase)
		self.checkCalibre.stateChanged.connect(self.OnIsCheckedCalibre)
		self.toolCalibre.clicked.connect(self.OnToolCalibreBase)
		self.cmbBases.currentIndexChanged.connect(self.OnVisibleQuerySearchControls)
		self.toolSelectQuery.clicked.connect(self.selectQueryCalibre)
		self.checkBackup.stateChanged.connect(self.OnIsCheckerBackup)
		self.toolPathBackup.clicked.connect(self.OnToolPathBackup)
		self.togglePathBases.clicked.connect(self.OnPathBasesToggle)
		self.toggleQueryBases.clicked.connect(self.OnQueryBasesToggle)
		self.toggleBackupBases.clicked.connect(self.OnBackupBasesToggle)
		head_style = 'QToolButton {border: 1px solid black; padding: 3px; color: #1E395B;}'  # #1e395b
		self.togglePathBases.setStyleSheet(head_style)
		self.toggleQueryBases.setStyleSheet(head_style)
		self.toggleBackupBases.setStyleSheet(head_style)

	@property
	def pathBasesCollapsed(self):
		return not self.widgetPathBases.isVisible()

	@pathBasesCollapsed.setter
	def pathBasesCollapsed(self, value):
		if value:
			self.widgetPathBases.setVisible(False)
			self.togglePathBases.setArrowType(Qt.RightArrow)
		else:
			self.widgetPathBases.setVisible(True)
			self.togglePathBases.setArrowType(Qt.DownArrow)
		self.adjustSize()

	@property
	def queryBasesCollapsed(self):
		return not self.widgetQueryBases.isVisible()

	@queryBasesCollapsed.setter
	def queryBasesCollapsed(self, value):
		if value:
			self.widgetQueryBases.setVisible(False)
			self.toggleQueryBases.setArrowType(Qt.RightArrow)
		else:
			self.widgetQueryBases.setVisible(True)
			self.toggleQueryBases.setArrowType(Qt.DownArrow)
		self.adjustSize()

	@property
	def backupBasesCollapsed(self):
		return not self.widgetBackupBases.isVisible()

	@backupBasesCollapsed.setter
	def backupBasesCollapsed(self, value):
		if value:
			self.widgetBackupBases.setVisible(False)
			self.toggleBackupBases.setArrowType(Qt.RightArrow)
		else:
			self.widgetBackupBases.setVisible(True)
			self.toggleBackupBases.setArrowType(Qt.DownArrow)
		self.adjustSize()

	@property
	def checker_Myhomelib(self):
		return self.checkMyhomelib.isChecked()

	@checker_Myhomelib.setter
	def checker_Myhomelib(self, value):
		self.checkMyhomelib.setChecked(value)

	@property
	def myhomelib(self):
		return self.inpMyhomelib.text()

	@myhomelib.setter
	def myhomelib(self, value):
		self.inpMyhomelib.setText(value)

	@property
	def checker_Calibre(self):
		return self.checkCalibre.isChecked()

	@checker_Calibre.setter
	def checker_Calibre(self, value):
		self.checkCalibre.setChecked(value)

	@property
	def calibre(self):
		return self.inpCalibre.text()

	@calibre.setter
	def calibre(self, value):
		self.inpCalibre.setText(value)

	@property
	def searchBase(self):
		return self.cmbBases.currentText()

	@searchBase.setter
	def searchBase(self, value):
		index = self.cmbBases.findText(value)
		if index >= 0:
			self.cmbBases.setCurrentIndex(index)

	@property
	def searchQuery(self):
		return self.textQuerySearch.toPlainText()

	@searchQuery.setter
	def searchQuery(self, value):
		self.textQuerySearch.setPlainText(value)

	@property
	def markQueryMyhomelib(self):
		return self.textQueryMarkMyhomelib.toPlainText()

	@markQueryMyhomelib.setter
	def markQueryMyhomelib(self, value):
		self.textQueryMarkMyhomelib.setPlainText(value)

	@property
	def checker_Backup(self):
		return self.checkBackup.isChecked()

	@checker_Backup.setter
	def checker_Backup(self, value):
		self.checkBackup.setChecked(value)

	@property
	def count_Backup(self):
		return self.spinBox.value()

	@count_Backup.setter
	def count_Backup(self, value):
		self.spinBox.setValue(value)

	@property
	def path_Backup(self):
		return self.textPathBackup.text()

	@path_Backup.setter
	def path_Backup(self, value):
		self.textPathBackup.setText(value)

	def OnIsCheckedMyhomelib(self):
		flags = self.checkMyhomelib.isChecked()
		self.inpMyhomelib.setEnabled(flags)
		self.inpMyhomelib.clear()
		self.toolMyhomelib.setEnabled(flags)
		self.cmbBases.addItem('MyHomeLib') if flags else self.cmbBases.removeItem(self.cmbBases.findText('MyHomeLib'))
		self.lblQueryMarkMyhomelib.setEnabled(flags)
		self.textQueryMarkMyhomelib.setEnabled(flags)
		if not flags:
			self.textQueryMarkMyhomelib.clear()

	def OnToolMyhomelibBase(self):
		data = self.inpMyhomelib.text()
		result = QFileDialog.getOpenFileName(self, caption='Выберите файл базы книг MyHomeLib', directory='D:/',
												  filter='MyHomeLib base (*.hlc2);;All files(*.*)')
		if result:
			self.inpMyhomelib.setText(os.path.normpath(result[0])) if result[0] else self.inpMyhomelib.setText(data)

	def selectQueryCalibre(self):
		if self.lblQueryCalibre.text() == 'Первый запрос':
			self.lblQueryCalibre.setText('Второй запрос')
			self.toolSelectQuery.setText('<-')
			self.save_query_calibre('query1')
			self.textQueryMarkCalibre.setPlainText(self.load_query_calibre('query2'))
		else:
			self.lblQueryCalibre.setText('Первый запрос')
			self.toolSelectQuery.setText('->')
			self.save_query_calibre('query2')
			self.textQueryMarkCalibre.setPlainText(self.load_query_calibre('query1'))

	def OnIsCheckedCalibre(self):
		flags = self.checkCalibre.isChecked()
		self.inpCalibre.setEnabled(flags)
		self.inpCalibre.clear()
		self.toolCalibre.setEnabled(flags)
		self.cmbBases.addItem('Calibre') if flags else self.cmbBases.removeItem(self.cmbBases.findText('Calibre'))
		self.lblQueryMarkCalibre.setEnabled(flags)
		self.lblQueryCalibre.setEnabled(flags)
		self.toolSelectQuery.setEnabled(flags)
		self.textQueryMarkCalibre.setEnabled(flags)
		if not flags:
			self.textQueryMarkCalibre.clear()

	def OnToolCalibreBase(self):
		data = self.inpCalibre.text()
		result = QFileDialog.getOpenFileName(self, caption='Выберите файл базы книг Calibre', directory='D:/',
												  filter='MyHomeLib base (metadata.db);;All files(*.*)')
		if result:
			self.inpCalibre.setText(os.path.normpath(result[0])) if result[0] else self.inpCalibre.setText(data)

	def OnVisibleQuerySearchControls(self):
		if self.cmbBases.count() >= 1:
			self.lblQuerySearch.setEnabled(True)
			self.textQuerySearch.setEnabled(True)
		else:
			self.textQuerySearch.setEnabled(False)
			self.lblQuerySearch.setEnabled(False)
			self.textQuerySearch.clear()

	def OnIsCheckerBackup(self):
		flags = self.checkBackup.isChecked()
		self.lblCountBackup.setEnabled(flags)
		self.spinBox.setEnabled(flags)
		self.lblPathBackup.setEnabled(flags)
		self.textPathBackup.setEnabled(flags)
		self.toolPathBackup.setEnabled(flags)

	def OnToolPathBackup(self):
		data = self.textPathBackup.text()
		result = QFileDialog.getExistingDirectory(self, caption='Выберите папку для сохранений резервных копий баз',
												  directory='D:/')
		if result:
			self.textPathBackup.setText(os.path.normpath(result)) if result[0] else self.textPathBackup.setText(data)

	def closeEvent(self, e):
		self.myclose = False
		self.close()

	def reject(self):
		self.myclose = False
		self.close()

	def load_query_calibre(self, key, default_value=None):
		if key in settings.mark_calibre.keys():
			return settings.mark_calibre[key]
		else:
			return default_value

	def save_query_calibre(self, key):
		settings.mark_calibre[key] = self.textQueryMarkCalibre.toPlainText()

	def OnPathBasesToggle(self):
		if self.widgetPathBases.isVisible():
			self.widgetPathBases.setVisible(False)
			self.togglePathBases.setArrowType(Qt.RightArrow)
		else:
			self.widgetPathBases.setVisible(True)
			self.togglePathBases.setArrowType(Qt.DownArrow)
		self.adjustSize()

	def OnQueryBasesToggle(self):
		if self.widgetQueryBases.isVisible():
			self.widgetQueryBases.setVisible(False)
			self.toggleQueryBases.setArrowType(Qt.RightArrow)
		else:
			self.widgetQueryBases.setVisible(True)
			self.toggleQueryBases.setArrowType(Qt.DownArrow)
		self.adjustSize()

	def OnBackupBasesToggle(self):
		if self.widgetBackupBases.isVisible():
			self.widgetBackupBases.setVisible(False)
			self.toggleBackupBases.setArrowType(Qt.RightArrow)
		else:
			self.widgetBackupBases.setVisible(True)
			self.toggleBackupBases.setArrowType(Qt.DownArrow)
		self.adjustSize()

	def accept(self):
		if self.checker_Myhomelib:
			if not os.path.exists(self.myhomelib):
				QMessageBox.critical(self, 'Ошибка', f'Файл "{self.myhomelib}" не существует')
				return False
		if self.checker_Calibre:
			if not os.path.exists(self.calibre):
				QMessageBox.critical(self, 'Ошибка', f'File "{self.calibre}" не существует')
				return False
		if self.textQuerySearch.isEnabled():
			if self.textQuerySearch.toPlainText() == '':
				QMessageBox.critical(self, 'Ошибка', 'Поисковый запрос не может быть пустым')
				return False
		if self.textQueryMarkMyhomelib.isEnabled():
			if self.textQueryMarkMyhomelib.toPlainText() == '':
				QMessageBox.critical(self, 'Ошибка', 'Запрос для установки отметки для базы MyHomeLib не может быть пустым')
				return False
		if self.textQueryMarkCalibre.isEnabled():
			if self.textQueryMarkCalibre.toPlainText() == '':
				QMessageBox.critical(self, 'Ошибка', 'Запрос для установки отметки для базы Calibre не может быть пустым')
				return False
		if self.checker_Backup:
			if not os.path.exists(self.path_Backup):
				QMessageBox.critical(self, 'Ошибка', 'Папка для резервных копий не существует или не выбрана')
				return False
		return super().accept()
