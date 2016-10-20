'''
Created on 29-10-2014

@author: esanchez
'''

from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
import HTMLParser
import httplib2, re
from libs import log, funciones
from model import TYPE

def obtenerImagenes(capitulo = Capitulo, manga = Manga):
    http = httplib2.Http()
    parser = esMangaHTMLImgsParser(manga, capitulo)    
    http = httplib2.Http()
    headers, body = http.request(capitulo.url)
    parser.feed("%s"%body)  
    return parser.IMAGENES    

def obtenerURLCap(manga = Manga, uri = None, capitulo = Capitulo):
    url = 'http://%s/manga/%s/c%s/%s'%(manga.site, manga.code, capitulo.code, uri)    
    return url 

def obtenerURLCaps(manga = Manga):
    manga.url = 'http://%s/manga/%s'%(manga.site, manga.code)
    return manga.url

def obtenerCapitulos(manga = Manga, urlCapitulos = '', parametros = ParamDescarga):
    lst=[]
    listCapsRet = []    
    codCapituloIni = parametros.codCapitulo
    parser = esMangaHTMLParser(manga)    
    http = httplib2.Http()
    log.info("http.request[lstCapitulos] ==> %s"%urlCapitulos) 
    headers, body = http.request(manga.url)
    parser.feed("%s"%body)
    for capitulo in parser.CAPITULOS:
        strUrl = capitulo.url
        res = strUrl.split("/")[-1]
        res = res.replace("c", "", 1)        
        capitulo.code = res
        capitulo.title = "%s %s"%(capitulo.title, capitulo.code)
        lst.append(capitulo)
        
    total = len(lst)
    totPre = len(str(total))
    lstAux = []
    index = 0
    for cap in lst:
        encontrado = False
        codCapOrig = funciones.prefijo(str(cap.code), totPre)
        for capAux in lstAux:
            codCapAux = funciones.prefijo(str(capAux.code), totPre)
            if codCapOrig < codCapAux:
                index = lstAux.index(capAux)
                encontrado = True
                break
        if not encontrado:
            lstAux.append(cap)
        else:
            lstAux.insert(index, cap)
    lst = lstAux    
    if(codCapituloIni is not None):
        capIni = funciones.prefijo(str(codCapituloIni), totPre)
        for cap in lst:
            codCap = funciones.prefijo(cap.code, totPre)
            if(parametros.tipo == TYPE.UNIQUE and codCap == capIni):
                listCapsRet.append(cap)
                break
            if (codCap >= capIni and parametros.tipo != TYPE.UNIQUE):
                listCapsRet.append(cap)            
    else:
        listCapsRet = lst
    manga.length = len(lst)        
    return listCapsRet, manga

class esMangaHTMLImgsParser(HTMLParser.HTMLParser):
    def __init__(self, manga=Manga, capitulo = Capitulo):
        self.manga = manga
        self.capitulo = capitulo
        self.reset()
        self.IMAGEN_ACTUAL = None
        self.IMAGENES = []
        self.VALIDTAG = False   
        self.VALID_IMAGEN = False
        self.INIT = False 
        self.TERMNADO = False
        self.countSelect = 0
    def handle_starttag(self, tag, attrs):
        if self.TERMNADO:
            return
        if tag == 'select' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'form-control page':
            #print '************************* Inicio listado de imagenes *******************************'
            self.INIT = True
            self.countSelect = self.countSelect + 1
        if not self.INIT:
            self.VALIDTAG = False
            return
        #print "<%s>%s"% (tag, attrs)
            
        if tag == 'option' and len(attrs) > 0 and attrs[0][0] == 'value':
            self.VALID_IMAGEN = True         
            self.IMAGEN_ACTUAL = Imagen()
            self.IMAGEN_ACTUAL.url = obtenerURLCap(self.manga, attrs[0][1], self.capitulo)
           # print "<%s>%s"% (tag, attrs)
        
        self.VALIDTAG = True        
    def handle_endtag(self, tag):
        #if tag == 'option':
        #    self.VALID_IMAGEN = False
        if not self.INIT:
            return
        #print "</%s>"%tag
        if tag == 'select':
            self.INIT = False
            self.TERMNADO = True   
            #print '************************* Fin listado de imgs *******************************'        
    def handle_data(self, data):
        if(not self.VALIDTAG):
            return
        if self.VALID_IMAGEN:
            content = ("%s"%data).strip()
            self.IMAGEN_ACTUAL.title = content
            self.IMAGEN_ACTUAL.code = content    
            
            self.IMAGENES.append(self.IMAGEN_ACTUAL)
            self.VALID_IMAGEN = False
            #print content.strip()

class esMangaHTMLParser(HTMLParser.HTMLParser):
    def __init__(self, manga=Manga):
        self.manga = manga
        self.reset()
        self.CAPITULO_ACTUAL = None
        self.CAPITULOS = []
        self.VALIDTAG = False   
        self.VALID_CAPITULO = False
        self.INIT = False 
    def handle_starttag(self, tag, attrs):
        if tag == 'ul' and len(attrs) > 0 and attrs[0][0] == 'class' and attrs[0][1] == 'lstepis':
            self.INIT = True
        if not self.INIT:
            self.VALIDTAG = False
            return
           
        if tag == 'a' and len(attrs) > 1 and attrs[0][0] == 'href' and attrs[1][0] == 'class':
            self.VALID_CAPITULO = True         
            self.CAPITULO_ACTUAL = Capitulo()
            self.CAPITULO_ACTUAL.url = attrs[0][1]
            #print "<%s>%s"% (tag, attrs)
        
        self.VALIDTAG = True        
    def handle_endtag(self, tag):
        if not self.INIT:
            return
        if tag == 'ul':
            self.INIT = False    
 
    def handle_data(self, data):
        if(not self.VALIDTAG):
            return
        if self.VALID_CAPITULO :
            content = ("%s"%data).strip()
            self.CAPITULO_ACTUAL.title = content
            self.CAPITULOS.append(self.CAPITULO_ACTUAL)
            self.VALID_CAPITULO = False
            #print content.strip()   