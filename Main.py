#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18-03-2014

@author: esanchez
'''
import config
from libs import log, funciones
from libs import MangaGet, MangaFile
from model import TYPE
from model.TYPE import ParamDescarga 
from model.bean import Capitulo, Manga 
from svc import VolumenScan

def organizarVolumenes(manga = Manga):
    lstFolder = MangaFile.listarArchivosCarpeta(manga)           
    for folder in lstFolder:
        print folder    
    if(len(lstFolder) > 0):
        totPre = len(lstFolder[0]) - 1
        lstVol = VolumenScan.listaVolumenes(manga)        
        for volumen in lstVol:
            lstFolderInVol = []
            capIni = volumen.capitulos[-1].name.split(" ")[-1]
            capFin = volumen.capitulos[0].name.split(" ")[-1]
            capIni = "C%s"%funciones.prefijo(str(capIni), totPre)
            capFin = "C%s"%funciones.prefijo(str(capFin), totPre)
            log.info( "%s ):: %s -> %s"%(volumen.name, capIni, capFin))
            for folder in lstFolder:
                downloadDir = "%s%s/download/%s"%(config.CONST_PATH, manga.code, folder)
                if capIni <= folder and folder <= capFin:
                    lstFolderInVol.append(downloadDir)
           # log.debug(lstFolderInVol)
            if(lstFolderInVol.__len__()> 0):                
                volumenName = volumen.name.split(" ")[-1]
                volumenName = "%s - %s %s-%s"%(funciones.prefijo(str(volumenName), 2), str(manga.code).title(), capIni, capFin)
                volumensDir = "%s%s/volumenes/%s"%(config.CONST_PATH, manga.code, volumenName)
                volumensDir = volumensDir.replace(' ', '')
                log.debug("[mkdir] =>%s"%volumensDir)
                MangaFile.makeDir(volumensDir)
                for folder in lstFolderInVol:
                    folderName = folder.split("/")[-1]
                    destFolder = "%s/%s"%(volumensDir, folderName)
                    MangaFile.move(folder, destFolder)

def descargarManga(codigoManga = None, parametros = ParamDescarga):
    log.debug(codigoManga)
    manga = config.mangas[codigoManga]
    MangaGet.lstCapitulos(manga, parametros)    
    for capitulo in manga.capitulos:        
        MangaFile.crearDirectorio(capitulo, manga)
        capitulo = MangaGet.lstImagenes(manga, capitulo)
        totalImgCarpeta = MangaFile.totalArchivosCarpeta(capitulo)
        if(capitulo.length > totalImgCarpeta):
            for imagen in capitulo.imagenes:
                retry = False
                numberRetry = int(0)
                while (numberRetry == 0 or retry):  
                    try:       
                        if retry:
                            log.error("Error al descargar imágen")
                            log.info("Retry N° %i"%numberRetry) 
                            retry = False                            
                        imagen = MangaGet.obtenerImagen(manga, imagen)
                        imagen = MangaFile.descargarArchivo(imagen, capitulo)
                    except AttributeError:    
                        retry = True
                    finally:
                        numberRetry = numberRetry + 1
            if(manga.site == config.submanga): 
                MangaFile.renombrarArchivos("%s/"%capitulo.folder, '')      
        else:
            log.error("Todos los archivos del capitulo %s ya han sido descargados"%capitulo.title)                              
    return manga

def evaluarParamExtra(paramExtra=None):
    cobUnica = bool(0)
    if(paramExtra is None):
        cobUnica = bool(0)
    else:
        if(str(paramExtra).upper() == '-D'):
            cobUnica = bool(1)        
    return cobUnica