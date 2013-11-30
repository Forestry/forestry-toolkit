# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inventSetUp.ui'
#
# Created: Thu Nov 21 22:47:59 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_inventSetUp(object):
    def setupUi(self, inventSetUp):
        inventSetUp.setObjectName(_fromUtf8("inventSetUp"))
        inventSetUp.resize(372, 248)
        self.lab_cmbFieldIn = QtGui.QLabel(inventSetUp)
        self.lab_cmbFieldIn.setGeometry(QtCore.QRect(102, 64, 141, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_cmbFieldIn.sizePolicy().hasHeightForWidth())
        self.lab_cmbFieldIn.setSizePolicy(sizePolicy)
        self.lab_cmbFieldIn.setObjectName(_fromUtf8("lab_cmbFieldIn"))
        self.cmbFieldIn = QtGui.QComboBox(inventSetUp)
        self.cmbFieldIn.setEnabled(True)
        self.cmbFieldIn.setGeometry(QtCore.QRect(246, 60, 118, 27))
        self.cmbFieldIn.setObjectName(_fromUtf8("cmbFieldIn"))
        self.lab_inputFileCSV = QtGui.QLabel(inventSetUp)
        self.lab_inputFileCSV.setGeometry(QtCore.QRect(11, 90, 91, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_inputFileCSV.sizePolicy().hasHeightForWidth())
        self.lab_inputFileCSV.setSizePolicy(sizePolicy)
        self.lab_inputFileCSV.setObjectName(_fromUtf8("lab_inputFileCSV"))
        self.lab_inputShape = QtGui.QLabel(inventSetUp)
        self.lab_inputShape.setGeometry(QtCore.QRect(13, 7, 110, 17))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_inputShape.sizePolicy().hasHeightForWidth())
        self.lab_inputShape.setSizePolicy(sizePolicy)
        self.lab_inputShape.setObjectName(_fromUtf8("lab_inputShape"))
        self.lab_cmbFieldTarget = QtGui.QLabel(inventSetUp)
        self.lab_cmbFieldTarget.setGeometry(QtCore.QRect(110, 147, 131, 20))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lab_cmbFieldTarget.sizePolicy().hasHeightForWidth())
        self.lab_cmbFieldTarget.setSizePolicy(sizePolicy)
        self.lab_cmbFieldTarget.setObjectName(_fromUtf8("lab_cmbFieldTarget"))
        self.inputShape = QtGui.QComboBox(inventSetUp)
        self.inputShape.setGeometry(QtCore.QRect(10, 30, 355, 27))
        self.inputShape.setObjectName(_fromUtf8("inputShape"))
        self.cmbFieldTarget = QtGui.QComboBox(inventSetUp)
        self.cmbFieldTarget.setEnabled(True)
        self.cmbFieldTarget.setGeometry(QtCore.QRect(244, 143, 118, 27))
        self.cmbFieldTarget.setObjectName(_fromUtf8("cmbFieldTarget"))
        self.layoutWidget = QtGui.QWidget(inventSetUp)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 110, 351, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.csv_layout = QtGui.QHBoxLayout(self.layoutWidget)
        self.csv_layout.setMargin(0)
        self.csv_layout.setObjectName(_fromUtf8("csv_layout"))
        self.inputFileCSV = QtGui.QLineEdit(self.layoutWidget)
        self.inputFileCSV.setReadOnly(True)
        self.inputFileCSV.setObjectName(_fromUtf8("inputFileCSV"))
        self.csv_layout.addWidget(self.inputFileCSV)
        self.BrowseCSV = QtGui.QToolButton(self.layoutWidget)
        self.BrowseCSV.setObjectName(_fromUtf8("BrowseCSV"))
        self.csv_layout.addWidget(self.BrowseCSV)
        self.joinFields = QtGui.QPushButton(inventSetUp)
        self.joinFields.setGeometry(QtCore.QRect(160, 190, 98, 27))
        self.joinFields.setObjectName(_fromUtf8("joinFields"))
        self.cancel = QtGui.QPushButton(inventSetUp)
        self.cancel.setGeometry(QtCore.QRect(262, 190, 98, 27))
        self.cancel.setObjectName(_fromUtf8("cancel"))
        self.progressBar = QtGui.QProgressBar(inventSetUp)
        self.progressBar.setGeometry(QtCore.QRect(10, 192, 140, 25))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.lab_cmbFieldIn.setBuddy(self.cmbFieldIn)
        self.lab_inputFileCSV.setBuddy(self.inputFileCSV)
        self.lab_inputShape.setBuddy(self.inputShape)
        self.lab_cmbFieldTarget.setBuddy(self.cmbFieldTarget)

        self.retranslateUi(inventSetUp)
        self.cmbFieldIn.setCurrentIndex(-1)
        self.inputShape.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(inventSetUp)
        inventSetUp.setTabOrder(self.inputShape, self.cmbFieldIn)
        inventSetUp.setTabOrder(self.cmbFieldIn, self.BrowseCSV)
        inventSetUp.setTabOrder(self.BrowseCSV, self.cmbFieldTarget)
        inventSetUp.setTabOrder(self.cmbFieldTarget, self.cancel)
        inventSetUp.setTabOrder(self.cancel, self.joinFields)
        inventSetUp.setTabOrder(self.joinFields, self.inputFileCSV)

    def retranslateUi(self, inventSetUp):
        inventSetUp.setWindowTitle(_translate("inventSetUp", "Dialog", None))
        self.lab_cmbFieldIn.setText(_translate("inventSetUp", "Use input join field", None))
        self.lab_inputFileCSV.setText(_translate("inventSetUp", "Load CSV file", None))
        self.lab_inputShape.setText(_translate("inventSetUp", "Input shapefile", None))
        self.lab_cmbFieldTarget.setText(_translate("inventSetUp", "Use join target field", None))
        self.BrowseCSV.setText(_translate("inventSetUp", "Browse", None))
        self.joinFields.setText(_translate("inventSetUp", "&Join", None))
        self.cancel.setText(_translate("inventSetUp", "Cancel", None))

