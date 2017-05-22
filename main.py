# -*- coding: utf-8 -*-

import sys, os
from qgis.core import QgsMapLayerRegistry, QgsMapLayer, QgsField, QGis
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QAction, QIcon
from PyQt4.QtCore import QVariant, QSize
from PyQt4 import QtGui, uic, QtCore
from interface import InterfaceFmeServer
import resources_rc

class Main:
    '''classe para ao iniciar o qgis adicionar o icon do plugin no barra de ferramentas '''
    def __init__(self, iface):
        '''construtor'''
        self.iface = iface
       
    def initGui(self):
        '''criar uma QAction para o plugin e adiciona na barra de ferramentas'''
        self.toolButton = QAction(QIcon(":/plugins/FmeServer/server.png"), u"FMEServer", self.iface.mainWindow())
        self.toolButton.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.toolButton)
        
    def unload(self):    
        '''remove da barra de ferramentas o QAction do plugin'''
        self.iface.removeToolBarIcon(self.toolButton)
            
    def run(self):
        '''inicializa a interface do plugin e desabilitar o QAction do plugin'''
        #try:
        dialog = QtGui.QDialog(self.iface.mainWindow())
        self.d = InterfaceFmeServer(self.iface, dialog)
        self.d.show()
        self.d.closeEvent = self.setEnabledToolButton
        self.toolButton.setEnabled(False)
        #except:
        #    self.setEnabledToolButton()
            
    def setEnabledToolButton(self, e=None):
        '''função para quando a interface do plugin for fechada habilitar o QAction do plugin'''
        self.toolButton.setEnabled(True)
   


   
    
    
    
