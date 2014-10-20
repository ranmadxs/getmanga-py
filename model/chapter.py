'''
Created on 22-09-2014

@author: esanchez
'''
from model import AbstractUtilDTO

class Volumen(AbstractUtilDTO):
    name = ""
    folder = ""
    capitulos = []
    def __init__(self, name=None, capitulos = [], folder = ""):
        self.name = name
        self.capitulos = capitulos
        self.folder = folder
        
class Capitulo(AbstractUtilDTO):
    name = ""
    folder = ""
    def __init__(self, name=None, folder=None):
        self.name = name
        self.folder = folder