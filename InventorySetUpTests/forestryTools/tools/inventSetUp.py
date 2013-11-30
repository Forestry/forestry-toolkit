# -*- coding: utf-8 -*-
#-----------------------------------------------------------
#
# fTools
# Copyright (C) xxx Abdoul Ousmane Dia
# EMAIL: dia.abdoul (at) gmail.com
# WEB : ----
#
# To be completed
#
#-----------------------------------------------------------
#
# licensed under the terms of GNU GPL 2
#
# To be completed
#
#---------------------------------------------------------------------

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
#from random import *

import math, ForestryFunctions
from ui_inventSetUp import Ui_inventSetUp

class Dialog(QDialog, Ui_inventSetUp):
    def __init__(self, iface):
        QDialog.__init__(self, iface.mainWindow())
        self.iface = iface
        self.setupUi(self)

        self.AddLayers()
        
        QObject.connect(self.BrowseCSV, SIGNAL("clicked()"), self.browse)
        QObject.connect(self.inputShape, SIGNAL("currentIndexChanged(QString)"), self.update)
	QObject.connect(self.joinFields, SIGNAL("clicked()"), self.Addjoin)
        
    
        self.setWindowTitle(self.tr("Join inventory data"))

    def AddLayers( self ):
        layers = ForestryFunctions.getLayerNames()
        self.inputShape.blockSignals(True)
        self.inputShape.clear()
        self.inputShape.blockSignals(False)
        self.inputShape.addItems(layers)



    # If input layer is changed, update field list
    def update(self, inputLayer):
        self.cmbFieldIn.clear()
        changedLayer = ForestryFunctions.getMapLayerByName(unicode(inputLayer))
        if changedLayer.type() == changedLayer.VectorLayer:
            changedLayer = ForestryFunctions.getVectorLayerByName(inputLayer)
            changedFields = ForestryFunctions.getFieldList(changedLayer)
            for f in changedFields:
            	self.cmbFieldIn.addItem(unicode(f.name()))
     
    #This function load csv file and get all fields and performs join action. 
    #I'm wodering whether I should keep this function?!

    def browse(self):
		#QMessageBox.information(None,"Test", "My browser")
		#ForestryFunctions.saveDialog()
	self.inputFileCSV.clear()
        ( self.shapefileName, self.encoding ) = ForestryFunctions.OpenDialog( self )
        if self.shapefileName is None or self.encoding is None:
            return
        self.inputFileCSV.setText( self.shapefileName )
	
	mFileName=self.inputFileCSV.text() #Keep reference on the csv file
	uri = mFileName+"?delimiter=%s&xField=%s&yField=%s" % (";", "x", "y")
	vlayer = QgsVectorLayer(uri, "Forest data", "delimitedtext")

	#Get fields and populate the combo box
	browsefields=ForestryFunctions.getFieldList(vlayer)
	for f in browsefields:
		self.cmbFieldTarget.addItem(unicode(f.name()))

	if vlayer.isValid():
		QgsMapLayerRegistry.instance().addMapLayer(vlayer)
		

#Joining vector layer to csv file
    def Addjoin(self):
	vlayer1 = ForestryFunctions.getMapLayerByName(unicode(self.inputShape.currentText()))
	vlayer2 = ForestryFunctions.getMapLayerByName(unicode(self.inputFileCSV.text()))
	#self.progressbar.setValue(0)
	ForestryFunctions.join(vlayer1,vlayer2,self.cmbFieldIn.currentText(),self.cmbFieldTarget.currentText())
	#self.progressbar.setValue(100)


#	ForestryFunctions.OpenDialog()
