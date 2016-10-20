#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 20-10-2016

@author: esanchez
'''
import unittest

from libs.TestHelper import ParametrizedTestCase
from libs import MangaGet
from model.bean import Manga, Capitulo, Imagen
from config import mangas


class TestMangaGetMethods(ParametrizedTestCase):
           
    def testObtenerCapitulo(self):   
        print self.param     
        capCode = self.param["capCode"]
        mangaCode = self.param["mangaCode"]
        manga = mangas[mangaCode]
        #print "testObtenerCapitulo en server %s"%manga.site
        capitulo = MangaGet.obtenerCapitulo(manga, capCode)        
        self.assertEqual(capCode, capitulo.code, "El Capitulo %s no se ha encontrado en el servidor %s "%(capCode, manga.site))
        #print "Capitulo = %s" % capitulo
  
    def testListaCapitulos(self):
        print self.param
        mangaCode = self.param["mangaCode"]
        manga = mangas[mangaCode]
        #print "testListaCapitulos en server %s"%manga.site
        manga = MangaGet.lstCapitulos(manga)
        self.assertLess(1, len(manga.capitulos), "No se han encontrado capitulos en el servidor %s"%manga.site)
        #print "total encontrado : %d" % len(manga.capitulos)
        
    def testListaImagenes(self):
        print self.param
        capCode = self.param["capCode"]
        mangaCode = self.param["mangaCode"]
        manga = mangas[mangaCode]
        capitulo = MangaGet.obtenerCapitulo(manga, capCode)
        capitulo = MangaGet.lstImagenes(manga, capitulo)
        self.assertLess(1, len(capitulo.imagenes), "No se han encontrado capitulos en el servidor %s"%manga.site)
  
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestMangaGetMethods, param={"mangaCode" : "sun_ken_rock", "capCode" : "7"}))
    suite.addTest(ParametrizedTestCase.parametrize(TestMangaGetMethods, param={"mangaCode" : "sun_ken_rock2", "capCode" : "7"}))
    unittest.TextTestRunner(verbosity=2).run(suite)
          