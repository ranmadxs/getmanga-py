'''
Created on 22-09-2014

@author: esanchez
'''
from model import AbstractUtilDTO

class Volumen(AbstractUtilDTO):
    name = ""
    capitulos = []
    def __init__(self, name=None, capitulos = []):
        self.name = name
        self.capitulos = capitulos
        
class Capitulo(AbstractUtilDTO):
    name = ""
    def __init__(self, name=None):
        self.name = name