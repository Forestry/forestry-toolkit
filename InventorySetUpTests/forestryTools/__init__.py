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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load forestryTools class from file forestryTools
    from forestrytools import forestryTools
    return forestryTools(iface)
