# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\designer\setting_markread.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_mark(object):
    def setupUi(self, settings_mark):
        settings_mark.setObjectName("settings_mark")
        settings_mark.resize(600, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(settings_mark.sizePolicy().hasHeightForWidth())
        settings_mark.setSizePolicy(sizePolicy)
        settings_mark.setMinimumSize(QtCore.QSize(600, 370))
        settings_mark.setMaximumSize(QtCore.QSize(600, 370))
        settings_mark.setWindowTitle("Настройки MarkRead")
        settings_mark.setToolTip("")
        settings_mark.setStatusTip("")
        settings_mark.setWhatsThis("")
        settings_mark.setAccessibleName("")
        settings_mark.setAccessibleDescription("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(settings_mark)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblBases = QtWidgets.QLabel(settings_mark)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblBases.sizePolicy().hasHeightForWidth())
        self.lblBases.setSizePolicy(sizePolicy)
        self.lblBases.setMinimumSize(QtCore.QSize(175, 20))
        self.lblBases.setMaximumSize(QtCore.QSize(175, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblBases.setFont(font)
        self.lblBases.setText("Настройка путей к базам")
        self.lblBases.setObjectName("lblBases")
        self.verticalLayout.addWidget(self.lblBases)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkMyhomelib = QtWidgets.QCheckBox(settings_mark)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkMyhomelib.setFont(font)
        self.checkMyhomelib.setToolTip("")
        self.checkMyhomelib.setStatusTip("")
        self.checkMyhomelib.setWhatsThis("")
        self.checkMyhomelib.setAccessibleName("")
        self.checkMyhomelib.setAccessibleDescription("")
        self.checkMyhomelib.setText("MyHomeLib")
        self.checkMyhomelib.setObjectName("checkMyhomelib")
        self.gridLayout.addWidget(self.checkMyhomelib, 0, 0, 1, 1)
        self.inpMyhomelib = QtWidgets.QLineEdit(settings_mark)
        self.inpMyhomelib.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inpMyhomelib.setFont(font)
        self.inpMyhomelib.setToolTip("")
        self.inpMyhomelib.setStatusTip("")
        self.inpMyhomelib.setWhatsThis("")
        self.inpMyhomelib.setAccessibleName("")
        self.inpMyhomelib.setAccessibleDescription("")
        self.inpMyhomelib.setText("")
        self.inpMyhomelib.setObjectName("inpMyhomelib")
        self.gridLayout.addWidget(self.inpMyhomelib, 0, 1, 1, 1)
        self.toolMyhomelib = QtWidgets.QToolButton(settings_mark)
        self.toolMyhomelib.setEnabled(False)
        self.toolMyhomelib.setToolTip("")
        self.toolMyhomelib.setStatusTip("")
        self.toolMyhomelib.setWhatsThis("")
        self.toolMyhomelib.setAccessibleName("")
        self.toolMyhomelib.setAccessibleDescription("")
        self.toolMyhomelib.setText("...")
        self.toolMyhomelib.setObjectName("toolMyhomelib")
        self.gridLayout.addWidget(self.toolMyhomelib, 0, 2, 1, 1)
        self.checkCalibre = QtWidgets.QCheckBox(settings_mark)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkCalibre.setFont(font)
        self.checkCalibre.setToolTip("")
        self.checkCalibre.setStatusTip("")
        self.checkCalibre.setWhatsThis("")
        self.checkCalibre.setAccessibleName("")
        self.checkCalibre.setAccessibleDescription("")
        self.checkCalibre.setText("Calibre")
        self.checkCalibre.setObjectName("checkCalibre")
        self.gridLayout.addWidget(self.checkCalibre, 1, 0, 1, 1)
        self.inpCalibre = QtWidgets.QLineEdit(settings_mark)
        self.inpCalibre.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inpCalibre.setFont(font)
        self.inpCalibre.setToolTip("")
        self.inpCalibre.setStatusTip("")
        self.inpCalibre.setWhatsThis("")
        self.inpCalibre.setAccessibleName("")
        self.inpCalibre.setAccessibleDescription("")
        self.inpCalibre.setText("")
        self.inpCalibre.setObjectName("inpCalibre")
        self.gridLayout.addWidget(self.inpCalibre, 1, 1, 1, 1)
        self.toolCalibre = QtWidgets.QToolButton(settings_mark)
        self.toolCalibre.setEnabled(False)
        self.toolCalibre.setToolTip("")
        self.toolCalibre.setStatusTip("")
        self.toolCalibre.setWhatsThis("")
        self.toolCalibre.setAccessibleName("")
        self.toolCalibre.setAccessibleDescription("")
        self.toolCalibre.setText("...")
        self.toolCalibre.setObjectName("toolCalibre")
        self.gridLayout.addWidget(self.toolCalibre, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(settings_mark)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.lblQuery = QtWidgets.QLabel(settings_mark)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblQuery.sizePolicy().hasHeightForWidth())
        self.lblQuery.setSizePolicy(sizePolicy)
        self.lblQuery.setMinimumSize(QtCore.QSize(200, 20))
        self.lblQuery.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lblQuery.setFont(font)
        self.lblQuery.setToolTip("")
        self.lblQuery.setStatusTip("")
        self.lblQuery.setWhatsThis("")
        self.lblQuery.setAccessibleName("")
        self.lblQuery.setAccessibleDescription("")
        self.lblQuery.setText("Настройка запросов к базам")
        self.lblQuery.setObjectName("lblQuery")
        self.verticalLayout.addWidget(self.lblQuery)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblBaseSearch = QtWidgets.QLabel(settings_mark)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblBaseSearch.sizePolicy().hasHeightForWidth())
        self.lblBaseSearch.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblBaseSearch.setFont(font)
        self.lblBaseSearch.setToolTip("")
        self.lblBaseSearch.setStatusTip("")
        self.lblBaseSearch.setWhatsThis("")
        self.lblBaseSearch.setAccessibleName("")
        self.lblBaseSearch.setAccessibleDescription("")
        self.lblBaseSearch.setText("База для поиска")
        self.lblBaseSearch.setObjectName("lblBaseSearch")
        self.horizontalLayout.addWidget(self.lblBaseSearch)
        self.cmbBases = QtWidgets.QComboBox(settings_mark)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbBases.sizePolicy().hasHeightForWidth())
        self.cmbBases.setSizePolicy(sizePolicy)
        self.cmbBases.setMinimumSize(QtCore.QSize(100, 20))
        self.cmbBases.setMaximumSize(QtCore.QSize(100, 20))
        self.cmbBases.setToolTip("")
        self.cmbBases.setStatusTip("")
        self.cmbBases.setWhatsThis("")
        self.cmbBases.setAccessibleName("")
        self.cmbBases.setAccessibleDescription("")
        self.cmbBases.setCurrentText("")
        self.cmbBases.setObjectName("cmbBases")
        self.horizontalLayout.addWidget(self.cmbBases)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblQuerySearch = QtWidgets.QLabel(settings_mark)
        self.lblQuerySearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblQuerySearch.sizePolicy().hasHeightForWidth())
        self.lblQuerySearch.setSizePolicy(sizePolicy)
        self.lblQuerySearch.setMinimumSize(QtCore.QSize(100, 45))
        self.lblQuerySearch.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblQuerySearch.setFont(font)
        self.lblQuerySearch.setToolTip("")
        self.lblQuerySearch.setStatusTip("")
        self.lblQuerySearch.setWhatsThis("")
        self.lblQuerySearch.setAccessibleName("")
        self.lblQuerySearch.setAccessibleDescription("")
        self.lblQuerySearch.setText("Поисковый запрос")
        self.lblQuerySearch.setWordWrap(True)
        self.lblQuerySearch.setObjectName("lblQuerySearch")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblQuerySearch)
        self.textQuerySearch = QtWidgets.QTextEdit(settings_mark)
        self.textQuerySearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textQuerySearch.sizePolicy().hasHeightForWidth())
        self.textQuerySearch.setSizePolicy(sizePolicy)
        self.textQuerySearch.setMinimumSize(QtCore.QSize(472, 45))
        self.textQuerySearch.setMaximumSize(QtCore.QSize(472, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textQuerySearch.setFont(font)
        self.textQuerySearch.setToolTip("")
        self.textQuerySearch.setStatusTip("")
        self.textQuerySearch.setWhatsThis("")
        self.textQuerySearch.setAccessibleName("")
        self.textQuerySearch.setAccessibleDescription("")
        self.textQuerySearch.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textQuerySearch.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textQuerySearch.setObjectName("textQuerySearch")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textQuerySearch)
        self.lblQueryMarkMyhomelib = QtWidgets.QLabel(settings_mark)
        self.lblQueryMarkMyhomelib.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblQueryMarkMyhomelib.sizePolicy().hasHeightForWidth())
        self.lblQueryMarkMyhomelib.setSizePolicy(sizePolicy)
        self.lblQueryMarkMyhomelib.setMinimumSize(QtCore.QSize(100, 45))
        self.lblQueryMarkMyhomelib.setMaximumSize(QtCore.QSize(100, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblQueryMarkMyhomelib.setFont(font)
        self.lblQueryMarkMyhomelib.setToolTip("")
        self.lblQueryMarkMyhomelib.setStatusTip("")
        self.lblQueryMarkMyhomelib.setWhatsThis("")
        self.lblQueryMarkMyhomelib.setAccessibleName("")
        self.lblQueryMarkMyhomelib.setAccessibleDescription("")
        self.lblQueryMarkMyhomelib.setText("Для отметки в MyHomeLib")
        self.lblQueryMarkMyhomelib.setScaledContents(False)
        self.lblQueryMarkMyhomelib.setWordWrap(True)
        self.lblQueryMarkMyhomelib.setObjectName("lblQueryMarkMyhomelib")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblQueryMarkMyhomelib)
        self.textQueryMarkMyhomelib = QtWidgets.QTextEdit(settings_mark)
        self.textQueryMarkMyhomelib.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textQueryMarkMyhomelib.sizePolicy().hasHeightForWidth())
        self.textQueryMarkMyhomelib.setSizePolicy(sizePolicy)
        self.textQueryMarkMyhomelib.setMinimumSize(QtCore.QSize(472, 45))
        self.textQueryMarkMyhomelib.setMaximumSize(QtCore.QSize(472, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textQueryMarkMyhomelib.setFont(font)
        self.textQueryMarkMyhomelib.setToolTip("")
        self.textQueryMarkMyhomelib.setStatusTip("")
        self.textQueryMarkMyhomelib.setWhatsThis("")
        self.textQueryMarkMyhomelib.setAccessibleName("")
        self.textQueryMarkMyhomelib.setAccessibleDescription("")
        self.textQueryMarkMyhomelib.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textQueryMarkMyhomelib.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textQueryMarkMyhomelib.setObjectName("textQueryMarkMyhomelib")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textQueryMarkMyhomelib)
        self.lblQueryMarkCalibre = QtWidgets.QLabel(settings_mark)
        self.lblQueryMarkCalibre.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblQueryMarkCalibre.sizePolicy().hasHeightForWidth())
        self.lblQueryMarkCalibre.setSizePolicy(sizePolicy)
        self.lblQueryMarkCalibre.setMinimumSize(QtCore.QSize(100, 75))
        self.lblQueryMarkCalibre.setMaximumSize(QtCore.QSize(100, 75))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblQueryMarkCalibre.setFont(font)
        self.lblQueryMarkCalibre.setToolTip("")
        self.lblQueryMarkCalibre.setStatusTip("")
        self.lblQueryMarkCalibre.setWhatsThis("")
        self.lblQueryMarkCalibre.setAccessibleName("")
        self.lblQueryMarkCalibre.setAccessibleDescription("")
        self.lblQueryMarkCalibre.setText("Query for mark in Calibre")
        self.lblQueryMarkCalibre.setWordWrap(True)
        self.lblQueryMarkCalibre.setObjectName("lblQueryMarkCalibre")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblQueryMarkCalibre)
        self.groupCalibre = QtWidgets.QStackedWidget(settings_mark)
        self.groupCalibre.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupCalibre.sizePolicy().hasHeightForWidth())
        self.groupCalibre.setSizePolicy(sizePolicy)
        self.groupCalibre.setMinimumSize(QtCore.QSize(472, 75))
        self.groupCalibre.setMaximumSize(QtCore.QSize(472, 75))
        self.groupCalibre.setToolTip("")
        self.groupCalibre.setStatusTip("")
        self.groupCalibre.setWhatsThis("")
        self.groupCalibre.setAccessibleName("")
        self.groupCalibre.setAccessibleDescription("")
        self.groupCalibre.setAutoFillBackground(False)
        self.groupCalibre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.groupCalibre.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.groupCalibre.setObjectName("groupCalibre")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textQueryMarkCalibre1 = QtWidgets.QTextEdit(self.page)
        self.textQueryMarkCalibre1.setEnabled(False)
        self.textQueryMarkCalibre1.setGeometry(QtCore.QRect(0, 27, 470, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textQueryMarkCalibre1.sizePolicy().hasHeightForWidth())
        self.textQueryMarkCalibre1.setSizePolicy(sizePolicy)
        self.textQueryMarkCalibre1.setMinimumSize(QtCore.QSize(470, 45))
        self.textQueryMarkCalibre1.setMaximumSize(QtCore.QSize(470, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textQueryMarkCalibre1.setFont(font)
        self.textQueryMarkCalibre1.setToolTip("")
        self.textQueryMarkCalibre1.setStatusTip("")
        self.textQueryMarkCalibre1.setWhatsThis("")
        self.textQueryMarkCalibre1.setAccessibleName("")
        self.textQueryMarkCalibre1.setAccessibleDescription("")
        self.textQueryMarkCalibre1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textQueryMarkCalibre1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textQueryMarkCalibre1.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textQueryMarkCalibre1.setObjectName("textQueryMarkCalibre1")
        self.lblFirstQueryCalibre = QtWidgets.QLabel(self.page)
        self.lblFirstQueryCalibre.setEnabled(False)
        self.lblFirstQueryCalibre.setGeometry(QtCore.QRect(5, 5, 90, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(90)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.lblFirstQueryCalibre.sizePolicy().hasHeightForWidth())
        self.lblFirstQueryCalibre.setSizePolicy(sizePolicy)
        self.lblFirstQueryCalibre.setMinimumSize(QtCore.QSize(90, 20))
        self.lblFirstQueryCalibre.setToolTip("")
        self.lblFirstQueryCalibre.setStatusTip("")
        self.lblFirstQueryCalibre.setWhatsThis("")
        self.lblFirstQueryCalibre.setAccessibleName("")
        self.lblFirstQueryCalibre.setAccessibleDescription("")
        self.lblFirstQueryCalibre.setText("Первый запрос")
        self.lblFirstQueryCalibre.setObjectName("lblFirstQueryCalibre")
        self.tootNextTab = QtWidgets.QToolButton(self.page)
        self.tootNextTab.setGeometry(QtCore.QRect(100, 5, 20, 20))
        self.tootNextTab.setToolTip("")
        self.tootNextTab.setStatusTip("")
        self.tootNextTab.setWhatsThis("")
        self.tootNextTab.setAccessibleName("")
        self.tootNextTab.setAccessibleDescription("")
        self.tootNextTab.setText("->")
        self.tootNextTab.setObjectName("tootNextTab")
        self.groupCalibre.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textQueryMarkCalibre2 = QtWidgets.QTextEdit(self.page_2)
        self.textQueryMarkCalibre2.setEnabled(False)
        self.textQueryMarkCalibre2.setGeometry(QtCore.QRect(0, 25, 470, 45))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textQueryMarkCalibre2.sizePolicy().hasHeightForWidth())
        self.textQueryMarkCalibre2.setSizePolicy(sizePolicy)
        self.textQueryMarkCalibre2.setMinimumSize(QtCore.QSize(470, 45))
        self.textQueryMarkCalibre2.setMaximumSize(QtCore.QSize(470, 45))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textQueryMarkCalibre2.setFont(font)
        self.textQueryMarkCalibre2.setToolTip("")
        self.textQueryMarkCalibre2.setStatusTip("")
        self.textQueryMarkCalibre2.setWhatsThis("")
        self.textQueryMarkCalibre2.setAccessibleName("")
        self.textQueryMarkCalibre2.setAccessibleDescription("")
        self.textQueryMarkCalibre2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textQueryMarkCalibre2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textQueryMarkCalibre2.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>")
        self.textQueryMarkCalibre2.setObjectName("textQueryMarkCalibre2")
        self.lblSecondQueryCalibre = QtWidgets.QLabel(self.page_2)
        self.lblSecondQueryCalibre.setEnabled(False)
        self.lblSecondQueryCalibre.setGeometry(QtCore.QRect(5, 5, 90, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(90)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.lblSecondQueryCalibre.sizePolicy().hasHeightForWidth())
        self.lblSecondQueryCalibre.setSizePolicy(sizePolicy)
        self.lblSecondQueryCalibre.setMinimumSize(QtCore.QSize(90, 20))
        self.lblSecondQueryCalibre.setToolTip("")
        self.lblSecondQueryCalibre.setStatusTip("")
        self.lblSecondQueryCalibre.setWhatsThis("")
        self.lblSecondQueryCalibre.setAccessibleName("")
        self.lblSecondQueryCalibre.setAccessibleDescription("")
        self.lblSecondQueryCalibre.setText("Второй запрос")
        self.lblSecondQueryCalibre.setObjectName("lblSecondQueryCalibre")
        self.tootPreviosTab = QtWidgets.QToolButton(self.page_2)
        self.tootPreviosTab.setGeometry(QtCore.QRect(100, 5, 20, 20))
        self.tootPreviosTab.setToolTip("")
        self.tootPreviosTab.setStatusTip("")
        self.tootPreviosTab.setWhatsThis("")
        self.tootPreviosTab.setAccessibleName("")
        self.tootPreviosTab.setAccessibleDescription("")
        self.tootPreviosTab.setText("<-")
        self.tootPreviosTab.setObjectName("tootPreviosTab")
        self.groupCalibre.addWidget(self.page_2)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.groupCalibre)
        self.verticalLayout.addLayout(self.formLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(settings_mark)
        self.buttonBox.setToolTip("")
        self.buttonBox.setStatusTip("")
        self.buttonBox.setWhatsThis("")
        self.buttonBox.setAccessibleName("")
        self.buttonBox.setAccessibleDescription("")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_3.addWidget(self.buttonBox)

        self.retranslateUi(settings_mark)
        self.groupCalibre.setCurrentIndex(1)
        self.buttonBox.accepted.connect(settings_mark.accept) # type: ignore
        self.buttonBox.rejected.connect(settings_mark.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(settings_mark)

    def retranslateUi(self, settings_mark):
        pass
