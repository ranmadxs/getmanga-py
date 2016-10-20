#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 20-10-2016

@author: esanchez
'''

import unittest
import Main
from libs.TestHelper import ParametrizedTestCase
from libs import MangaGet
from model.bean import Manga, Capitulo, Imagen
from config import mangas

class TestMainMethods(ParametrizedTestCase):
    
    def testInfoManga(self):   
        print self.param   
        mangaCode = self.param["mangaCode"]
        manga = mangas[mangaCode]
        Main.infoManga(manga)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestMainMethods, param={"mangaCode" : "sun_ken_rock"}))
    unittest.TextTestRunner(verbosity=2).run(suite)