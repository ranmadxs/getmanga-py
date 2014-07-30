#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 11-04-2014

@author: esanchez
'''
import httplib2, re
import config
from model.bean import Capitulo, Manga, Imagen
from libs import log
import os

def obtenerCaratulas(manga = Manga):
    log.info("Obtener caratulas")
    if not manga.cover is None:
        dirName = crearDirectorioCaratula(manga)
        pat = re.compile('<a href="(.+?)" title="(.+?)">')
        http = httplib2.Http()
        headers, body = http.request(manga.cover)
        li = pat.findall(body)
        for elem in li:
            log.debug("%s (%s)" %( elem[1], elem[0]))
            headers, body = http.request(elem[0])    
            rex = re.compile(r'<div class="raw_links clear">(.*?)<div class="block" id="unsorted" style="margin-top:5px;padding-top:10px;text-align:center;">',re.S|re.M)
            match = rex.findall(body)                
            pat = re.compile('<a href="(.+?)">')
            imagenes = pat.findall(match[0])
            for img in imagenes:                
                descargarImagenCover(dirName, img)

def descargarImagenCover(folder, imgUrl):
    filename = imgUrl.split("/")[-1]
    filePath = '%s/%s' %(folder, filename)
    if(not os.path.isfile(filePath)):
        imgRealUrl = imgUrl.replace(' ', '\ ')
        os.system('wget %s -P %s' % (imgRealUrl, folder))
        log.info('wget %s -P %s'%( imgRealUrl, folder))
    else:
        log.error('El archivo [%s] ya existe'% filename)
    
def crearDirectorioCaratula(manga = Manga):
    dirName = "%s%s/covers"%(config.CONST_PATH, manga.code)
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        log.info("mkdir %s"%dirName)
    else:
        log.error("La carpeta [%s] ya exíste"%dirName)
    return dirName