# -*- coding: utf-8 -*-
"""
/***************************************************************************
 forestryTools
                                 A QGIS plugin
 A collection of forestry analysis tools
                              -------------------
        begin                : 2013-11-18
        copyright            : (C) 2013 by Abdoul Ousmane Dia (OpenGeomatica), Lee Muller () and Tyler Mitchell ()
        email                : dia.abdoul@opengeomatica.ca
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *

# Initialize Qt resources from file resources.py
import resources_rc
import os.path, sys


# Set up current path, so that we know where to look for mudules
currentPath = os.path.dirname(__file__)
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/utils'))
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/tools'))

import inventSetUp #Loading the module interface here (file dialog)

class forestryTools:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)


        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'forestrytools_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


    def initGui(self):
        # Create action that will start plugin configuration
        #self.action = QAction(
        #    QIcon(":/plugins/forestrytools/icon.png"),
        #    u"Forestry tools", self.iface.mainWindow())
     
	# Create the menu and submenus
	self.ForestryTools = QMenu(QCoreApplication.translate("Forestry tools", "&Forestry tools"))
	self.InventSetUp = QAction(QCoreApplication.translate("Forestry tools", "Inventory setup"),self.iface.mainWindow())
	self.InventAnalysis = QAction(QCoreApplication.translate("Forestry tools", "Inventory analysis"), self.iface.mainWindow())

	# Add menues and submenus
	self.ForestryTools.addActions([self.InventSetUp, self.InventAnalysis])

	# Integrade plugin menu to Qgis Vector menu
	self.menu = self.iface.vectorMenu()
	self.menu.addMenu( self.ForestryTools )

	# Connecting menu items to the slots

	QObject.connect(self.InventSetUp, SIGNAL("triggered()"), self.execInventSetUp)
	QObject.connect(self.InventAnalysis, SIGNAL("triggered()"), self.execInventAnalysis)

   
	#Loads inventory setup dialog. This dialog set a join between selected points shapefile and csv containing inventory data

    def execInventSetUp(self):
    	ivs = inventSetUp.Dialog(self.iface) #instanciating the Dialog here
    	ivs.show()
    	ivs.exec_()

	#Loads inventory analysis dialog. This dialog executes several calculations according to available inventory data
    def execInventAnalysis(self):
		QMessageBox.information(None,"On going...","This module is being created")

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&forestryToolsPlugin", self.iface.action)

