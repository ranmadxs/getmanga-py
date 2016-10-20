'''
Created on 19-10-2016

@author: esanchez
'''

from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
from model import TYPE
from libs import log, funciones
import httplib2
from bs4 import BeautifulSoup

def obtenerImagenes(manga = Manga, capitulo = Capitulo):
    lstImagenes = []
    http = httplib2.Http()
    headers, body = http.request(capitulo.url)
    soup = BeautifulSoup(body, 'html.parser')
    soupDiv = soup.find("div", {"class" : "pagination-bar"})
    numberImgs = int(soupDiv.get_text().encode('utf-8').replace("/", ""))
    #http://submanga.org/resources/uploads/manga/sun-ken-rock/capitulo/es/6/5.jpg
    for i in range(1, numberImgs+1):
        urlImg = "http://%s/resources/uploads/manga/%s/capitulo/es/%s/%s.jpg" % (manga.site, manga.uCode, capitulo.code, i)
        imagen = Imagen(i, urlImg)
        lstImagenes.append(imagen)
    return lstImagenes           

def obtenerCapitulos(manga = Manga, urlCapitulos = '', parametros = ParamDescarga):
    http = httplib2.Http()
    codCapituloIni = parametros.codCapitulo
    headers, body = http.request(urlCapitulos)
    content = body
    log.file(body)
    #print content
    soup = BeautifulSoup(content, 'html.parser')
    lst=[]
    listCapsRet = []
    lstCaps = []
    soupTable = soup.find("table", {"id" : "caps-list"})
    rows = soupTable.find_all('tr')
    for row in rows:
        cells = row.find_all("td")
        tituloCap = cells[1].get_text().encode('utf-8')
        urlCap= "%s/es"%(cells[1].a.get("href"))
        capitulo = Capitulo(urlCap, tituloCap)
        capitulo.code = cells[0].get_text().encode('utf-8')
        lstCaps.append(capitulo)
    
    if(codCapituloIni is not None):
        for cap in lstCaps:
            if(parametros.tipo == TYPE.UNIQUE and int(cap.code) == int(codCapituloIni)):
                lst.append(cap)
                break
            if(parametros.tipo != TYPE.UNIQUE and int(cap.code) >= int(codCapituloIni)):
                lst.append(cap)
    else: 
        lst = lstCaps
                
        
    return lst, manga


def obtenerURLCaps(manga = Manga):
    manga.url = 'http://%s/%s'%(manga.site, manga.uCode)
    return manga.url
