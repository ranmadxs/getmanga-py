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
        for imagen in capitulo.imagenes:
            imagen = MangaGet.obtenerImagen(manga, imagen)
            imagen = MangaFile.descargarArchivo(imagen, capitulo)
        if(manga.site == config.submanga): 
            MangaFile.renombrarArchivos("%s/"%capitulo.folder, '')
    return manga

def evaluarParamExtra(paramExtra=None):
    cobUnica = bool(0)
    if(paramExtra is None):
        cobUnica = bool(0)
    else:
        if(str(paramExtra).upper() == '-D'):
            cobUnica = bool(1)        
    return cobUnica