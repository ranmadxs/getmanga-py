from libs import funciones
import config

codCarp = "a1"
cant = 4  
nomCarp = funciones.agregaCeros(codCarp, cant)

print "%s   ---->   %s"%(codCarp, nomCarp)

print config.VAR_MAIN_PATH