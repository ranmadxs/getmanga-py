#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17-03-2014

@author: esanchez
'''
import httplib2, re
import config
from svc import Submanga, Esmangahere, Submangaorg
from libs import log, funciones
from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
from model import TYPE



CONST_EXP_OBT_IMAGEN='<img id="img_mng_enl" src="(.+?)" alt="(.+?)"/>'
CONST_ESMANGAHERE_IMG = '<img src="(.+?)" width="(.+?)" id="image" alt="(.+?)" />'
CONST_ESMANGA_IMG = '<img style="width:100% !important;" src="(.+?)" alt="(.+?)" />'

http = httplib2.Http()

def obtenerCapitulo(manga = Manga, codCapitulo = None):
    if codCapitulo != None :
        parametros = ParamDescarga(codCapitulo, TYPE.UNIQUE)
        manga = lstCapitulos(manga, parametros)
        return (manga.capitulos[:1] or [None])[0]
    return None
    
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
            if(manga.site == config.submangaorg):
                urlCapitulo = Submangaorg.obtenerURLCaps(manga)
                caps, manga = Submangaorg.obtenerCapitulos(manga, urlCapitulo, parametros)
            if(manga.site == config.submanga):
                urlCapitulo = Submanga.obtenerURLCaps(manga)
                caps, manga = Submanga.obtenerCapitulos(manga, urlCapitulo, parametros)
            if manga.site == config.esmangahere:
                urlCapitulo = Esmangahere.obtenerURLCaps(manga)
                caps, manga = Esmangahere.obtenerCapitulos(manga, urlCapitulo, parametros)
        except IndexError:                
            retry = True
        finally:
            numberRetry = numberRetry + 1
    manga.capitulos = caps        
    return manga

def lstImagenes(manga = Manga, capitulo = Capitulo):
    lstImagenes = []
    log.info("http.request[lstImagenes] ==> %s"%capitulo.url)
    if(manga.site == config.submangaorg):
        lstImagenes = Submangaorg.obtenerImagenes(manga, capitulo)    
    if(manga.site == config.submanga):        
        lstImagenes = Submanga.obtenerImagenes(capitulo) 
    if manga.site == config.esmangahere:
        lstImagenes = Esmangahere.obtenerImagenes(capitulo, manga)

    capitulo.imagenes = lstImagenes
    capitulo.length = len(lstImagenes)
    return capitulo

def obtenerImagen(manga = Manga, imagen = Imagen):
    if(manga.site == config.submangaorg):
        imagen.urlReal = imagen.url
        imagen.title = imagen.code
        return imagen
    if(manga.site == config.esmangahere):
        pat = re.compile(CONST_ESMANGAHERE_IMG)             
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
        if(manga.site == config.submanga):
            imagen.urlReal = img
        if(manga.site == config.esmangahere):
            imagen.urlReal = img[0]
    return imagen

def obtenerCodByURL(url, prefijoURL):
    code = url.replace(prefijoURL, '')
    code = code.replace("/", '')
    return code