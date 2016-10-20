#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 20-10-2016

@author: esanchez
'''
import unittest

from libs import MangaGet
from model.bean import Manga, Capitulo, Imagen
from config import mangas


class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite

class TestMangaGetMethods(ParametrizedTestCase):
           
    def testObtenerCapitulo(self):   
        print self.param     
        capCode = self.param["capCode"]
        mangaCode = self.param["mangaCode"]
        manga = mangas[mangaCode]
        print "testObtenerCapitulo en server %s"%manga.site
        capitulo = MangaGet.obtenerCapitulo(manga, capCode)        
        self.assertEqual(capCode, capitulo.code, "El Capitulo %s no se ha encontrado en el servidor %s "%(capCode, manga.site))
        print "Capitulo = %s" % capitulo
  
    def testListaCapitulos(self):
        print self.param
        mangaCode = self.param["mangaCode"]
        manga = mangas[mangaCode]
        print "testListaCapitulos en server %s"%manga.site
        manga = MangaGet.lstCapitulos(manga)
        self.assertLess(1, len(manga.capitulos), "No se han encontrado capitulos en el servidor %s"%manga.site)
        print "total encontrado : %d" % len(manga.capitulos)
  
if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestMangaGetMethods, param={"mangaCode" : "sun_ken_rock", "capCode" : "7"}))
    suite.addTest(ParametrizedTestCase.parametrize(TestMangaGetMethods, param={"mangaCode" : "sun_ken_rock2", "capCode" : "7"}))
    unittest.TextTestRunner(verbosity=2).run(suite)
          