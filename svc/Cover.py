#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11-04-2014

@author: esanchez
'''
import json
import urllib2
import httplib2, re
import config
from model.bean import Capitulo, Manga, Imagen
from libs import log, funciones
import os

def obtenerCaratulas(manga = Manga):
    log.info("Obtener caratulas")
    if not manga.cover is None:
        dirName = crearDirectorioCaratula(manga)
        data = json.load(urllib2.urlopen(manga.cover))
        #print data["MUid"]
        if not "Error" in data:
            for cover in data["Covers"]["a"]:
            #print cover
                filename = '%s\\ v%s_%s.jpg'%(data["MUid"], funciones.prefijo(str(cover["Volume"]), 2), cover["Side"])
                descargarImagenCover(dirName, cover["Raw"], filename)
        else:
            log.error('%s => [%s] %s'% (manga.code, manga.id, data["Error"]))

def descargarImagenCover(folder, imgUrl, filename):
    filePath = '%s/%s' %(folder, filename)
    if(not os.path.isfile(filePath)): 
        log.info('curl %s -o %s/%s'%( imgUrl, folder, filename))
        os.system('curl %s -o %s/%s' % ( imgUrl, folder, filename)) 
    else:
        log.error('El archivo [%s] ya existe'% filename)
    
def crearDirectorioCaratula(manga = Manga):
    dirName = "%s%s/covers"%(config.CONST_PATH, manga.uCode)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        log.info("mkdir %s"%dirName)
    else:
        log.error("La carpeta [%s] ya exíste"%dirName)
    return dirName