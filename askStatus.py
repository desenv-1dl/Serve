# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QAction, QIcon
from PyQt4.QtCore import QVariant, QSize
from time import sleep
import json
import urllib2
    
class AskStatus(QtCore.QObject):
    '''classe para gerar trabalhos em plano de fundo'''
    finished = QtCore.pyqtSignal(dict)
    def __init__(self, url, parent=None):
        '''construtor'''
        super(AskStatus, self).__init__(parent)
        self.url = url
     
    def getStatus(self):
        '''função para pergutar status do serviço no servidor'''
        try:
            result = urllib2.Request(self.url)
            f = urllib2.urlopen(result)
            data = json.loads(f.read())  
            return data
        except:
            a = {'status': 'Erro plugin', 'log':''}
            return a 
    
    def run(self):       
        '''função para iniciar perguntas ao servidor em determinado periodo de tempo''' 
        for p in range(30):
            data = self.getStatus()
            if (data) and ((data['status'] == 'Executado') or (data['status'] == 'Erro') ):
                break
            sleep(10)
        self.finished.emit(data)
        
                  
