#!/usr/bin/env python
from model import AbstractUtilDTO
class Manga(AbstractUtilDTO):
    CONSTANT_INFO_URL = "https://www.mangaupdates.com/series.html?id=%s"
    CONSTANT_MANGA_COVERS_URL = "http://mcd.iosphe.re/api/v1/series/%s/"
    id= ""
    site = ""    
    code = ""
    url = ""
    length = 0
    capitulos = []
    cover = None
    urlVolumen = None
    infoUrl = ""
    uCode = None
    def __init__(self, code=None, site=None, idManga=None, urlVolumen=None, uCode=None, length=0, url=None, capitulos = []):
        if (uCode == None):
            uCode = code
        self.uCode = uCode
        self.id = idManga
        self.code = code
        self.site = site
        self.urlVolumen = urlVolumen
        self.length=length
        self.url = url
        self.capitulos = capitulos
        if (not idManga is None and idManga != '0'):
            self.cover = (self.CONSTANT_MANGA_COVERS_URL%idManga)
        else:
            self.cover = None
        self.infoUrl = (self.CONSTANT_INFO_URL%idManga)
        
class Capitulo(AbstractUtilDTO):
    code = ""
    url = ""
    folder = ""
    title = ""
    length = 0
    imagenes = []
    def __init__(self, url=None, title=None, length = 0, imagenes = [], code=None, folder=None):
        self.url=url
        self.title=title
        self.length=length
        self.imagenes = imagenes
        self.code = code
        self.folder = folder

class Imagen(AbstractUtilDTO):
    code = ""
    url = ""
    title = ""
    path = ""
    urlReal = None
    def __init__(self, code=None, url=None, title=None, urlReal=None, path=None):
        self.url=url
        self.code=code
        self.urlReal = urlReal
        self.title=title
        self.path = path