from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from .add_profile_markread_ui import Ui_addProfileDialog


class AddProfileDialog(QtWidgets.QDialog, Ui_addProfileDialog):
	def __init__(self, parent):
		super(AddProfileDialog, self).__init__(parent)
		self.setupUi(self)
		self.myclose = True

	def accept(self):
		if self.lineEdit.text() == '':
			QMessageBox.critical(self, 'Ошибка', 'Не введено название профиля')
			return False
		return super().accept()

	def closeEvent(self, e):
		self.myclose = False
		self.close()

	def reject(self):
		self.myclose = False
		self.close()
