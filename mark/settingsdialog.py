import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

from .config_mark import settings
from .setting_markread_ui import Ui_settings_mark


class SettingsDialog(QtWidgets.QDialog, Ui_settings_mark):
	def __init__(self, parent):
		super(SettingsDialog, self).__init__(parent)
		self.setupUi(self)
		self.myclose = True
		self.groupCalibre.setCurrentIndex(0)
		self.checkMyhomelib.stateChanged.connect(self.OnIsCheckedMyhomelib)
		self.toolMyhomelib.clicked.connect(self.onToolMyhomelibBase)
		self.checkCalibre.stateChanged.connect(self.OnIsCheckedCalibre)
		self.toolCalibre.clicked.connect(self.onToolCalibreBase)
		self.cmbBases.currentIndexChanged.connect(self.OnVisibleQuerySearchControls)
		self.tootNextTab.clicked.connect(lambda: self.selectTabQueryCalibre('Первый запрос'))
		self.tootPreviosTab.clicked.connect(lambda: self.selectTabQueryCalibre('Второй запрос'))
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
	def markQueryCalibre1(self):
		return self.textQueryMarkCalibre1.toPlainText()

	@markQueryCalibre1.setter
	def markQueryCalibre1(self, value):
		self.textQueryMarkCalibre1.setPlainText(value)

	@property
	def markQueryCalibre2(self):
		return self.textQueryMarkCalibre2.toPlainText()

	@markQueryCalibre2.setter
	def markQueryCalibre2(self, value):
		self.textQueryMarkCalibre2.setPlainText(value)

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

	def onToolMyhomelibBase(self):
		data = self.inpMyhomelib.text()
		result = QFileDialog.getOpenFileName(self, caption='Select base MyHomeLib', directory='D:/',
												  filter='MyHomeLib base (*.hlc2);;All files(*.*)')
		if result:
			self.inpMyhomelib.setText(result[0]) if result[0] else self.inpMyhomelib.setText(data)

	def selectTabQueryCalibre(self, t):
		self.groupCalibre.setCurrentIndex(0) if t == 'Второй запрос' else self.groupCalibre.setCurrentIndex(1)

	def OnIsCheckedCalibre(self):
		flags = self.checkCalibre.isChecked()
		self.inpCalibre.setEnabled(flags)
		self.inpCalibre.clear()
		self.toolCalibre.setEnabled(flags)
		self.cmbBases.addItem('Calibre') if flags else self.cmbBases.removeItem(self.cmbBases.findText('Calibre'))
		self.lblQueryMarkCalibre.setEnabled(flags)
		self.groupCalibre.setEnabled(flags)
		self.lblFirstQueryCalibre.setEnabled(flags)
		self.lblSecondQueryCalibre.setEnabled(flags)
		self.textQueryMarkCalibre1.setEnabled(flags)
		self.textQueryMarkCalibre2.setEnabled(flags)
		if not flags:
			self.textQueryMarkCalibre1.clear()
			self.textQueryMarkCalibre2.clear()

	def onToolCalibreBase(self):
		data = self.inpCalibre.text()
		result = QFileDialog.getOpenFileName(self, caption='Select base Calibre', directory='D:/',
												  filter='MyHomeLib base (metadata.db);;All files(*.*)')
		if result:
			self.inpCalibre.setText(result[0]) if result[0] else self.inpCalibre.setText(data)

	def OnVisibleQuerySearchControls(self):
		if self.cmbBases.count() >= 1:
			self.lblQuerySearch.setEnabled(True)
			self.textQuerySearch.setEnabled(True)
		else:
			self.textQuerySearch.setEnabled(False)
			self.lblQuerySearch.setEnabled(False)
			self.textQuerySearch.clear()

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

	def save_query_calibre(self, key, value):
		settings.mark_calibre[key] = value

	def accept(self):
		if self.checker_Myhomelib:
			if not os.path.exists(self.myhomelib):
				QMessageBox.critical(self, 'Markread', f'Файл "{self.myhomelib}" не существует')
				return False
		if self.checker_Calibre:
			if not os.path.exists(self.calibre):
				QMessageBox.critical(self, 'Markread', f'File "{self.calibre}" не существует')
				return False
		if self.textQuerySearch.isEnabled():
			if self.textQuerySearch.toPlainText() == '':
				QMessageBox.critical(self, 'Markread', 'Поисковый запрос не может быть пустым')
				return False
		if self.textQueryMarkMyhomelib.isEnabled():
			if self.textQueryMarkMyhomelib.toPlainText() == '':
				QMessageBox.critical(self, 'Markread', 'Запрос для установки отметки для базы MyHomeLib не может быть пустым')
				return False
		# if self.textQueryMarkCalibre.isEnabled():
		# 	if self.textQueryMarkCalibre.toPlainText() == '':
		# 		QMessageBox.critical(self, 'Markread', 'Запрос для установки отметки для базы Calibre не может быть пустым')
		# 		return False
		return super().accept()
