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

def listaImagenesTest(capituloCode, mangaCode):
    manga = mangas[mangaCode]
    capitulo = getCapitulo(capituloCode, mangaCode)
    MangaGet.lstImagenes(manga, capitulo)
    return capitulo

def descargaMagnaTest(capituloCode, mangaCode):
    paramDescarga = ParamDescarga(capituloCode, TYPE.UNIQUE)
    Main.descargarManga(mangaCode, paramDescarga)

def organizarVolumenesTest(codManga):
    manga = mangas[codManga]
    Main.organizarVolumenes(manga)

def descargaCaratulasTest(codManga):    
    manga = mangas[codManga]
    Cover.obtenerCaratulas(manga)

#descargaMagnaTest("56", "sun_ken_rock")
descargaCaratulasTest("sun_ken_rock")
#organizarVolumenesTest("sun_ken_rock")
#TInicio est 1
#capitulo = getCapitulo("11", "sun_ken_rock2")
#print capitulo
#print ">>>>>>>>  Fin test getCapitulo <<<<<<<<<<<"

'''


capitulo = listaImagenesTest("2", "sun_ken_rock2")
for imagen in capitulo.imagenes:
    print imagen
print ">>>>>>>>  Fin test listaImagenesTest <<<<<<<<<<<"

manga = listaCapTest("sun_ken_rock2")
for capitulo in manga.capitulos:
    print capitulo
    
print ">>>>>>>>  Fin test listaCapTest <<<<<<<<<<<"

'''
