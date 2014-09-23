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


print 'Inicio Test'
'''
pat = re.compile('<ul class="chapterlistfull">(.+?)</ul>')
http = httplib2.Http()
headers, body = http.request("http://manga.animea.net/zetman.html#.VCBcf493_ac")
li = pat.findall(body)
print li
exit(0)
'''
        
parser = funciones.MyHTMLParser()
http = httplib2.Http()
#headers, body = http.request("http://manga.animea.net/alpine-rose.html#.VBmELY93_ac")
headers, body = http.request("http://manga.animea.net/slam-dunk.html#.VCCIy493_ac")
parser.feed("%s"%body)
for volumen in parser.VOLUMEN:
    print volumen
parser.close()
exit(0)


#manga = mangas['is']
#Cover.obtenerCaratulas(manga)

#MangaFile.renombrarArchivos('/media/Shampoo/Manga/uzumaki/01 Uzumaki C001-006/C05/', '')

#print mangas["shingeki_no_kyojin"]
#paramDescarga = ParamDescarga('Extra_vol-9', TYPE.UNIQUE)
#descargarManga('dorohedoro2', paramDescarga)
#sys.exit(0)

'''
Lista de Capitulos
'''
#manga = mangas['zetman2']
#paramDescarga = ParamDescarga(None, None)
#paramDescarga = ParamDescarga('Extra_vol-13', TYPE.UNIQUE)
#manga = MangaGet.lstCapitulos(manga, paramDescarga)
#log.info(manga)

'''
Lista de Imagenes
'''
#manga = mangas['zetman2']
#capitulo = Capitulo()
#capitulo.code = "14"
#capitulo.url = "http://submanga.com/c/35471"
#capitulo.title = "Zetman 14"
#capitulo.length = 0
#capitulo.folder = "/media/Shampoo/Manga/zetman/download/C014"
#MangaGet.lstImagenes(manga, capitulo)
#log.info(capitulo)

#manga = mangas['dorohedoro2']
#imagen = Imagen("1", "http://submanga.com/c/211690")
#imagen = MangaGet.obtenerImagen(manga, imagen)
#print imagen




#pat = re.compile('<select class="cbo_wpm_chp" onchange="[^"]+">(.+?)</select>')
'''
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
'''

#    strOption = str(elem)
    #strOption = strOption.replace('<strong>', '')
    #strOption = strOption.replace('</strong>', '')
    #pat2 = re.compile('<a href="(.+?)">(.+?)</a>')
    #li2 = pat2.findall(strOption)
    #print li2
'''
pat3 = re.compile('<option value="[^"]+">(.+?)</option>')
http = httplib2.Http()
headers, body = http.request("http://submanga.com/c/191518")
body = body.replace(' selected', '')
print body
li3 = pat3.findall(body)
print li3
'''

'''
def tryint(x):
    try:
        return int(x)
    except ValueError:
        return x

def splittedname(s):
    return tuple(tryint(x) for x in re.split('([0-9]+)', s[0][0]))

#names = ['YT4.11', '4.3', 'YT4.2', '4.10', 'PT2.19', 'PT2.9']
#names = [('19', 'Cap\xc3\xadtulo 19'), ('18', 'Cap\xc3\xadtulo 18'), ('17', 'Cap\xc3\xadtulo 17'), ('16', 'Cap\xc3\xadtulo 16'), ('15', 'Cap\xc3\xadtulo 15'), ('14', 'Cap\xc3\xadtulo 14'), ('13', 'Cap\xc3\xadtulo 13'), ('12', 'Cap\xc3\xadtulo 12'), ('11', 'Cap\xc3\xadtulo 11'), ('10', 'Cap\xc3\xadtulo 10'), ('9', 'Cap\xc3\xadtulo 9'), ('8', 'Cap\xc3\xadtulo 8'), ('7', 'Cap\xc3\xadtulo 7'), ('6', 'Cap\xc3\xadtulo 6'), ('5', 'Cap\xc3\xadtulo 5'), ('4', 'Cap\xc3\xadtulo 4'), ('3', 'Cap\xc3\xadtulo 3'), ('2', 'Cap\xc3\xadtulo 2'), ('1', 'Cap\xc3\xadtulo 1')]
#names = [[('http://submanga.com/Uzumaki/19/115760', 'Uzumaki 19')], [('http://submanga.com/Uzumaki/18/115759', 'Uzumaki 18')], [('http://submanga.com/Uzumaki/17/115756', 'Uzumaki 17')], [('http://submanga.com/Uzumaki/16/115754', 'Uzumaki 16')], [('http://submanga.com/Uzumaki/15/115753', 'Uzumaki 15')], [('http://submanga.com/Uzumaki/14/115703', 'Uzumaki 14')], [('http://submanga.com/Uzumaki/13/10559', 'Uzumaki 13')], [('http://submanga.com/Uzumaki/12/115698', 'Uzumaki 12')], [('http://submanga.com/Uzumaki/11/115691', 'Uzumaki 11')], [('http://submanga.com/Uzumaki/10/115688', 'Uzumaki 10')], [('http://submanga.com/Uzumaki/9/115685', 'Uzumaki 9')], [('http://submanga.com/Uzumaki/8/115684', 'Uzumaki 8')], [('http://submanga.com/Uzumaki/7/9760', 'Uzumaki 7')], [('http://submanga.com/Uzumaki/6/9374', 'Uzumaki 6')], [('http://submanga.com/Uzumaki/5/9230', 'Uzumaki 5')], [('http://submanga.com/Uzumaki/4/115675', 'Uzumaki 4')], [('http://submanga.com/Uzumaki/3/9108', 'Uzumaki 3')], [('http://submanga.com/Uzumaki/2/8964', 'Uzumaki 2')], [('http://submanga.com/Uzumaki/1/8943', 'Uzumaki 1')], [('http://submanga.com/Uzumaki/Extra_-_Cap\xc3\xadtulo_perdido/115606', 'Uzumaki Extra - Cap\xc3\xadtulo perdido')]]

#lista = sorted(names, key=splittedname)
#print lista
'''