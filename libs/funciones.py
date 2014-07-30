#!/usr/bin/env python
# -*- coding: utf-8 -*-
import httplib

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

