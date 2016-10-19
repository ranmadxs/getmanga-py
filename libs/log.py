'''
Created on 17-03-2014

@author: esanchez
'''
import time 
import logging
import config
from libs.funciones import bcolors

#fileLog=open(archivoLog,'w')
fileTime =  time.strftime("%Y%m%d") 
logFileName = '%slogs/%s_%s'%(config.CONST_PATH, config.CONST_FILE_LOG, fileTime) 

logging.basicConfig(filename=logFileName,
                    level=logging.DEBUG, 
                    format='%(asctime)-1s [%(levelname)s] (%(name)s) : %(message)s'
                    )
def info(msg):    
    print (bcolors.OKBLUE +'[INFO]\t' +bcolors.ENDC+ str(msg))
    logging.info(msg)
    #fileLog.write('[INFO]\t' + text + "\n")
    #fileLog.flush()
    
def error(msg):    
    print (bcolors.FAIL +'[ERROR]\t' +bcolors.ENDC+ str(msg))
    logging.error(msg)
    #fileLog.write('[ERROR]\t' + text + "\n")
    #fileLog.flush()

def debug(msg):    
    print (bcolors.OKGREEN +'[DEBUG]\t' +bcolors.ENDC+ str(msg))
    logging.debug(msg)
    #fileLog.write('[DEBUG]\t' + text + "\n")
    #fileLog.flush()

def file(msg):
    logging.info(msg)   
    #print msg
    #logging.debug(" ## Guardado en Archivo disabled para file ##")
    
#TODO: Deo eliminar este metodo y los comentarios
def close():
    print ("close")
    #fileLog.close()