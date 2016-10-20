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


def capituloZunKenRock():
    capitulo = Capitulo()
    capitulo.code = "6"
    capitulo.url = "http://submanga.org/sun-ken-rock/capitulo/6/es"
    capitulo.title = "Zun Ken Rock 6"
    capitulo.length = 0
    capitulo.folder = "/Manga/sun_ken_rock/download/C06"
    return capitulo

def listaCapTest():
    manga = mangas['sun_ken_rock']
    paramDescarga = ParamDescarga('6', TYPE.UNIQUE)
    #paramDescarga = ParamDescarga('13', None)
    manga = MangaGet.lstCapitulos(manga, paramDescarga)
    for capitulo in manga.capitulos:
        print capitulo
    #log.info(manga)

def listaImagenesTest():
    #manga = mangas['liar_game2']
    manga = mangas['sun_ken_rock']
    capitulo = capituloZunKenRock()
    MangaGet.lstImagenes(manga, capitulo)
    log.info(capitulo)

def descargaMagnaTest():
    paramDescarga = ParamDescarga('6', TYPE.UNIQUE)
    Main.descargarManga('sun_ken_rock2', paramDescarga)

#listaCapTest()
#listaImagenesTest()
descargaMagnaTest()
