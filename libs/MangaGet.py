#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17-03-2014

@author: esanchez
'''
import httplib2, re
import config
from svc import Esmangaonline, Submanga
from libs import log, funciones
from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
from model import TYPE

CONST_EXP_LST_IMAGENES = '<select class="cbo_wpm_pag" onchange="[^"]+">(.+?)</select>'
CONST_EXP_LST_IMG_OPTION='<option value="[^"]+" >(.+?)</option>'
CONST_EXP_OBT_IMAGEN='<img id="img_mng_enl" src="(.+?)" alt="(.+?)"/>'

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
        except IndexError:                
            retry = True
        finally:
            numberRetry = numberRetry + 1
    manga.capitulos = caps        
    return manga

def lstImagenes(manga = Manga, capitulo = Capitulo):
    lstImagenes = []
    log.info("http.request[lstImagenes] ==> %s"%capitulo.url)
    separadorFin = ""    
    numberImgs = []
    if(manga.site == config.esmangaonline or manga.site == config.eshentaionline):
        pat = re.compile(CONST_EXP_LST_IMAGENES)
        headers, body = http.request(capitulo.url)        
        optionsImgs = pat.findall("%s"%body)
        if(len(optionsImgs) > 0):
            strOptions = str(optionsImgs[0])
            strOptions = strOptions.replace('selected="selected"', '')
            pat = re.compile(CONST_EXP_LST_IMG_OPTION)
            numberImgs = pat.findall("%s"%strOptions)
    if(manga.site == config.submanga):        
        pat = re.compile('<option value="[^"]+">(.+?)</option>')
        headers, body = http.request(capitulo.url) 
        body = body.replace(' selected', '')
        numberImgs = pat.findall("%s"%body)
        separadorFin = "/"    
    for codeImg in numberImgs:
        imagen = Imagen(codeImg, '%s%s%s'%(capitulo.url, separadorFin, codeImg))
        lstImagenes.append(imagen)
    capitulo.imagenes = lstImagenes
    capitulo.length = len(lstImagenes)
    return capitulo

def obtenerImagen(manga = Manga, imagen = Imagen):
    if(manga.site == config.esmangaonline or manga.site == config.eshentaionline):
        pat = re.compile(CONST_EXP_OBT_IMAGEN)
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
        else:
            imagen.urlReal = img
    return imagen

def obtenerCodByURL(url, prefijoURL):
    code = url.replace(prefijoURL, '')
    code = code.replace("/", '')
    return code