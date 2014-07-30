'''
Created on 21-03-2014

@author: esanchez
'''
from model import AbstractUtilDTO

RECURSIVE = '-R'
UNIQUE = '-U'
CAPITULOS = '-C'
HELP = '--help'
H = '-h'

class ParamDescarga(AbstractUtilDTO):
    tipo=None
    codCapitulo = None
    
    def __init__(self, codCapitulo=None, tipo=None):
        self.tipo=tipo
        self.codCapitulo=codCapitulo
        