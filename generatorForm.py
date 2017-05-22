# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from qgis.utils import iface
from PyQt4.QtCore import QSettings
from styleSheet import *

class GeneratorForm:
	'''classe para gerar form'''
	def __init__(self, routine):
		'''construtor'''
		self.routine = routine
		self.data = {}
		self.le = []
		self.cb = []
		self.createForm()

	def createForm(self):
		'''função para criar o form'''
		routineAreaScroll = QtGui.QScrollArea()
		routineAreaScroll.setStyleSheet( unicode(routineAreaStyle))
		routineAreaScroll.setWidgetResizable(True)
		self.createLayout()
		routineAreaScroll.setWidget(self.routineWidget)
		routineAreaScroll.setVisible(False)
		self.layout = routineAreaScroll

	def createLayout(self):
		'''função para criar layout'''
		self.routineWidget = QtGui.QWidget()
		self.routineWidget.setGeometry(QtCore.QRect(0, 0, 337, 525))
		verticalLayout_2 = QtGui.QVBoxLayout(self.routineWidget)
		verticalLayout_2.addWidget(self.createLabelDescription(True))
		verticalLayout_2.addWidget(self.createLabelDescription())
		for f in self.routine['parametros']:
			verticalLayout_2.addLayout(self.createField(f))
		verticalLayout_2.addItem(self.createSpace())
		verticalLayout_2.addWidget(self.createStartButton())
		verticalLayout_2.addWidget(self.createProgress())

	def createLabelDescription(self, t=False):
		'''função para criar o campo da descrição'''
		label = QtGui.QLabel(self.routineWidget)
		label.setFixedWidth(400)
		if t:
			label.setStyleSheet( unicode(labelVersionStyle))
			label.setText(unicode(u'<br/>'+u'Versão  :  '+self.routine['versao']+u'<br/><br/>'))
		else:
			label.setStyleSheet( unicode(labelDescriptionStyle))
			label.setText(unicode(u'<br/>'+self.routine['descricao']+u'<br/><br/>'))
		self.description = label
		return label

	def createField(self, f):
		'''função para criar os campos de entrada para a rotina'''
		horizontalLayout = QtGui.QHBoxLayout()
		label = QtGui.QLabel(self.routineWidget)
		label.setStyleSheet(unicode(labelFieldStyle))
		label.setText(unicode(f['descricao']))
		label.setFixedWidth(80)
		horizontalLayout.addWidget(label)
		if f['nome'][:3] == 'db_':
			Edit = self.createComboField(f)
		else:
			Edit = self.createLineField(f)
		horizontalLayout.addWidget(Edit)
		return horizontalLayout
	
	def createComboField(self, f):
		'''função para criar a caixa de seleção'''
		Edit = QtGui.QComboBox(self.routineWidget)
		Edit.setStyleSheet(unicode(comboFieldStyle))
		Edit.setFixedWidth(250)
		Edit.setObjectName(unicode(f['nome']))
		self.addConnections(Edit)
		self.cb.append(Edit)
		return Edit
	
	def createLineField(self, f):
		'''função para criar a linha de texto'''
		Edit = QtGui.QLineEdit(self.routineWidget)
		Edit.setStyleSheet(unicode(lineEditFieldStyle))
		Edit.setFixedWidth(250)
		Edit.setObjectName(unicode(f['nome']))
		self.le.append(Edit)
		Edit.textEdited.connect(lambda:self.setDataForm(Edit))
		return Edit

	def cleanForm(self):
		'''função para limpar as linhas de texto do form'''
		for le in self.le:
			le.clear()
		self.data = {}

	def setDataForm(self, e ):
		'''função para definir os dados de entrada do form'''
		self.data[unicode(e.objectName())] = unicode(e.text())

	def getDataForm(self):
		'''função para obter os dados de entrada do form'''
		for cb in self.cb:
			self.data[unicode(cb.objectName())] = unicode(cb.currentText().replace(' ',''))
		return self.data

	def createSpace(self):
		'''função para criar um espaço para ajustar os campos dentro do form'''
		spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		return spacerItem 

	def createStartButton(self):
		'''função para criar o botão de "star"'''
		pushButton = QtGui.QPushButton(self.routineWidget)
		pushButton.setStyleSheet(unicode(buttonFormStyle))
		pushButton.setCheckable(True)
		pushButton.setAutoExclusive(False)
		pushButton.setText("INICIAR")
		self.button = pushButton
		return pushButton
		
	def createProgress(self):
		'''função para criar a barra de progresso'''
		progressBar = QtGui.QProgressBar(self.routineWidget)
		progressBar.setStyleSheet(unicode(progressBarStyle))
		progressBar.setRange(0,1)
		progressBar.setVisible(False)
		self.progress = progressBar
		return progressBar
	
	def getListConnections(self):
		'''função para obter as configurações do qgis contendo as conexões do usuário'''
		s = QSettings()
		s.beginGroup("PostgreSQL/connections")
		return s
			
	def addConnections(self, e):
		'''função para extrair as conexões do usuário das configurações e adicionar na caixa de seleção'''
		s = self.getListConnections()
		connects=['SELECIONE DB']
		for x in s.allKeys():
			if x[-9:] == "/username":
				c=x[:-9]+"/database"
				connects.append(s.value(c))
		e.addItems(connects)
		

