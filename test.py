#!/usr/bin/env python
# -*- coding: utf-8 -*-
########### Resivas el error los archivos deben ser renombrados

'''
Created on 17-03-2014

@author: esanchez
'''
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

########### BASIC DATA TEST ####################3
def capituloZetaman2():    
    capitulo = Capitulo()
    capitulo.code = "14"
    capitulo.url = "http://submanga.com/c/35471"
    capitulo.title = "Zetman 14"
    capitulo.length = 0
    capitulo.folder = "/media/Shampoo/Manga/zetman/download/C014"
    return capitulo

def capituloSprite():    
    capitulo = Capitulo()
    capitulo.code = "1"
    capitulo.url = "http://esmanga.com/manga/sprite/c1"
    capitulo.title = "Sprite 1"
    capitulo.length = 0
    capitulo.folder = "/media/Shampoo/Manga/sprite/download/C01"
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
    volumenes, status = VolumenScan.listaVolumenes(manga)
    for volumen in volumenes:
        print volumen
    
def descargaCaratulasTest():    
    manga = mangas['sprite']
    Cover.obtenerCaratulas(manga)

def listaCapitulosTest():
    manga = mangas['sprite']
    paramDescarga = ParamDescarga(None, None)
    #paramDescarga = ParamDescarga('13', None)
    manga = MangaGet.lstCapitulos(manga, paramDescarga)
    log.info(manga)

def listaImagenesTest():
    #manga = mangas['liar_game2']
    manga = mangas['sprite']
    capitulo = capituloSprite()
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
    Main.descargarManga('sprite', paramDescarga)


def obtenerImagenTest():
    #manga = mangas['zetman2']
    manga = mangas['liar_game2']
    #imagen = imagenZetaman2()
    imagen = imagenLiar_game2()
    imagen = MangaGet.obtenerImagen(manga, imagen)
    print imagen

def excludeFilesTest():
    manga = mangas['liar_game']
    parametros = ParamDescarga(None, None)
    lstExclusions = Main.exclusionFiles(manga)   
    log.info(" exclusions.txt == %s" % lstExclusions) 
    MangaGet.lstCapitulos(manga, parametros)
    listCapitulos = []
    #TODO: Debo seguir trabajando en el tema de las exclusiones que no esta bien
    for capitulo in manga.capitulos:        
        if not (capitulo.code in lstExclusions):
            print capitulo.code
            listCapitulos.append(capitulo)

def organizarVolumenesTest():
    manga = mangas['kagerou_days']
    Main.organizarVolumenes(manga)

def scannVolumenTest():
    manga = mangas['liar_game']
    lstVol, status = VolumenScan.listaVolumenes(manga)        
    for volumen in lstVol:
        print volumen

def infoMangaTest():
    manga = mangas['holy_knight']
    #manga = mangas['ant']
    #manga = mangas['i_am_a_hero']
    Main.infoManga(manga)

def renombrarArchivosTest():
    MangaFile.renombrarArchivos('/media/Shampoo/Manga/dragon_head/volumenes/02Vol/', 'Dragonhead v02 ')
    
'''
 ########## Inicio Ejec Test #########
'''

#descargaCaratulasTest()

#exit(0)

import time
import thread


def worker(tiempo):
    print threading.currentThread().getName(), 'Lanzado (Worker)'
    time.sleep(tiempo)
    print threading.currentThread().getName(), 'Deteniendo'

def servicio():
    print threading.currentThread().getName(), 'Lanzado'
    print threading.currentThread().getName(), 'Deteniendo'

t = threading.Thread(target=servicio, name='Servicio')

w = threading.Thread(target=worker, args=(30,), name='Worker.w')

z = threading.Thread(target=worker, args=(10,), name='Worker.z')

w.start()

z.start()

t.start()

activeCount = threading.active_count()
print activeCount

print threading.enumerate()
for t in threading.enumerate():
    if "Worker" in t.getName():
        print "Worker activo"
    print t.getName()

workerActivo = True
while (workerActivo):
    workerActivo = False
    for t in threading.enumerate():
        if "Worker" in t.getName():
            workerActivo = True

    
exit(0)

def workers(num):
    """thread worker function"""
    print 'Worker: %s' % num
    return

threads = []
for i in range(5):
    t = threading.Thread(target=workers, args=(i,))
    threads.append(t)
    t.start()    
exit(0)

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass

#renombrarArchivosTest()
#infoMangaTest()   
#parserTest()
#organizarVolumenesTest()
#listaCapitulosTest()
#listaImagenesTest()
#obtenerImagenTest()

#descargaMagnaTest()
exit(0)
#open the file template
filein = open( '/media/Shampoo/Libros/lista_92000.txt' )
str(filein.read()).decode('utf-8')

