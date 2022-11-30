import webbrowser
from PyQt5.QtWidgets import QDialog
from .aboutdialog_ui import Ui_AboutDialog

import version

class AboutDialog(QDialog, Ui_AboutDialog):
    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)
        self.labelName.setText('Fb2Tool v{0}'.format(version.version))
        self.adjustSize()
        
    def openLink(self, link):
        browser = webbrowser.get()
        browser.open_new_tab(link)