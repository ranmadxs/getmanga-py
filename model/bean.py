#!/usr/bin/env python
from model import AbstractUtilDTO
class Manga(AbstractUtilDTO):
    CONSTANT_INFO_URL = "https://www.mangaupdates.com/series.html?id=%s"
    CONSTANT_MANGA_COVERS_URL = "http://manga.joentjuh.nl/series/%s/"
    id= ""
    site = ""
    code = ""
    url = ""
    length = 0
    capitulos = []
    cover = ""
    urlVolumen = None
    infoUrl = ""
    def __init__(self, code=None, site=None, idManga=None, urlVolumen=None, length=0, url=None, capitulos = []):
        self.id = idManga
        self.code = code
        self.site = site
        self.urlVolumen = urlVolumen
        self.length=length
        self.url = url
        self.capitulos = capitulos
        self.cover = (self.CONSTANT_MANGA_COVERS_URL%idManga)
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