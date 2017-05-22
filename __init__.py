# -*- coding: utf-8 -*-

from main import Main

def name():
    return "Servidor de Rotinas do FME"
def description():
    return "Possibilita Multiplos usuários rodarem rotinas do FME"
def version():
    return "Version 0.1"
def classFactory(iface):
    from main import Main
    return Main(iface)
def qgisMinimumVersion():
    return "2.0"
def author():
    return "Felipe Diniz"
def email():
    return "me@hotmail.com"
def icon():
    return "icon.png"
