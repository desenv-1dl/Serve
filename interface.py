# -*- coding: utf-8 -*-
import sys, os
import urllib2
import urllib
import json
from time import sleep
from PyQt4.QtCore import pyqtSlot, pyqtSignal
from PyQt4.QtGui import QAction, QIcon, QMessageBox
from PyQt4.QtCore import QVariant, QSize
from PyQt4 import QtGui, uic, QtCore
from generatorButton import GeneratorButton
from generatorTabs import GeneratorTabs
from askStatus import AskStatus
import resources_rc

sys.path.append(os.path.dirname(__file__))
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'interface.ui'), resource_suffix='_rc')

class InterfaceFmeServer(QtGui.QDialog, FORM_CLASS):
    '''classe para gerar a interface do plugin'''
    def __init__(self, iface, parent=None):
        '''construtor'''
        super(InterfaceFmeServer, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface
        self.sumOfFound = None
        self.listToSearch = {}
        self.lastRoutine = None
        self.url = 'http://10.25.163.20:3006/'
        data = self.get()
        self.configure(data)

    def configure(self, data):
        '''função inicia a criação e configuração dos objetos da interface'''
        self.searchLineEdit.returnPressed.connect(lambda:self.searchRoutine(self.searchLineEdit))
        self.searchLineEdit.textEdited.connect(lambda:self.restartSearch(self.searchLineEdit))
        totalData = data
        self.tabs = GeneratorTabs(totalData, self.categoryTabWidget)
        for r in totalData:
            self.createRoutine(r)
            
    def createRoutine(self, r):
        '''função cria os objetos necessário para cada rotina'''
        parent = self.tabs.getTabs()[unicode(r['categoria'])][0]
        routine = GeneratorButton(r, parent)
        self.tabs.getTabs()[unicode(r['categoria'])][1].addWidget(routine.getButton())
        self.verticalLayout1.addWidget(routine.getForm().layout)
        self.listToSearch[(r['nome'], r['descricao'],)] = routine
        routine.getButton().toggled.connect(lambda:self.setStartForm(routine))
        routine.getForm().button.toggled.connect(lambda:self.setStartRoutine(routine))

    def setStartRoutine(self, r):
        '''função configura a inicialização da rotina'''
        if r.getForm().button.isChecked():            
            self.startRoutine(r)           
        else:
            self.finishRoutine(r)           
    
    def blockInterface(self, r, b):
        '''função para bloquear a interface'''
        self.categoryTabWidget.setEnabled(not(b))
        r.getForm().layout.setEnabled(not(b))
  
    def startRoutine(self, r):
        '''função para iniciar rotina'''
        self.blockInterface(r, True)
        self.progressBar = r.getForm().progress
        self.progressBar.setVisible(True)
        r.getForm().button.setText('PROCESSANDO ...')    
        self.post(r)
        r.getForm().cleanForm()

    def finishRoutine(self, r):
        '''função para finalizar a rotina'''
        self.progressBar.setVisible(False)
        r.getForm().button.setText('START')        
        self.blockInterface(r, False)
    
    def setStartForm(self, r):
        '''função para abrir o form da rotina'''
        if (self.lastRoutine):
            self.lastRoutine.getForm().layout.setVisible(False)
            self.lastRoutine.getButton().setChecked(False)
            self.lastRoutine = None
        if r.getButton().isChecked():
            r.getForm().layout.setVisible(True)
            r.getButton().setChecked(True)
            self.lastRoutine = r 
        else:
            r.getForm().layout.setVisible(False)
            r.getButton().setChecked(False)
            self.lastRoutine = None
             
    def checkSearchTabs(self, b, data):
        for r in data:
            if b:
                self.categoryTabWidget.setTabText(self.categoryTabWidget.indexOf(self.tabs.getTabs()[r][2]), '%s (%i)'%(r, data[r]))
            else:
                self.categoryTabWidget.setTabText(self.categoryTabWidget.indexOf(self.tabs.getTabs()[r][2]), '%s '%(r))
                
    def setButtonsVisible(self, b):
        for r in self.listToSearch:
            if not(self.listToSearch[r].getButton().isVisible()):
                self.listToSearch[r].getButton().setVisible(b)  
                               
    def searchRoutine(self, le):
        '''função para pesquisar os botões pelos nomes'''
        self.setButtonsVisible(True)
        test = self.listToSearch.copy()
        if self.sumOfFound:
            self.checkSearchTabs(False, self.sumOfFound)
        self.sumOfFound = {}
        if (test) and (le.text() != ''):
            for r in self.listToSearch:
                if ((unicode(le.text()).lower() in unicode(r[0]).lower())) or ((unicode(le.text()).lower() in unicode(r[1]).lower())):
                    v = test.pop(r)
                    if not(v.getRoutine()['categoria'] in self.sumOfFound):
                        self.sumOfFound[v.getRoutine()['categoria']] = 1
                    else:
                        self.sumOfFound[v.getRoutine()['categoria']]+=1
            self.checkSearchTabs(True, self.sumOfFound)
            for r in test:
                test[r].getButton().setVisible(False) 
    
    def restartSearch(self, le):
        if self.sumOfFound:
            self.checkSearchTabs(False, self.sumOfFound)
        if not(le.text()):
            self.setButtonsVisible(True)
   
    def closeEvent(self, event):
        '''função para confirmar o fechamento da interface'''
        reply = QMessageBox.question(self, u"Aviso:", u'<font color=white>Tem certeza que deseja fechar? (Isso não cancelará a rotina do FME)<font/>',
                                      QMessageBox.Yes, QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def get(self):
        try:
            '''função para executar o GET no servidor'''
            proxy = urllib2.ProxyHandler({'http': 'http://syncro:senha1234@10.25.163.1:3128',
                                           'https': 'http://syncro:senha1234@10.25.163.1:3128'})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
            result = urllib2.Request(self.url+'workspaces/versions?last=true')
            f = urllib2.urlopen(result)
            data = json.loads(f.read())
            return data       
        except:
            QMessageBox.warning(self, u"ERRO:", u"<font color=red>Problema no servidor : Método 'GET'")
    
    def post(self, r):
        '''função para executar o POST no servidor'''
        try:
            self.currentRoutine = r
            DIC = { 'parametros' : r.getForm().getDataForm()}
            url = self.url+'workspaces/versions/'+unicode(r.getRoutine()['id'])+'/jobs'
            req = urllib2.Request(url)
            req.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(req, json.dumps(DIC))
            data = json.loads(response.read())
            self.startJobBackground((self.url+'jobs/'+data['jobid']))
        except:
            QMessageBox.warning(self, u"ERRO:", u"<font color=red>Problema no servidor : Método 'POST'")
     
    def message(self, d):
        QMessageBox.information(self, u"AVISO:", u"""<font color=white><pre>'STATUS' : %s<br>'LOG' : %s</pre>""" %(d['status'], d['log']))

          
    def jobFinished(self, d):
        '''função para finalizar trabalho em plano de fundo'''
        self.worker.deleteLater()
        self.thread.quit()
        self.thread.wait()
        self.thread.deleteLater()
        self.thread = None
        self.worker = None
        self.progressBar.setRange(0,1)
        self.progressBar.setValue(1)
        self.message(d)
        self.currentRoutine.getForm().button.toggle()
        
        
    def startJobBackground(self, url):
        '''função para iniciar trabalho em plano de fundo'''
        self.progressBar.setRange(0,0)
        thread = QtCore.QThread(self)
        worker = AskStatus(url)
        worker.moveToThread(thread)
        worker.finished.connect(self.jobFinished)
        thread.started.connect(worker.run)
        thread.start()        
        self.thread = thread
        self.worker = worker
