# -*- coding: utf-8 -*-

from PyQt4 import QtGui, uic, QtCore
from styleSheet import *

class GeneratorTabs:
    '''classe para gerar abas'''
    def __init__(self, dataRoutine, tab):
        '''construtor'''
        self.data = dataRoutine
        self.tabWidget = tab
        self.categories = []
        self.setCategories()
        self.tabs = {}
        self.criarTab()
        
    def getTabs(self):
        '''função retorna todas as abas ligadas'''
        return self.tabs

    def getCategories(self):
        '''função retorna todas as categorias'''
        return self.categories
    
    def setCategories(self):
        '''função define todas as categorias'''
        for r in self.data:
            self.categories.append(r['categoria'])
             
    def criarTab(self):
        '''função criar todas as abas'''
        categories = list(set(self.getCategories()))
        for category in categories:
            tab = QtGui.QWidget()
            tab.setObjectName(unicode(category))
            verticalLayout_4 = QtGui.QVBoxLayout(tab)
            scrollArea = QtGui.QScrollArea(tab)
            scrollArea.setWidgetResizable(True)
            scrollAreaWidgetContents = QtGui.QWidget()
            verticalLayout_3 = QtGui.QVBoxLayout(scrollAreaWidgetContents)
            scrollArea.setWidget(scrollAreaWidgetContents)
            verticalLayout_4.addWidget(scrollArea)
            self.tabWidget.addTab(tab, unicode(""))
            self.tabWidget.setTabText(self.tabWidget.indexOf(tab), category)
            self.tabs[category]=[scrollAreaWidgetContents, verticalLayout_3, tab]            
        self.tabWidget.setCurrentIndex(0)    