'''
Created on 17-03-2014

@author: esanchez
'''
#TODO: 
# " nuevo servidor de manga con seleium http://submanga.org/"
# OFFLINE esmangaonline.com
# ONLINE submanga.com, es.mangahere.co


#http://es.mangahere.co/manga/freezing/
#http://bato.to

#http://submanga.com/claymore/completa
#http://esmangaonline.com/alive/
import os
VAR_MAIN_PATH = os.path.dirname(os.path.abspath(__file__))

from model.bean import Manga
CONST_PATH_SRC = VAR_MAIN_PATH
CONST_PATH='/Manga/'
CONST_FILE_LOG = 'logs.csv'
CONST_EXCLUSIONS_FILE = "exclusions.txt"
CONST_INFO_FILE = "info.txt"
CONST_DOWNLOAD_FILE = "download.txt"
CONST_MANGA_CFT_FILE = "%s/list_manga.cfg" % VAR_MAIN_PATH
CONST_CANTIDAD_CERO_IMG = 9
CONST_CANTIDAD_CERO_FOLDER = 4

volumenurl = "manga.animea.net"
#infourl = "https://www.mangaupdates.com/series.html?id=%s"

# MANGA SERVERS
submanga = "submanga.com"
submangaorg = "submanga.org"
esmangahere = "es.mangahere.co"

#esmangaonline = "esmangaonline.com"
#eshentaionline = "eshentaionline.com"
#esmanga = "esmanga.com"

MANGA_DEFAULT_SERVER = submangaorg

#mangaCovers="http://manga.joentjuh.nl/series/%s/" -> ya no sirve
#mangaCovers=http://mcd.iosphe.re/ -> esta es la nueva y mantiene los mismos ids parece
#http://mcd.iosphe.re/manga/42898/   tiene api json XDDD     =>   http://mcd.iosphe.re/api/v1/series/%s/

# por ejemplo http://mcd.iosphe.re/manga/1037/
mangas = {}

def readFile(archivo):
    lines = []
    try:
        lines = [line.strip() for line in open(archivo)]
    except IOError:
        None
    return lines

listMangaFile = readFile(CONST_MANGA_CFT_FILE)
#print listMangaFile
for mangaFileList in listMangaFile:
    mangaArray = []    
    mangaFileArray = mangaFileList.split("\t")
    for mangaField in mangaFileArray:
        if mangaField.strip() != "":
            mangaArray.append(mangaField)  
    if mangaArray.__len__() < 3:        
        mangaArray[mangaArray.__len__():3] = [None] * (3 - mangaArray.__len__())
    mangaCode = mangaArray[0].strip()    
    mangaUCode =  mangaArray[3].strip() if mangaArray.__len__() == 4 else  mangaCode    
    mangaObj = Manga(mangaCode, MANGA_DEFAULT_SERVER, mangaArray[1], mangaArray[2], mangaUCode)
    #print mangaObj
    mangas[mangaCode] = mangaObj

letras = map(chr, range(97, 101))
