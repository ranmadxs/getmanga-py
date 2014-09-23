#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18-03-2014

@author: esanchez
'''
import config
from libs import log
from libs import MangaGet, MangaFile
from model import TYPE
from model.TYPE import ParamDescarga 

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