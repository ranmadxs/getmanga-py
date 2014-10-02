#!/usr/bin/env python
from model import AbstractUtilDTO
class Manga(AbstractUtilDTO):
    site = ""
    code = ""
    url = ""
    length = 0
    capitulos = []
    cover = ""
    urlVolumen = None
    infoUrl = ""
    def __init__(self, code=None, site=None, cover=None, urlVolumen=None, infoUrl=None, length=0, url=None, capitulos = []):
        self.code = code
        self.site = site
        self.urlVolumen = urlVolumen
        self.length=length
        self.url = url
        self.capitulos = capitulos
        self.cover = cover
        self.infoUrl = infoUrl
        
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