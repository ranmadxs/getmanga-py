'''
Created on 26-03-2014

@author: esanchez
'''
import httplib2, re
from libs import log, funciones
from model.bean import Capitulo, Manga, Imagen
from model.TYPE import ParamDescarga
from model import TYPE

CONST_EXP_LST_CAPITULOS = '<a class="lst" href="(.+?)" title="(.+?)">'

def splittedname(s):
    return tuple(funciones.tryint(x) for x in re.split('([0-9]+)', s[0]))

def obtenerCapitulos(manga = Manga, urlCapitulos = '', parametros = ParamDescarga):
    codCapituloIni = parametros.codCapitulo
    pat = re.compile('<select class="cbo_wpm_chp" onchange="[^"]+">(.+?)</select>')
    http = httplib2.Http()
    headers, body = http.request(urlCapitulos)
    li = pat.findall(body)
    listCapsRet = []
    lst=[]
    strOption = str(li[0])
    strOption = strOption.replace('selected="selected"', '')
    pat2 = re.compile('<option value="(.+?)" >(.+?)</option>')
    lstCaps = pat2.findall(strOption)
    total = len(lstCaps)
    totPre = len(str(total))
    manga.length = total
#    print lstCaps
#    exit(0)
    if(total > 1):        
        lstCaps = sorted(lstCaps, key=splittedname)
    if(codCapituloIni is not None):
        for cap in lstCaps:
            codCap = funciones.prefijo(cap[0], totPre)
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
        capitulo = Capitulo(None, cap[1])
        capitulo.code = str(cap[0])
        capitulo.url = "%s%s/"%(manga.url, capitulo.code)
        lst.append(capitulo)        
    return lst, manga

def obtenerURLCaps(manga = Manga):
    pat = re.compile(CONST_EXP_LST_CAPITULOS)    
    urlCapitulo = None
    manga.url = 'http://%s/%s/'%(manga.site, manga.code)
    log.info("http.request[lstCapitulos] ==> %s"%manga.url)  
    http = httplib2.Http()
    headers, body = http.request(manga.url)
    varContenidoHtml = body        
    caps = pat.findall(varContenidoHtml)
    if caps != None:
        urlCapitulo = caps[0][0]
    return urlCapitulo
