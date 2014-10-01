#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 25-09-2014

@author: esanchez
'''
import httplib2, re
import config
from model.bean import Manga
from libs import log, funciones
import os

def getURLScann(manga = Manga):
    return "http://%s/%s"%(config.volumenurl, manga.urlVolumen)

def listaVolumenes(manga = Manga):
    parser = funciones.VolumenHTMLParser()
    http = httplib2.Http()
    urlVol = getURLScann(manga)
    log.info("http.request[listaVolumenes] ==> %s"%urlVol)  
    headers, body = http.request(urlVol)
    body = str(body).decode('utf-8')
    parser.feed("%s"%body)
    parser.close()
    return parser.VOLUMEN