import sys
from PyQt5.QtWidgets import QToolBar, QWidget, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize


def _icon(pixmap):
    icon = QIcon(pixmap)
    icon.addPixmap(pixmap, QIcon.Disabled)
    return icon


class MainToolbar(QToolBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.settingsPixmap = None
        self.savePixmap = None
        self.addPixmap = None
        self.folderPixmap = None
        self.renamePixmap = None
        self.convertPixmap = None

    def addSeparator(self):
        if sys.platform == 'win32':
            separator = QWidget(self)
            separator.setFixedWidth(4)
            self.addWidget(separator)

    def setCenterAlign(self):
        spacer1 = QWidget()
        spacer1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        spacer2 = QWidget()
        spacer2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        for action in self.actions():
            self.insertWidget(action, spacer1)
            break
        self.addWidget(spacer2)

    def setLargeIcons(self):
        self.settingsPixmap = QPixmap(':/toolbar/settings_30px.png')
        self.savePixmap = QPixmap(':/toolbar/save_30px.png')
        self.addPixmap = QPixmap(':/toolbar/add_file_30px.png')
        self.folderPixmap = QPixmap(':/toolbar/add_folder_30px.png')
        self.renamePixmap = QPixmap(':/toolbar/rename_30px.png')
        self.convertPixmap = QPixmap(':/toolbar/convert_30px.png')
       
        if sys.platform == 'win32':
            self.setIconSize(QSize(36, 36))
        else:
            self.setIconSize(QSize(28, 28))
        self.setIcons()

    def setSmallIcons(self):
        self.settingsPixmap = QPixmap(':/toolbar/settings_16px.png')
        self.savePixmap = QPixmap(':/toolbar/save_16px.png')
        self.addPixmap = QPixmap(':/toolbar/add_file_16px.png')
        self.folderPixmap = QPixmap(':/toolbar/add_folder_16px.png')
        self.renamePixmap = QPixmap(':/toolbar/rename_16px.png')
        self.convertPixmap = QPixmap(':/toolbar/convert_16px.png')
        if sys.platform == 'win32':
            self.setIconSize(QSize(26, 26))
        else:
            self.setIconSize(QSize(22, 22))
        self.setIcons()

    def setIcons(self):
        for action in self.actions():
            if action.objectName() == 'actionSettings':
                action.setIcon(_icon(self.settingsPixmap))
            elif action.objectName() == 'actionSave_metadata':
                action.setIcon(_icon(self.savePixmap))
            elif action.objectName() == 'actionAdd_file':
                action.setIcon(_icon(self.addPixmap))
            elif action.objectName() == 'actionAdd_folder':
                action.setIcon(_icon(self.folderPixmap))
            elif action.objectName() == 'actionRename':
                action.setIcon(_icon(self.renamePixmap))
            elif action.objectName() == 'actionConvert':
                action.setIcon(_icon(self.convertPixmap))
