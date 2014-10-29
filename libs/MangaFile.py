#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18-03-2014

@author: esanchez
'''
import os, shutil
from libs import log
import config
from libs import funciones
from model.bean import Capitulo, Manga, Imagen
from warnings import catch_warnings

def listarArchivosCarpeta(manga = Manga ):
    dirName = "%s%s/download/"%(config.CONST_PATH, manga.code)
    return listaArchivosPath(dirName)

def listaArchivosPath(dirName = None):
    files = []
    if dirName != None:
        files = os.listdir(dirName)
    return files

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
    makeDir(dirName)
    #else:
    #    log.error("El capítulo [%s] no tiene imágenes"%capitulo.code)
    return capitulo

def move(orig=None, dest=None):
    log.debug("[mv] %s -> %s "%(orig, dest))
    shutil.move(orig, dest)

def copy(orig=None, dest=None):
    if(not os.path.isfile(dest)):
        log.debug("[cp] %s -> %s "%(orig, dest))
        shutil.copyfile(orig, dest)
    else:
        log.file("El archivo [%s] ya exíste"%dest)        

def makeDir(dirName = None):
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        log.info("mkdir %s"%dirName)
    else:
        log.error("La carpeta [%s] ya exíste"%dirName)

def readFile(archivo):
    lines = []
    try:
        lines = [line.strip() for line in open(archivo)]
    except IOError:
        None
    return lines

def descargarArchivo(imagen = Imagen, capitulo = Capitulo):
    filename = imagen.urlReal.split("/")[-1]
    filePath = '%s/%s' %(capitulo.folder, filename)
    if(not os.path.isfile(filePath)):
        log.info('curl %s -o %s/%s'%( imagen.urlReal, capitulo.folder, filename))
        os.system('curl %s -o %s/%s' % (imagen.urlReal, capitulo.folder, filename))        
    else:
        log.error('El archivo [%s] ya existe'% filename)
    imagen.path = filePath
    return imagen