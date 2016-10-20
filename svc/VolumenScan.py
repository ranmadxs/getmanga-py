#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 25-09-2014

@author: esanchez
'''
import httplib2, re, HTMLParser
from model import chapter
import config
from model.bean import Manga
from libs import log, funciones
import os

def getURLScann(manga = Manga):
    return "http://%s/%s"%(config.volumenurl, manga.urlVolumen)

def getMangaInfo(manga = Manga):
    parser = InfoHTMLParser()
    http = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
    log.info("http.request[infoManga] ==> %s"%manga.infoUrl)
    headers, body = http.request(manga.infoUrl)
    #body = str(body).decode('utf-8')
    parser.feed("%s"%body)
    parser.close()  
    return parser.STATUS, parser.VOL_INFO  

def listaVolumenes(manga = Manga):
    parser = VolumenHTMLParser()
    http = httplib2.Http()
    urlVol = getURLScann(manga)
    log.info("http.request[listaVolumenes] ==> %s"%urlVol)  
    headers, body = http.request(urlVol)
    body = str(body).decode('utf-8')
    parser.feed("%s"%body)
    parser.close()
    return parser.VOLUMEN, parser.STATUS

class InfoHTMLParser(HTMLParser.HTMLParser):
    
    def __init__(self):
        self.reset()
        self.STATUS = None
        self.FIND_STATUS = False
        self.VOL_INFO = None
        self.FIND_VOL_INFO = False
        self.VALID_TAG = False
        self.TAG = None
    def handle_starttag(self, tag, attrs):
        if tag == 'div':
            self.VALID_TAG = True
        self.TAG = tag
            
    def handle_endtag(self, tag):
        self.VALID_TAG = False     
           
    def handle_data(self, data):
        dataHtml = str(data).strip()
        if self.FIND_STATUS == True and self.VALID_TAG == True:
            self.FIND_STATUS = False
            self.STATUS = dataHtml
            return
        if 'Completely Scanlated?' == dataHtml:
            self.FIND_STATUS = True

        if self.FIND_VOL_INFO == True and self.VALID_TAG == True:
            self.FIND_VOL_INFO = False
            self.VOL_INFO = dataHtml            
            return
        if 'Status in Country of Origin' == dataHtml:
            self.FIND_VOL_INFO = True


class VolumenHTMLParser(HTMLParser.HTMLParser):
    def __init__(self):
        self.reset()
        self.VOLUMEN = []
        self.VALIDTAG = False   
        self.VALID_VOLUMEN = False
        self.VALID_CAPITULO = False
        self.INIT = False 
        self.STATUS = None
        self.FIND_STATUS = False
        
    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'chapterlistfull':
            self.INIT = True
        if not self.INIT:
            self.VALIDTAG = False
            return
        if tag == 'li' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'volume':
            self.VALID_VOLUMEN = True 
            
        if tag == 'a' and len(attrs) > 1 and attrs[0][0] == 'href' and attrs[1][0] == 'id':
            self.VALID_CAPITULO = True         
        
        self.VALIDTAG = True        
    def handle_endtag(self, tag):
        if tag == 'li':
            self.VALID_VOLUMEN = False
        if tag == 'a':
            self.VALID_CAPITULO = False
        if not self.INIT:
            return
        if tag == 'ul':
            self.INIT = False    
    def handle_data(self, data):
        if self.FIND_STATUS == True:
            self.FIND_STATUS = False
            self.STATUS = data.strip()
            return
        if 'Status:' == data.strip():
            self.FIND_STATUS = True
        
        if(not self.VALIDTAG):
            return
        if(self.VALID_VOLUMEN):
            volumen = chapter.Volumen(data, [])
            self.VOLUMEN.append(volumen)
        if self.VALID_CAPITULO and self.VOLUMEN.__len__() > 0:
            capitulo = chapter.Capitulo(data)
            volumen = self.VOLUMEN.pop()
            volumen.capitulos.append(capitulo)
            self.VOLUMEN.append(volumen)