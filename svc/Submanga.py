'''
Created on 26-03-2014

@author: esanchez
'''
import httplib2, re
from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
from libs import log, funciones
from model import TYPE
#"http://submanga.com/claymore/completa"

def splittedname(s):
    return tuple(funciones.tryint(x) for x in re.split('([0-9]+)', s[0][0]))

def obtenerCapitulos(manga = Manga, urlCapitulos = '', parametros = ParamDescarga):
    codCapituloIni = parametros.codCapitulo
    pat = re.compile('<td class="s">(.+?)</td>')
    http = httplib2.Http()
    lstCaps = []
    listCapsRet=[]
    lst=[]
    log.info("http.request[lstCapitulos] ==> %s"%urlCapitulos) 
    headers, body = http.request(urlCapitulos)
    log.file(body)
    li = pat.findall("%s"%body)
    log.file(li)
    for elem in li:    
        strOption = str(elem)
        strOption = strOption.replace('<strong>', '')
        strOption = strOption.replace('</strong>', '')
        pat2 = re.compile('<a href="(.+?)">(.+?)</a>')
        cap = pat2.findall("%s"%strOption)
        lstCaps.append(cap)    
    total = len(lstCaps) 
    manga.length = total
    totPre = len(str(total))
#    print lstCaps
#    exit(0)
    if(total > 1):          
        lstCaps = sorted(lstCaps, key=splittedname)
    if(codCapituloIni is not None):
        for cap in lstCaps:
            codCap = cap[0][0].split("/")[-2]
            codCap = funciones.prefijo(codCap, totPre)
            capIni = funciones.prefijo(str(codCapituloIni), totPre)
            codCap = funciones.decode(codCap)
            if(parametros.tipo == TYPE.UNIQUE and codCap == capIni):
                listCapsRet.append(cap)
                break
            if (codCap >= capIni and parametros.tipo != TYPE.UNIQUE):
                listCapsRet.append(cap)
    else:
        listCapsRet = lstCaps

    
    for cap in listCapsRet:
        capitulo = Capitulo(cap[0][0], cap[0][1])
        #capitulo.url = "%s%s/"%(manga.url, capitulo.code)
        capitulo.code = capitulo.url.split("/")[-2]
        auxUri = capitulo.url.split("/")[-3]
        capitulo.url = capitulo.url.replace("%s/%s"%(auxUri, capitulo.code), "c")
        lst.append(capitulo)    
    return lst, manga

def obtenerURLCaps(manga = Manga):
    manga.url = 'http://%s/%s/completa'%(manga.site, manga.code)
    return manga.url