import os
import toml
from PyQt5.QtCore import QCoreApplication, QPoint
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QMenu
import config
from .convertdialog_ui import Ui_ConvertDialog
from .smartdialog import SmartDialog

settings = config.settings
_t = QCoreApplication.translate


class ConvertDialog(SmartDialog, Ui_ConvertDialog):
    def __init__(self, parent):
        super(ConvertDialog, self).__init__(parent)
        self.setupUi(self)
        self.restoreSize()
        self._path_list = set()
        self.comboFormat.currentIndexChanged.connect(self.onFormatChanged)
        self.checkSendToKindle.stateChanged.connect(self.onSendtokindleChanged)
        self.checkDelAftefSend.stateChanged.connect(self.onDeleteaftersendChanged)
        self.checkMoveToFinal.stateChanged.connect(self.onMovetofinalChanged)
        self.checkUseScructurSrc.stateChanged.connect(self.onCreateStrucArcSrc)
        self.toolAuthorPattern.clicked.connect(self.onToolAuthorPattern)
        self.toolDirPattern.clicked.connect(self.onToolDirPattern)
        self.textOutputDir.clicked.connect(self.onTextOutputDirClick)
        self.c = None
        self.textFinalDir.clicked.connect(self.onTextFinalDirClick)
        self._path_list_final_fb2 = set()
        self.tabWidget.setCurrentIndex(0)
        self.getstatedelaftersend()

    @property
    def outputFormat(self):
        return self.comboFormat.currentText()

    @property
    def outputPath(self):
        return self.textOutputDir.text()

    @property
    def overwrite(self):
        return self.checkOverwrite.isChecked()

    @property
    def stk(self):
        return self.checkSendToKindle.isChecked()
    
    @property
    def debug(self):
        return self.checkDebug.isChecked()
    
    @property
    def convertPathList(self):
        return list(self._path_list)
    
    @property
    def packoutput(self):
        return self.checkPackOutputFiles.isChecked()

    @property
    def movetofinal(self):
        return self.checkMoveToFinal.isChecked()

    @property
    def packfinal(self):
        return self.checkPackFinal.isChecked()

    @property
    def usestructursrc(self):
        return self.checkUseScructurSrc.isChecked()

    @property
    def authorpattern(self):
        return self.textAuthorPattern.text()

    @property
    def dirpattern(self):
        return self.textDirPattern.text()

    @property
    def finalDir(self):
        return self.textFinalDir.text()

    @property
    def finalFb2PathList(self):
        return list(self._path_list_final_fb2)

    @outputPath.setter
    def outputPath(self, value):
        self.textOutputDir.setText(value)

    @outputFormat.setter
    def outputFormat(self, value):
        index = self.comboFormat.findText(value)
        if index >= 0:
            self.comboFormat.setCurrentIndex(index)
        self.onFormatChanged()

    @overwrite.setter
    def overwrite(self, value):
        self.checkOverwrite.setChecked(value)

    @stk.setter
    def stk(self, value):
        self.checkDelAftefSend.setEnabled(value)
        self.checkSendToKindle.setChecked(value)

    @debug.setter
    def debug(self, value):
        self.checkDebug.setChecked(value)

    @convertPathList.setter
    def convertPathList(self, values):
        if values:
            for val in values:
                self._path_list.add(val)

    @packoutput.setter
    def packoutput(self, value):
        self.checkPackOutputFiles.setChecked(value)

    @movetofinal.setter
    def movetofinal(self, value):
        self.checkMoveToFinal.setChecked(value)

    @packfinal.setter
    def packfinal(self, value):
        self.checkPackFinal.setChecked(value)

    @usestructursrc.setter
    def usestructursrc(self, value):
        self.checkUseScructurSrc.setChecked(value)

    @authorpattern.setter
    def authorpattern(self, value):
        self.textAuthorPattern.setText(value)

    @dirpattern.setter
    def dirpattern(self, value):
        self.textDirPattern.setText(value)

    @finalDir.setter
    def finalDir(self, value):
        self.textFinalDir.setText(value)

    @finalFb2PathList.setter
    def finalFb2PathList(self, values):
        if values:
            for val in values:
                self._path_list_final_fb2.add(val)

    def onFormatChanged(self):
        self.checkSendToKindle.setEnabled(self.comboFormat.currentText() == 'epub')
        self.checkDelAftefSend.setEnabled(self.comboFormat.currentText() == 'epub')

    def onMovetofinalChanged(self):
        flags = self.checkMoveToFinal.isChecked()
        if not flags:
            self.checkPackFinal.setChecked(flags)
            self.checkUseScructurSrc.setChecked(flags)
        self.textFinalDir.setEnabled(self.checkMoveToFinal.isChecked())
        self.checkPackFinal.setEnabled(self.checkMoveToFinal.isChecked())
        self.checkUseScructurSrc.setEnabled(self.checkMoveToFinal.isChecked())

    def onCreateStrucArcSrc(self):
        self.textAuthorPattern.setEnabled(self.checkUseScructurSrc.isChecked())
        self.toolAuthorPattern.setEnabled(self.checkUseScructurSrc.isChecked())
        self.textDirPattern.setEnabled(self.checkUseScructurSrc.isChecked())
        self.toolDirPattern.setEnabled(self.checkUseScructurSrc.isChecked())

    def onSendtokindleChanged(self):
        self.checkDelAftefSend.setEnabled(self.checkSendToKindle.isChecked())

    def onDeleteaftersendChanged(self):
        flags = not self.checkDelAftefSend.isChecked()
        self.checkPackOutputFiles.setEnabled(flags)
        self.c['sendtokindle']['delete_sent_book'] = True if self.checkDelAftefSend.isChecked() else False
        with open(settings.convert_converter_config, 'w', encoding='utf-8') as f:
            toml.dump(self.c, f)

    def getstatedelaftersend(self):
        if settings.convert_converter_config:
            self.c = toml.load(settings.convert_converter_config)
            state = self.c['sendtokindle']['delete_sent_book']
            self.checkDelAftefSend.setChecked(state)
        else:
            self.checkDelAftefSend.setEnabled(False)

    def onTextOutputDirClick(self):
        menu = QMenu()
        item = menu.addAction(_t('ConvertDialog', 'Browse...'))
        item.setData(('browse_action', ''))
        if len(self._path_list) > 0:
            menu.addSeparator()
            pathListMenu = QMenu(_t('ConvertDialog', 'Saved path list'))
            for p in self._path_list:
                item = pathListMenu.addAction(p)
                item.setData(('saved_path', p))
            menu.addMenu(pathListMenu)
        menu.addSeparator()
        item = menu.addAction(_t('ConvertDialog', 'Save current path in list'))
        item.setData(('save_action', ''))
        item = menu.addAction(_t('ConvertDialog', 'Delete current path from list'))
        item.setData(('delete_action', ''))
        
        action = menu.exec_(self.textOutputDir.mapToGlobal(QPoint(self.textOutputDir.width(), 0)))
        if action:
            element = action.data()

            if element[0] == 'browse_action':
                result = QFileDialog.getExistingDirectory(directory=self.textOutputDir.text())
                if result:
                    self.textOutputDir.setText(os.path.normpath(result))
            elif element[0] == 'saved_path':
                self.textOutputDir.setText(element[1])
            elif element[0] == 'save_action':
                if self.textOutputDir.text():
                    self._path_list.add(os.path.normpath(self.textOutputDir.text()))
            elif element[0] == 'delete_action':              
                    self._path_list.discard(os.path.normpath(self.textOutputDir.text()))

    def onTextFinalDirClick(self):
        menu = QMenu()
        item = menu.addAction(_t('ConvertDialog', 'Browse...'))
        item.setData(('browse_action', ''))
        if len(self._path_list_final_fb2) > 0:
            menu.addSeparator()
            pathListfinalfb2Menu = QMenu(_t('ConvertDialog', 'Saved path list'))
            for p in self._path_list_final_fb2:
                item = pathListfinalfb2Menu.addAction(p)
                item.setData(('saved_path', p))
            menu.addMenu(pathListfinalfb2Menu)
        menu.addSeparator()
        item = menu.addAction(_t('ConvertDialog', 'Save current path in list'))
        item.setData(('save_action', ''))
        item = menu.addAction(_t('ConvertDialog', 'Delete current path from list'))
        item.setData(('delete_action', ''))

        action = menu.exec_(self.textFinalDir.mapToGlobal(QPoint(self.textFinalDir.width(), 0)))
        if action:
            element = action.data()

            if element[0] == 'browse_action':
                result = QFileDialog.getExistingDirectory(directory=self.textFinalDir.text())
                if result:
                    self.textFinalDir.setText(os.path.normpath(result))
            elif element[0] == 'saved_path':
                self.textFinalDir.setText(element[1])
            elif element[0] == 'save_action':
                if self.textFinalDir.text():
                    self._path_list_final_fb2.add(os.path.normpath(self.textFinalDir.text()))
            elif element[0] == 'delete_action':
                self._path_list_final_fb2.discard(os.path.normpath(self.textFinalDir.text()))

    def accept(self):
        if self.outputPath:
            if not os.path.exists(self.outputPath):
                QMessageBox.critical(self,
                                     'Fb2Tool',
                                     _t('ConvertDialog', 'Folder "{0}" not exists').format(self.outputPath))
                return False
        else:
            QMessageBox.critical(self, 'Fb2Tool', _t('ConvertDialog', 'Output folder not specified'))
            return False

        if self.checkMoveToFinal.isChecked():
            if self.finalDir:
                if not os.path.exists(self.finalDir):
                    QMessageBox.critical(self,
                                         'Fb2Tool',
                                         _t('ConvertDialog', 'Folder "{0}" not exists').format(self.finalDir))
                    return False
            else:
                QMessageBox.critical(self, 'Fb2Tool', _t('ConvertDialog', 'Path to final folder not specified'))
                return False
        return super().accept()

    def onToolAuthorPattern(self):
        elements = {
            _t('ren', 'First name'): '#f',
            _t('ren', 'Middle name'): '#m',
            _t('ren', 'Last name'): '#l',
            _t('ren', 'Fist name initial'): '#fi',
            _t('ren', 'Middle name initial'): '#mi'
        }
        self.toolPatternMenu(elements, self.textAuthorPattern, self.toolAuthorPattern.mapToGlobal(QPoint(0, 0)))

    def onToolDirPattern(self):
        elements = {
            'Series': '#Series',
            'Author': '#Author',
        }
        self.toolPatternMenu(elements, self.textDirPattern, self.toolDirPattern.mapToGlobal(QPoint(0, 0)))

    def toolPatternMenu(self, elements, control, point):
        menu = QMenu()
        for key in elements:
            item = menu.addAction(key)
            item.setData(elements[key])
        action = menu.exec_(point)
        if action:
            element = action.data()
            text = control.text()
            if control.selectionStart() == -1:
                pos = control.cursorPosition()
                text = text[:pos] + element + text[pos:]
                control.setText(text)
                control.setCursorPosition(pos + len(element))
            else:
                start = control.selectionStart()
                end = control.selectionEnd()
                text = text[:start] + element + text[end:]
                control.setText(text)
                control.setCursorPosition(start + len(element))
