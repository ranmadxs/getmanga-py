#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18-03-2014

@author: esanchez
'''
import os
from libs import log
import config
from libs import funciones
from model.bean import Capitulo, Manga, Imagen

def totalArchivosCarpeta(capitulo = Capitulo):
    files = []
    total = 0
    try:
        files = os.listdir(capitulo.folder)
    except OSError:
        log.error("No existe la carpeta %s"%capitulo.folder)
    finally:
        total = len(files)
    return total

def renombrarArchivos(mypath='.', prefijo=None, sufijo = '', overflow=7):
    log.debug("Renombrar Archivos")
    listFiles = [ f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath,f)) ]
    largo = len(str(len(listFiles))) + overflow
    log.debug("Total de archivos = %s"%len(listFiles))
    for fileName in listFiles :
        newName = fileName.replace(prefijo, '')
        newName = newName.replace(sufijo, '')
        newName = "p_%s"%funciones.prefijo(newName, largo)
        pathFile = "%s%s"%(mypath, fileName)
        pathNewFile = "%s%s"%(mypath, newName)
        os.rename(pathFile, pathNewFile)
        log.info("Ren %s -> %s"%(fileName, newName))

def crearDirectorio(capitulo = Capitulo, manga = Manga):
    stringCode = funciones.prefijo(capitulo.code, len(str(manga.length)))
    dirName = "%s%s/download/C%s"%(config.CONST_PATH, manga.code, stringCode)
    dirName = funciones.decode(dirName)
    capitulo.folder = dirName
    #if capitulo.length > 0:
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        log.info("mkdir %s"%dirName)
    else:
        log.error("La carpeta [%s] ya exíste"%dirName)
    #else:
    #    log.error("El capítulo [%s] no tiene imágenes"%capitulo.code)
    return capitulo

def descargarArchivo(imagen = Imagen, capitulo = Capitulo):
    filename = imagen.urlReal.split("/")[-1]
    filePath = '%s/%s' %(capitulo.folder, filename)
    if(not os.path.isfile(filePath)):
        os.system('wget %s -P %s' % (imagen.urlReal, capitulo.folder))
        log.info('wget %s -P %s'%( imagen.urlReal, capitulo.folder))
    else:
        log.error('El archivo [%s] ya existe'% filename)
    imagen.path = filePath
    return imagen