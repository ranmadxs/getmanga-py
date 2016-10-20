#!/usr/bin/env python
# -*- coding: utf-8 -*-

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import Main
import sys, os
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
import threading


def getCapitulo(capituloCode, mangaCode):
    manga = mangas[mangaCode]
    capitulo = MangaGet.obtenerCapitulo(manga, capituloCode)
    return capitulo

def listaCapTest(mangaCode):
    manga = mangas[mangaCode]
    manga = MangaGet.lstCapitulos(manga)
    return manga
    #log.info(manga)

#def listaImagenesTest():
#    manga = mangas['sun_ken_rock']
#    capitulo = capituloZunKenRock()
#    MangaGet.lstImagenes(manga, capitulo)
#    log.info(capitulo)

def descargaMagnaTest():
    paramDescarga = ParamDescarga('10', TYPE.UNIQUE)
    Main.descargarManga('sun_ken_rock', paramDescarga)

#TInicio est 1
capitulo = getCapitulo("2", "sun_ken_rock2")
print capitulo
print ">>>>>>>>  Fin test getCapitulo <<<<<<<<<<<"

manga = listaCapTest("sun_ken_rock2")
for capitulo in manga.capitulos:
    print capitulo
    
print ">>>>>>>>  Fin test listaCapTest <<<<<<<<<<<"

#listaImagenesTest()
#descargaMagnaTest()
