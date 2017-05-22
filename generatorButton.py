# -*- coding: utf-8 -*-
from PyQt4 import QtGui, uic, QtCore
from generatorForm import GeneratorForm
from styleSheet import *

class GeneratorButton:
    '''classe para gerar um botão para cada rotina'''
    def __init__(self, routine, parent):
        '''construtor'''
        self.parent = parent
        self.setRoutine(routine)
        self.setForm(GeneratorForm(routine))
        self.createButton()
           
    def setRoutine(self, r):
        '''função para definir o dicionário com todos os dados da rotina'''
        self.routine = r
        
    def setForm(self, f):
        '''função para definir o generatorForm'''
        self.form = f
    
    def getForm(self):
        '''função para obter o generatorForm'''
        return self.form

    def getRoutine(self):
        '''função para obter o dicionário com todo os dados da rotina'''
        return self.routine
    
    def getButton(self):
        '''função para obter o botão da rotina'''
        return self.pushButton
      
    def createButton(self):
        '''função para criar o botão da rotina'''
        pushButton = QtGui.QPushButton(self.parent)
        pushButton.setObjectName(unicode(self.routine['categoria']))
        pushButton.setStyleSheet(unicode(buttonRoutineStyle))
        pushButton.setText(unicode(self.routine['nome']))
        pushButton.setCheckable(True)
        self.pushButton = pushButton 
        
