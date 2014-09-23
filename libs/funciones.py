#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib
import HTMLParser
from model import chapter

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def tryint(x):
    try:
        return int(x)
    except ValueError:
        return x

def ordenarLista(lst):
    listaAux = []
    
    return lst

def decode(texto):
    texto = texto.replace('\xc3\xad', 'í')
    texto = texto.replace('%C2%B7', '-')
    texto = texto.replace('\xc2\xb7', '-')
    return texto

#http://eshentaionline.com/Circunstancias-Familiares/02
def prefijo(nombre, largo = 0):
    dif = largo - len(nombre)
    prefijoNombre = ""
    if(dif > 0):
        for c in xrange(0, dif):
            prefijoNombre = "0%s"%prefijoNombre
    return '%s%s'%(prefijoNombre, nombre)

def existeURL(site, path):
    conn = httplib.HTTPConnection(site)
    conn.request('HEAD', path)
    response = conn.getresponse()
    conn.close()
    return response.status == 200

class VolumenHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.reset()
        self.VOLUMEN = []
        self.VALIDTAG = False   
        self.VALID_VOLUMEN = False
        self.VALID_CAPITULO = False
        self.INIT = False 
    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'chapterlistfull':
            #print '************************* Inicio listado de caps *******************************'
            self.INIT = True
        if not self.INIT:
            self.VALIDTAG = False
            return
        #print "<%s>%s"% (tag, attrs)
        if tag == 'li' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'volume':
            self.VALID_VOLUMEN = True 
            
        if tag == 'a' and len(attrs) > 1 and attrs[0][0] == 'href' and attrs[1][0] == 'id':
            self.VALID_CAPITULO = True         
        
        self.VALIDTAG = True        
    def handle_endtag(self, tag):
        if tag == 'li':
            self.VALID_VOLUMEN = False
        if tag == 'a':
            self.VALID_CAPITULO = False
        if not self.INIT:
            return
        #print "</%s>"%tag
        if tag == 'ul':
            self.INIT = False    
            #print '************************* Fin listado de caps *******************************'        
    def handle_data(self, data):
        if(not self.VALIDTAG):
            return
        if(self.VALID_VOLUMEN):
            volumen = chapter.Volumen(data, [])
            self.VOLUMEN.append(volumen)
        if self.VALID_CAPITULO :
            capitulo = chapter.Capitulo(data)
            volumen = self.VOLUMEN.pop()
            volumen.capitulos.append(capitulo)
            self.VOLUMEN.append(volumen)
        #print "%s"%data