# -*- coding: utf-8 -*-

#-----------------------------------------------------------
#
# ForestryTools
# Copyright (C) 2013 Abdoul O. Dia
# EMAIL: dia.abdoul (at) gmail.com
# WEB : -----
#
# A collection of forestry functions
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
from qgis.gui import *


import locale

# Return list of names of all layers in QgsMapLayerRegistry
def getLayerNames( ):
    layermap = QgsMapLayerRegistry.instance().mapLayers()
    layerlist = []
    for name, layer in layermap.iteritems():
       layerlist.append( layer.name() )
    return sorted( layerlist, cmp=locale.strcoll )

# Return list of names of all fields from input QgsVectorLayer
def getFieldNames( vlayer ):
    fieldmap = getFieldList( vlayer )
    fieldlist = []
    for field in fieldmap:
        if not field.name() in fieldlist:
            fieldlist.append( field.name() )
    return sorted( fieldlist, cmp=locale.strcoll )

# Return QgsVectorLayer from a layer name ( as string )
def getVectorLayerByName( myName ):
    layermap = QgsMapLayerRegistry.instance().mapLayers()
    for name, layer in layermap.iteritems():
        if layer.type() == QgsMapLayer.VectorLayer and layer.name() == myName:
            if layer.isValid():
                return layer
            else:
                return None

# Return QgsMapLayer from a layer name ( as string )
def getMapLayerByName( myName ):
    layermap = QgsMapLayerRegistry.instance().mapLayers()
    for name, layer in layermap.iteritems():
        if layer.name() == myName:
            if layer.isValid():
                return layer
            else:
                return None

# Return the field list of a vector layer
def getFieldList( vlayer ):
    return vlayer.dataProvider().fields()

# Open Dialog and select a csv file
def OpenDialog( parent, filtering="CSV files (*.csv *.CSV)"):
    settings = QSettings()
    dirName = settings.value( "/lastShapefileDir" )
    encode = settings.value( "/encoding" )
    fileDialog = QgsEncodingFileDialog( parent, "Open csv file", dirName, filtering, encode )
    fileDialog.setDefaultSuffix( "csv" )
    fileDialog.setFileMode( QFileDialog.AnyFile )
    fileDialog.setAcceptMode( QFileDialog.AcceptOpen )
    fileDialog.setConfirmOverwrite( True )
    if not fileDialog.exec_() == QDialog.Accepted:
            return None, None
    files = fileDialog.selectedFiles()
    settings.setValue("/UI/lastShapefileDir", QFileInfo( unicode( files[0] ) ).absolutePath() )
    return ( unicode( files[0] ), unicode( fileDialog.encoding() ) )



def join(vlayer1,vlayer2,fieldSource,fieldTarget):
	#vector1 = QgsVectorLayer("path to dbf file", "test1", "ogr")
	id1 = vlayer1.id()
	#vector2 = QgsVectorLayer("path to shapefile", "test2", "ogr")
	id2 = vlayer1.id()
	#print id2
	#QgsMapLayerRegistry.instance().addMapLayer(vector1)
	#QgsMapLayerRegistry.instance().addMapLayer(vector2)
	info = QgsVectorJoinInfo()
	
	info.joinFieldIndex = vlayer1.fieldNameIndex(fieldSource)
	info.joinLayerId = id1
	info.targetFieldIndex = vlayer2.fieldNameIndex(fieldTarget)
	info.targetFieldName = QString(u(fieldTarget))
	info.memoryCache = True
	#print info.joinFieldIndex #All the following show the correct values
	#print info.joinFieldName
	#print info.joinLayerId
	#print info.targetFieldIndex
	#print info.targetFieldName
	print info.memoryCache
	QgsMapLayerRegistry.instance().mapLayer(id2).addJoin(info)
