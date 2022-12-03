import os
import sys
import webbrowser
import subprocess
from PyQt5.QtCore import QCoreApplication
from .settingsdialog_ui import Ui_SettingsDialog
from .smartdialog import SmartDialog

_t = QCoreApplication.translate


class SettingsDialog(Ui_SettingsDialog, SmartDialog):
    def __init__(self, parent):
        super(SettingsDialog, self).__init__(parent)
        self.setupUi(self)
        self.restoreSize()
        self.btnEditConfig.clicked.connect(self.onEditConfig)
        self.btnDowloadConverter.clicked.connect(self.onDownloadConverter)
        if sys.platform == 'win32':
            self.textConverterPath.setFilter(_t('SettingsDialog', 'fb2c.exe (fb2c.exe);;All files (*.*)'))
            self.textReaderFb2.setFilter(_t('SettingsDialog', 'Executable files (*.exe);;All files (*.*)'))
            self.textReaderEpub.setFilter(_t('SettingsDialog', 'Executable files (*.exe);;All files (*.*)'))
        else:
            self.textConverterPath.setFilter(_t('SettingsDialog', 'fb2c (fb2c);;All files (*)'))
            self.textReaderFb2.setFilter(_t('SettingsDialog', 'All files (*)'))
            self.textReaderEpub.setFilter(_t('SettingsDialog', 'All files (*)'))
        self.textConverterPath.setCaption(_t('SettingsDialog', 'Select fb2c executable'))
        self.textConverterConfig.setCaption(_t('SettingsDialog', 'Select fb2c config file'))
        self.textConverterConfig.setFilter(_t('SettingsDialog', 'Config files (*.json *.yaml *.yml *.toml);;All files(*.*)'))
        self.myclose = True

    @property
    def converterPath(self):
        return self.textConverterPath.text()

    @property
    def converterConfig(self):
        return self.textConverterConfig.text()

    @property
    def readerAppFb2(self):
        return self.textReaderFb2.text()

    @property
    def readerAppEpub(self):
        return self.textReaderEpub.text()
    @property
    def defaultDir(self):
        return self.textDefaultDir.text()

    @converterPath.setter
    def converterPath(self, value):
        self.textConverterPath.setText(value)

    @converterConfig.setter
    def converterConfig(self, value):
        self.textConverterConfig.setText(value)

    @readerAppFb2.setter
    def readerAppFb2(self, value):
        self.textReaderFb2.setText(value)

    @readerAppEpub.setter
    def readerAppEpub(self, value):
        self.textReaderEpub.setText(value)

    @defaultDir.setter
    def defaultDir(self, value):
        self.textDefaultDir.setText(value)

    def onEditConfig(self):
        if self.converterConfig:
            if sys.platform == 'win32':
                os.startfile(self.converterConfig)
            elif sys.platform == 'darwin':
                subprocess.call(('open', self.converterConfig))
            else:
                subprocess.call(('xdg-open', self.converterConfig))

    def onDownloadConverter(self):
        link = 'https://github.com/rupor-github/fb2converter/releases/'
        browser = webbrowser.get()
        browser.open_new_tab(link)

    def closeEvent(self, e):
        self.myclose = False
        self.close()

    def reject(self):
        self.myclose = False
        self.close()
