# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src\designer\set_status_markread.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SetMarkStatus(object):
    def setupUi(self, SetMarkStatus):
        SetMarkStatus.setObjectName("SetMarkStatus")
        SetMarkStatus.resize(346, 432)
        SetMarkStatus.setToolTip("")
        SetMarkStatus.setStatusTip("")
        SetMarkStatus.setWhatsThis("")
        SetMarkStatus.setAccessibleName("")
        SetMarkStatus.setAccessibleDescription("")
        self.verticalLayout = QtWidgets.QVBoxLayout(SetMarkStatus)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lblAuthor_st = QtWidgets.QLabel(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblAuthor_st.sizePolicy().hasHeightForWidth())
        self.lblAuthor_st.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lblAuthor_st.setFont(font)
        self.lblAuthor_st.setToolTip("")
        self.lblAuthor_st.setStatusTip("")
        self.lblAuthor_st.setWhatsThis("")
        self.lblAuthor_st.setAccessibleName("")
        self.lblAuthor_st.setAccessibleDescription("")
        self.lblAuthor_st.setText("Автор(ы):")
        self.lblAuthor_st.setObjectName("lblAuthor_st")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblAuthor_st)
        self.inpAuthor_st = QtWidgets.QLineEdit(SetMarkStatus)
        self.inpAuthor_st.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inpAuthor_st.setFont(font)
        self.inpAuthor_st.setToolTip("")
        self.inpAuthor_st.setStatusTip("")
        self.inpAuthor_st.setWhatsThis("")
        self.inpAuthor_st.setAccessibleName("")
        self.inpAuthor_st.setAccessibleDescription("")
        self.inpAuthor_st.setInputMask("")
        self.inpAuthor_st.setText("")
        self.inpAuthor_st.setObjectName("inpAuthor_st")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inpAuthor_st)
        self.lblTitle_st = QtWidgets.QLabel(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblTitle_st.sizePolicy().hasHeightForWidth())
        self.lblTitle_st.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblTitle_st.setFont(font)
        self.lblTitle_st.setToolTip("")
        self.lblTitle_st.setStatusTip("")
        self.lblTitle_st.setWhatsThis("")
        self.lblTitle_st.setAccessibleName("")
        self.lblTitle_st.setAccessibleDescription("")
        self.lblTitle_st.setText("Название:")
        self.lblTitle_st.setObjectName("lblTitle_st")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblTitle_st)
        self.inpTitle_st = QtWidgets.QLineEdit(SetMarkStatus)
        self.inpTitle_st.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inpTitle_st.setFont(font)
        self.inpTitle_st.setToolTip("")
        self.inpTitle_st.setStatusTip("")
        self.inpTitle_st.setWhatsThis("")
        self.inpTitle_st.setAccessibleName("")
        self.inpTitle_st.setAccessibleDescription("")
        self.inpTitle_st.setInputMask("")
        self.inpTitle_st.setText("")
        self.inpTitle_st.setObjectName("inpTitle_st")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.inpTitle_st)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnPrevios = QtWidgets.QPushButton(SetMarkStatus)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnPrevios.setFont(font)
        self.btnPrevios.setToolTip("")
        self.btnPrevios.setStatusTip("")
        self.btnPrevios.setWhatsThis("")
        self.btnPrevios.setAccessibleName("")
        self.btnPrevios.setAccessibleDescription("")
        self.btnPrevios.setText("Предыдущая")
        self.btnPrevios.setObjectName("btnPrevios")
        self.horizontalLayout.addWidget(self.btnPrevios)
        self.btnNext = QtWidgets.QPushButton(SetMarkStatus)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnNext.setFont(font)
        self.btnNext.setToolTip("")
        self.btnNext.setStatusTip("")
        self.btnNext.setWhatsThis("")
        self.btnNext.setAccessibleName("")
        self.btnNext.setAccessibleDescription("")
        self.btnNext.setText("Следующая")
        self.btnNext.setObjectName("btnNext")
        self.horizontalLayout.addWidget(self.btnNext)
        self.btnSetStatus = QtWidgets.QPushButton(SetMarkStatus)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSetStatus.setFont(font)
        self.btnSetStatus.setToolTip("")
        self.btnSetStatus.setStatusTip("")
        self.btnSetStatus.setWhatsThis("Отметить статус")
        self.btnSetStatus.setAccessibleName("")
        self.btnSetStatus.setAccessibleDescription("")
        self.btnSetStatus.setText("Отметить")
        self.btnSetStatus.setObjectName("btnSetStatus")
        self.horizontalLayout.addWidget(self.btnSetStatus)
        self.lblIcon = QtWidgets.QLabel(SetMarkStatus)
        self.lblIcon.setEnabled(False)
        self.lblIcon.setToolTip("")
        self.lblIcon.setStatusTip("")
        self.lblIcon.setWhatsThis("")
        self.lblIcon.setAccessibleName("")
        self.lblIcon.setAccessibleDescription("")
        self.lblIcon.setText("")
        self.lblIcon.setPixmap(QtGui.QPixmap(":/icons/set_status_16px.png"))
        self.lblIcon.setObjectName("lblIcon")
        self.horizontalLayout.addWidget(self.lblIcon)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(SetMarkStatus)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblStatus = QtWidgets.QLabel(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblStatus.sizePolicy().hasHeightForWidth())
        self.lblStatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblStatus.setFont(font)
        self.lblStatus.setToolTip("")
        self.lblStatus.setStatusTip("")
        self.lblStatus.setWhatsThis("")
        self.lblStatus.setAccessibleName("")
        self.lblStatus.setAccessibleDescription("")
        self.lblStatus.setText("Статус:")
        self.lblStatus.setObjectName("lblStatus")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblStatus)
        self.cmbStatus = QtWidgets.QComboBox(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbStatus.sizePolicy().hasHeightForWidth())
        self.cmbStatus.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbStatus.setFont(font)
        self.cmbStatus.setToolTip("")
        self.cmbStatus.setStatusTip("")
        self.cmbStatus.setWhatsThis("")
        self.cmbStatus.setAccessibleName("")
        self.cmbStatus.setAccessibleDescription("")
        self.cmbStatus.setObjectName("cmbStatus")
        self.cmbStatus.addItem("")
        self.cmbStatus.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cmbStatus)
        self.lblOperation = QtWidgets.QLabel(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblOperation.sizePolicy().hasHeightForWidth())
        self.lblOperation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblOperation.setFont(font)
        self.lblOperation.setToolTip("")
        self.lblOperation.setStatusTip("")
        self.lblOperation.setWhatsThis("")
        self.lblOperation.setAccessibleName("")
        self.lblOperation.setAccessibleDescription("")
        self.lblOperation.setText("Операция:")
        self.lblOperation.setObjectName("lblOperation")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblOperation)
        self.cmbOperation = QtWidgets.QComboBox(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbOperation.sizePolicy().hasHeightForWidth())
        self.cmbOperation.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cmbOperation.setFont(font)
        self.cmbOperation.setObjectName("cmbOperation")
        self.cmbOperation.addItem("")
        self.cmbOperation.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cmbOperation)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblCurrentDate = QtWidgets.QLabel(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblCurrentDate.sizePolicy().hasHeightForWidth())
        self.lblCurrentDate.setSizePolicy(sizePolicy)
        self.lblCurrentDate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblCurrentDate.setFont(font)
        self.lblCurrentDate.setToolTip("")
        self.lblCurrentDate.setStatusTip("")
        self.lblCurrentDate.setWhatsThis("")
        self.lblCurrentDate.setAccessibleName("")
        self.lblCurrentDate.setAccessibleDescription("")
        self.lblCurrentDate.setText("Выбранная дата:")
        self.lblCurrentDate.setObjectName("lblCurrentDate")
        self.horizontalLayout_2.addWidget(self.lblCurrentDate)
        self.inpDate = QtWidgets.QLineEdit(SetMarkStatus)
        self.inpDate.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.inpDate.setFont(font)
        self.inpDate.setToolTip("")
        self.inpDate.setStatusTip("")
        self.inpDate.setWhatsThis("")
        self.inpDate.setAccessibleName("")
        self.inpDate.setAccessibleDescription("")
        self.inpDate.setInputMask("")
        self.inpDate.setText("")
        self.inpDate.setObjectName("inpDate")
        self.horizontalLayout_2.addWidget(self.inpDate)
        self.btnCalendVis = QtWidgets.QToolButton(SetMarkStatus)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnCalendVis.setFont(font)
        self.btnCalendVis.setToolTip("")
        self.btnCalendVis.setStatusTip("")
        self.btnCalendVis.setWhatsThis("")
        self.btnCalendVis.setAccessibleName("")
        self.btnCalendVis.setText("▼")
        self.btnCalendVis.setObjectName("btnCalendVis")
        self.horizontalLayout_2.addWidget(self.btnCalendVis)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.calendarWidget = QtWidgets.QCalendarWidget(SetMarkStatus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.calendarWidget.setFont(font)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(SetMarkStatus)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SetMarkStatus)
        self.buttonBox.accepted.connect(SetMarkStatus.accept) # type: ignore
        self.buttonBox.rejected.connect(SetMarkStatus.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SetMarkStatus)

    def retranslateUi(self, SetMarkStatus):
        _translate = QtCore.QCoreApplication.translate
        SetMarkStatus.setWindowTitle(_translate("SetMarkStatus", "Dialog"))
        self.cmbStatus.setItemText(0, _translate("SetMarkStatus", "Начал"))
        self.cmbStatus.setItemText(1, _translate("SetMarkStatus", "Закончил"))
        self.cmbOperation.setItemText(0, _translate("SetMarkStatus", "Читать"))
        self.cmbOperation.setItemText(1, _translate("SetMarkStatus", "Слушать"))
from . import resources_mark_rc
