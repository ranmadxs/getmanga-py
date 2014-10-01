#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18-03-2014

@author: esanchez
'''
import config, os
from libs import log, funciones
from libs import MangaGet, MangaFile
from model import TYPE
from model.TYPE import ParamDescarga 
from model.bean import Capitulo, Manga 
from svc import VolumenScan
from string import Template

def infoManga(manga = Manga):
    log.info("[Info Manga] %s"%manga.code)
    fileInfo = "%s%s/%s"%(config.CONST_PATH, manga.code, config.CONST_INFO_FILE)

    #open the file template
    filein = open( '%s/tpl/info.tpl'%config.CONST_PATH_SRC )
    info = VolumenScan.getURLScann(manga)
    info = str(info).decode('utf-8')
    lstVol = VolumenScan.listaVolumenes(manga)
    listVol = []
    countVol = int(0)
    countCap = int(0)
    for vol in lstVol:                
        for cap in vol.capitulos:
            capStr = str("  > %s"%cap.name).decode('utf-8')
            listVol.append(capStr)
            countCap = countCap + 1
        listVol.append("------------------------------")
        listVol.append(vol.name)
        listVol.append("------------------------------")
        countVol = countVol + 1
    listVol = listVol[::-1]
    #read it
    src = Template( str(filein.read()).decode('utf-8') )
    #document data
    title = str(manga.code).decode('utf-8')
    cover = str(manga.cover).decode('utf-8')
    d={ 'title':title, 'list':'\n'.join(listVol) , 'cover' : cover, 'info' : info, 'countCap' : countCap, 'countVol' : countVol}
    #do the substitution
    result = src.substitute(d)
    result = result.encode('utf-8')
    log.debug(result)
    file_ = open(fileInfo, 'w')
    file_.write(result)
    file_.close()

def organizarVolumenes(manga = Manga):
    lstFolder = MangaFile.listarArchivosCarpeta(manga)           
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
    lstExclusions = exclusionFiles(manga)   
    log.info(" exclusions.txt == %s" % lstExclusions) 
    MangaGet.lstCapitulos(manga, parametros)
    listCapitulos = []
    #TODO: Debo seguir trabajando en el tema de las exclusiones que no esta bien
    for capitulo in manga.capitulos:
        if not (capitulo.code in lstExclusions):
            listCapitulos.append(capitulo)
            
    for capitulo in listCapitulos:        
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

def exclusionFiles(manga = Manga):
    fileExcl = "%s%s/%s"%(config.CONST_PATH, manga.code, config.CONST_EXCLUSIONS_FILE)
    lstExcl = MangaFile.readFile(fileExcl)
    return lstExcl

def evaluarParamExtra(paramExtra=None):
    cobUnica = bool(0)
    if(paramExtra is None):
        cobUnica = bool(0)
    else:
        if(str(paramExtra).upper() == '-D'):
            cobUnica = bool(1)        
    return cobUnica