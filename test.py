#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17-03-2014

@author: esanchez
'''
import sys
from config import mangas
from libs import MangaGet, MangaFile
from model.bean import Manga, Capitulo, Imagen
from model import chapter
from Main import descargarManga
from libs import log
import httplib
import httplib2, re
from re import sub
from libs import funciones
from model.TYPE import ParamDescarga
from model import TYPE
from svc import Cover
import HTMLParser

print 'Test wget'

#Test: Parsea el html y genera objeto volumen como areglo
def parserTest():    
    parser = funciones.VolumenHTMLParser()
    http = httplib2.Http()
    headers, body = http.request("http://manga.animea.net/zetman.html#.VCGOu493_ac")
    #headers, body = http.request("http://manga.animea.net/slam-dunk.html#.VCCIy493_ac")
    parser.feed("%s"%body)
    for volumen in parser.VOLUMEN:
        print volumen
    parser.close()
    
def descargaCaratulasTest():    
    manga = mangas['is']
    Cover.obtenerCaratulas(manga)

def listaCapitulosTest():
    manga = mangas['zetman2']
    paramDescarga = ParamDescarga(None, None)
    #paramDescarga = ParamDescarga('13', TYPE.UNIQUE)
    manga = MangaGet.lstCapitulos(manga, paramDescarga)
    log.info(manga)

def listaImagenesTest():
    manga = mangas['zetman2']
    capitulo = Capitulo()
    capitulo.code = "14"
    capitulo.url = "http://submanga.com/c/35471"
    capitulo.title = "Zetman 14"
    capitulo.length = 0
    capitulo.folder = "/media/Shampoo/Manga/zetman/download/C014"
    MangaGet.lstImagenes(manga, capitulo)
    log.info(capitulo)
    
def expresionesRegularesTest():    
    pat = re.compile('<a href="(.+?)" title="(.+?)">')
    http = httplib2.Http()
    headers, body = http.request("http://manga.joentjuh.nl/series/9709/")
    li = pat.findall(body)
    for elem in li:
        print "%s (%s)" %( elem[1], elem[0])
        headers, body = http.request(elem[0])    
        rex = re.compile(r'<div class="raw_links clear">(.*?)<div class="block" id="unsorted" style="margin-top:5px;padding-top:10px;text-align:center;">',re.S|re.M)
        match = rex.findall(body)
            
        pat = re.compile('<a href="(.+?)">')
        imagenes = pat.findall(match[0])
        for img in imagenes:
            print img

def descargaMagnaTest():
    paramDescarga = ParamDescarga('Extra_vol-9', TYPE.UNIQUE)
    descargarManga('dorohedoro2', paramDescarga)
    

'''
 ########## Inicio Ejec Test #########
'''
parserTest()
#descargaCaratulasTest()
#descargaMagnaTest()
exit(0)
