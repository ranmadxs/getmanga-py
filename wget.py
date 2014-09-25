#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from config import mangas
from Main import descargarManga
from libs import log 
from model.TYPE import ParamDescarga 
from model import TYPE
from svc import Cover
from libs.funciones import bcolors
#sys.exit(0)
args = sys.argv

if len(args) > 0 and (args[1] == TYPE.HELP or args[1] == TYPE.H):
    print(bcolors.OKBLUE + "\nGETMANGA 1.1 " + bcolors.ENDC +"Copyright (c) Ranmadxs 2014\n")
    print("Uso:           getmanga <codigoManga> <numeroCapitulo> -<comando>\n")
    print("<comando>\n")
    print(" -h   -- help         Muestra la ayuda, no requiere código del manga ni número del capítulo")
    print(" -U                   Descarga un único capítulo")
    print(" -C                   Descarga las carátulas del manga")
    print(" -L                   Lista los mangas que se encuentran en config.py")
    print(" -V                   Organiza los capítulos de la carpeta download en volúmenes, información extraída de manga.animea.net (Desarrollo)")
    sys.exit(0)

if len(args) > 0 and (args[1] == TYPE.L):
    for manga in mangas:
        print manga
    sys.exit(0)
log.debug('>> Inicio getManga <<')

if(len(args) < 2):
    strError = "Se requieren los siguientes parametros de entrada [nombreManga, codCapitulo]"
    log.error(strError)  
    raise Exception (strError)
codManga = args[1]
codCapitulo = None
if(len(args) >= 3):
    codCapitulo = args[2]
paramExtra = None
log.debug(args)
if(len(args) >= 4):
    paramExtra = args[3]
log.debug(paramExtra)

if (codCapitulo == TYPE.CAPITULOS):
    manga = mangas[codManga]
    Cover.obtenerCaratulas(manga)
    log.debug(">>>> FIN wget.py (ObtenerCover) <<<<")
    sys.exit(0)

if codCapitulo == TYPE.V:
    log.info("Inicio organizando los capítulos en volúmenes")
    log.debug(">>>> FIN wget.py (OrganizarVolumenes) <<<<")
    sys.exit(0)
    
    
paramDescarga = ParamDescarga(codCapitulo, paramExtra)
log.debug(paramDescarga)
descargarManga(codManga, paramDescarga)
log.debug("FIN manga "+codManga)
#log.debug("FIN manga "+codManga+" :: Total Archivos Descargados= "+str(count))
log.close()
log.debug(">>>> FIN wget.py <<<<")
sys.exit(0)