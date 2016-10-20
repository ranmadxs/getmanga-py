#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18-03-2014

@author: esanchez
'''
import config, os, time
from libs import log, funciones
from libs import MangaGet, MangaFile
from model import TYPE
from model.TYPE import ParamDescarga 
from model.bean import Capitulo, Manga 
from svc import VolumenScan
from string import Template
import threading

def infoManga(manga = Manga):
    log.info("[Info Manga] %s"%manga.code)
    fileInfo = "%s%s/%s"%(config.CONST_PATH, manga.uCode, config.CONST_INFO_FILE)

    #open the file template
    filein = open( '%s/tpl/info.tpl'%config.CONST_PATH_SRC )
    info = VolumenScan.getURLScann(manga)
    info = str(info).decode('utf-8')
    lstVol, status = VolumenScan.listaVolumenes(manga)
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
    status, volinfo = VolumenScan.getMangaInfo(manga)
    #read it
    src = Template( str(filein.read()).decode('utf-8') )
    #document data
    title = str(manga.code).decode('utf-8')
    cover = str(manga.cover).decode('utf-8')
    d={ 'title':title, 'list':'\n'.join(listVol) , 'cover' : cover, 'info' : info, 'countCap' : countCap, 'countVol' : countVol, 'status' : status, 'volinfo': volinfo}
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
        lstVol, status = VolumenScan.listaVolumenes(manga)        
        for volumen in lstVol:
            lstFolderInVol = []
            capIni = volumen.capitulos[-1].name.split(" ")[-1]
            capFin = volumen.capitulos[0].name.split(" ")[-1]
            capIni = funciones.eliminarChrToEnd(capIni, ".")
            capFin = funciones.eliminarChrToEnd(capFin, ".")
            capIni = "C%s"%funciones.prefijo(str(capIni), totPre)
            capFin = "C%s"%funciones.prefijo(str(capFin), totPre)
            log.info( "%s ):: %s -> %s"%(volumen.name, capIni, capFin))
            for folder in lstFolder:
                downloadDir =  MangaFile.getMangaDownloadFolder(manga.uCode, folder)
                if capIni <= folder and folder <= capFin:
                    lstFolderInVol.append(downloadDir)
            if(lstFolderInVol.__len__()> 0):                
                volumenName = volumen.name.split(" ")[-1]
                volumenName = "%s-%s-%s-%s"%(funciones.prefijo(str(volumenName), 2), str(manga.uCode).title(), capIni, capFin)
                volumensDir = "%s%s/volumenes/%s"%(config.CONST_PATH, manga.uCode, volumenName)
                volumensDir = volumensDir.replace(' ', '')
                log.debug("[mkdir] =>%s"%volumensDir)
                MangaFile.makeDir(volumensDir)
                for folder in lstFolderInVol:
                    folderName = folder.split("/")[-1]
                    destFolder = "%s/%s"%(volumensDir, folderName)
                    MangaFile.move(folder, destFolder)         
    else:
        log.error("No se han encontrado capítulos en la carpeta download")               
    volumensDir = "%s%s/volumenes/"  %(config.CONST_PATH, manga.uCode)
    coverDir = "%s%s/covers/"  %(config.CONST_PATH, manga.uCode)
    lstVolumen = MangaFile.listaArchivosPath(volumensDir)
    lstCovers = MangaFile.listaArchivosPath(coverDir)
    log.info("Poniendo las carátulas en los volúmenes")
    if(len(lstVolumen) > 0) and (len(lstCovers) > 0):
        for volumen in lstVolumen:
            volFolder = "%s%s"%(volumensDir, volumen)
            log.debug(volFolder)
            numVol = volumen.split("-")[0]
            frontFile = "%s v%s_front.jpg"%(manga.id, numVol)
            fullFile = "%s v%s_full.jpg"%(manga.id, numVol)
            tocFile = "%s v%s_toc.jpg"%(manga.id, numVol)
            backFile = "%s v%s_back.jpg"%(manga.id, numVol)
            if (frontFile in lstCovers):
                origen = "%s%s"%(coverDir,frontFile)
                destino = "%s/001_front.jpg"%(volFolder)                
                MangaFile.copy(origen, destino)
            if (fullFile in lstCovers):
                origen = "%s%s"%(coverDir,fullFile)
                destino = "%s/002_full.jpg"%(volFolder)                
                MangaFile.copy(origen, destino)
            if (tocFile in lstCovers):
                origen = "%s%s"%(coverDir,tocFile)
                destino = "%s/003_toc.jpg"%(volFolder)                
                MangaFile.copy(origen, destino)
            if (backFile in lstCovers):
                origen = "%s%s"%(coverDir,backFile)
                destino = "%s/z004_back.jpg"%(volFolder)                
                MangaFile.copy(origen, destino)

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
    fileTime =  time.strftime("%Y%m%d")       
    fileDownload = MangaFile.getMangaDownloadFolder(manga.uCode, "t%s_%s"%(fileTime, config.CONST_DOWNLOAD_FILE))  
    for capitulo in listCapitulos:        
        MangaFile.crearDirectorio(capitulo, manga)
        capitulo = MangaGet.lstImagenes(manga, capitulo)
        totalImgCarpeta = MangaFile.totalArchivosCarpeta(capitulo)
        if(capitulo.length > totalImgCarpeta):
            log.debug("Descargando Imágenes del capítulo :: %s" % capitulo.code)
            file_ = open(fileDownload, 'a')
            file_.write("====== Resumen C%s ====== \n"%(capitulo.code))
            file_.close()
            descargarImagenesCapitulo(manga, capitulo, fileDownload)
            totalImgCarpeta = MangaFile.totalArchivosCarpeta(capitulo)
            file_ = open(fileDownload, 'a')
            file_.write("C%s \t Total:%s \t Descargados:%s \n"%(capitulo.code, capitulo.length, totalImgCarpeta))
            file_.close()
        else:
            log.error("Todos los archivos del capitulo %s ya han sido descargados"%capitulo.title)  
        
    return manga

def descargarImagenesCapitulo(manga = Manga, capitulo = Capitulo, fileDownload = None):
    for imagen in capitulo.imagenes:
        imagen = MangaGet.obtenerImagen(manga, imagen)
        #imagen = MangaFile.descargarArchivo(imagen, capitulo)
        t = threading.Thread(target=MangaFile.descargarArchivo, args = (imagen, capitulo, manga, fileDownload), name='WorkerDescargarArchivo.C%s.I%s'%(capitulo.code, imagen.code))
        t.start()
        #if(manga.site == config.submanga or manga.site == config.esmanga): 
        #    MangaFile.renombrarArchivos("%s/"%capitulo.folder, '')
    
    #Se espera hasta que todos las imgs del cap esten descargadas hasta seguir con el siguiente cap
    workerActivo = True
    while (workerActivo):
        workerActivo = False
        for t in threading.enumerate():
            if "WorkerDescargarArchivo" in t.getName():
                workerActivo = True          

def exclusionFiles(manga = Manga):
    fileExcl = "%s%s/%s"%(config.CONST_PATH, manga.uCode, config.CONST_EXCLUSIONS_FILE)
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