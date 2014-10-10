class AbstractUtilDTO:
    def __init__(self, dictionary = None):
        if dictionary != None:
            for k, v in dictionary.items():
                setattr(self, k, v)
                
                
    def __str__(self):
        var = ""
        elementos = []
        quote='"'
        for k, v in self.__dict__.items():
            if isinstance(v, list):               
                lista = []
                for elem in getattr(self, k, v):
                    lista.append(str(elem))    
                elementos.append('"%s":[%s]'% (k, ', '.join(lista)))
            else:
                uquo = ''
                valor = getattr(self, k, v)
                #and not (valor is None))
                if isinstance(v, str) or (valor is None):  
                    uquo = quote
                strValue = '"%s":&q%s&q'%(k, str(valor))
                #quote = '"%s":&quote%s&quote'%(k, str(getattr(self, k, v)))
                strValue = strValue.replace("&q", uquo)
                elementos.append(strValue)
        var = var + ', '.join(elementos)    
        #return "\n%s={%s}" % (self.__class__, var)
        return "{%s}" % (var)