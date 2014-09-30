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

def listaVolumenes(manga = Manga):
    parser = funciones.VolumenHTMLParser()
    http = httplib2.Http()
    urlVol = "http://%s/%s"%(config.volumenurl, manga.urlVolumen)
    log.info("http.request[listaVolumenes] ==> %s"%urlVol)  
    headers, body = http.request(urlVol)
    parser.feed("%s"%body)
    parser.close()
    return parser.VOLUMEN