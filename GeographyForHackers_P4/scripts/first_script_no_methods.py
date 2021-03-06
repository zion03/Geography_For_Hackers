"""
FirstScript: Chapter 7 exercise for GforH course on PyQGIS

# it is not best practice to import *
# instead, only import the methods and attributes you need
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from qgis.core import *
from qgis.utils import iface

wb = QgsVectorLayer('vector_file.shp', 'countries', 'ogr')
QgsMapLayerRegistry.instance().addMapLayer(wb)

active_layer = iface.activeLayer()
renderer = active_layer.rendererV2()
symbol = renderer.symbol()
symbol.setColor(QColor(Qt.red))
iface.mapCanvas().refresh()
iface.legendInterface().refreshLayerSymbology(active_layer)

iface.showAttributeTable(iface.activeLayer())
