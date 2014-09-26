#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 17-03-2014

@author: esanchez
'''
import Main
import sys
from config import mangas
from libs import MangaGet, MangaFile
from model.bean import Manga, Capitulo, Imagen
from model import chapter
from libs import log
import httplib
import httplib2, re
from re import sub
from libs import funciones
from model.TYPE import ParamDescarga
from model import TYPE
from svc import Cover, Esmangahere, VolumenScan
import HTMLParser

########### BASIC DATA TEST ####################3
def capituloZetaman2():    
    capitulo = Capitulo()
    capitulo.code = "14"
    capitulo.url = "http://submanga.com/c/35471"
    capitulo.title = "Zetman 14"
    capitulo.length = 0
    capitulo.folder = "/media/Shampoo/Manga/zetman/download/C014"
    return capitulo

def capituloLiar_game2():    
    capitulo = Capitulo()
    capitulo.code = "1"
    capitulo.url = "http://es.mangahere.co/manga/liar_game/c1/"
    capitulo.title = "Liar Game   1"
    capitulo.length = 0
    capitulo.folder = "/media/Shampoo/Manga/liar_game/download/C01"
    return capitulo

def imagenZetaman2():
    imagen = Imagen()
    imagen.url = "http://submanga.com/c/35471/1"
    imagen.code = "1"
    return imagen

def imagenLiar_game2():
    imagen = Imagen()
    imagen.url = "http://es.mangahere.co/manga/liar_game/c51/"
    imagen.code = "1"
    imagen.title = "1"
    return imagen


print 'Test wget'

#Test: Parsea el html y genera objeto volumen como areglo
def parserTest():
    manga = mangas['wolf_guy']   
    volumenes = VolumenScan.listaVolumenes(manga)
    for volumen in volumenes:
        print volumen
    
def descargaCaratulasTest():    
    manga = mangas['is']
    Cover.obtenerCaratulas(manga)

def listaCapitulosTest():
    manga = mangas['liar_game2']
    #paramDescarga = ParamDescarga(None, None)
    paramDescarga = ParamDescarga('13', None)
    manga = MangaGet.lstCapitulos(manga, paramDescarga)
    log.info(manga)

def listaImagenesTest():
    #manga = mangas['liar_game2']
    manga = mangas['zetman2']
    capitulo = capituloZetaman2()
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
    paramDescarga = ParamDescarga('13', TYPE.UNIQUE)
    Main.descargarManga('liar_game2', paramDescarga)


def obtenerImagenTest():
    #manga = mangas['zetman2']
    manga = mangas['liar_game2']
    #imagen = imagenZetaman2()
    imagen = imagenLiar_game2()
    imagen = MangaGet.obtenerImagen(manga, imagen)
    print imagen

def organizarVolumenesTest():
    manga = mangas['slam-dunk']
    Main.organizarVolumenes(manga)
'''
 ########## Inicio Ejec Test #########
'''
    
#parserTest()
organizarVolumenesTest()
#listaCapitulosTest()
#listaImagenesTest()
#obtenerImagenTest()
#descargaCaratulasTest()
#descargaMagnaTest()
exit(0)

