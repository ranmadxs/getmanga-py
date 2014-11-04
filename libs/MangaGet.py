#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17-03-2014

@author: esanchez
'''
import httplib2, re
import config
from svc import Esmangaonline, Submanga, Esmangahere, Esmanga
from libs import log, funciones
from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
from model import TYPE



CONST_EXP_OBT_IMAGEN='<img id="img_mng_enl" src="(.+?)" alt="(.+?)"/>'
CONST_ESMANGAHERE_IMG = '<img src="(.+?)" width="(.+?)" id="image" alt="(.+?)" />'
CONST_ESMANGA_IMG = '<img style="width:100% !important;" src="(.+?)" alt="(.+?)" />'

http = httplib2.Http()
    
def lstCapitulos(manga = Manga, parametros = ParamDescarga):
    caps = []
    urlCapitulo = None 
    retry = False
    numberRetry = int(0)
    while (numberRetry == 0 or retry):  
        try: 
            if retry:
                log.error("Error al obtener capítulos")
                log.info("Retry N° %i"%numberRetry) 
                retry = False                        
            if(manga.site == config.esmangaonline or manga.site == config.eshentaionline):
                urlCapitulo = Esmangaonline.obtenerURLCaps(manga)
                caps, manga = Esmangaonline.obtenerCapitulos(manga, urlCapitulo, parametros)
            if(manga.site == config.submanga):
                urlCapitulo = Submanga.obtenerURLCaps(manga)
                caps, manga = Submanga.obtenerCapitulos(manga, urlCapitulo, parametros)
            if manga.site == config.esmangahere:
                urlCapitulo = Esmangahere.obtenerURLCaps(manga)
                caps, manga = Esmangahere.obtenerCapitulos(manga, urlCapitulo, parametros)
            if manga.site == config.esmanga:
                urlCapitulo = Esmanga.obtenerURLCaps(manga)
                caps, manga = Esmanga.obtenerCapitulos(manga, urlCapitulo, parametros)
        except IndexError:                
            retry = True
        finally:
            numberRetry = numberRetry + 1
    manga.capitulos = caps        
    return manga

def lstImagenes(manga = Manga, capitulo = Capitulo):
    lstImagenes = []
    log.info("http.request[lstImagenes] ==> %s"%capitulo.url)
    if(manga.site == config.esmangaonline or manga.site == config.eshentaionline):
        lstImagenes = Esmangaonline.obtenerImagenes(capitulo)
    if(manga.site == config.submanga):        
        lstImagenes = Submanga.obtenerImagenes(capitulo) 
    if manga.site == config.esmangahere:
        lstImagenes = Esmangahere.obtenerImagenes(capitulo, manga)
    if manga.site == config.esmanga:
        lstImagenes = Esmanga.obtenerImagenes(capitulo, manga)

    capitulo.imagenes = lstImagenes
    capitulo.length = len(lstImagenes)
    return capitulo

def obtenerImagen(manga = Manga, imagen = Imagen):
    if(manga.site == config.esmangaonline or manga.site == config.eshentaionline):
        pat = re.compile(CONST_EXP_OBT_IMAGEN)
    if(manga.site == config.esmangahere):
        pat = re.compile(CONST_ESMANGAHERE_IMG)        
    if(manga.site == config.esmanga):
        pat = re.compile(CONST_ESMANGA_IMG)        
    if(manga.site == config.submanga):
        pat = re.compile('<div><a href="[^"]+"><img src="(.+?)"/></a><br/></div>')
    log.info("http.request[obtenerImagen] ==> %s"%imagen.url)
    headers, body = http.request(imagen.url)
    log.file (body)
    arrayImagen = pat.findall("%s"%body)
    if(manga.site == config.submanga and len(arrayImagen) == 0):
        pat = re.compile('</script><a href="[^"]+"><img src="(.+?)"/></a><br/>')
    arrayImagen = pat.findall("%s"%body)
    log.file (arrayImagen)
    for img in arrayImagen: 
        if(manga.site == config.esmangaonline or manga.site == config.eshentaionline):
            imagen.urlReal = img[0]
            imagen.title = img[1]
        if(manga.site == config.submanga):
            imagen.urlReal = img
        if(manga.site == config.esmangahere):
            imagen.urlReal = img[0]
        if(manga.site == config.esmanga):
            imagen.urlReal = img[0]
    return imagen

def obtenerCodByURL(url, prefijoURL):
    code = url.replace(prefijoURL, '')
    code = code.replace("/", '')
    return code