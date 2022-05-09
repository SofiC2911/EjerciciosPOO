class Conjunto:
    __lista = []
    
    def __init__(self, lista):
        self.__lista = lista
        
    def __str__(self):
        s = " { "
        for lista in self.__lista:
            s += str(lista) + " "
        return s + "}"
          
    def __add__ (self, otro):
        A = len( self.__lista )
        B = len( otro.__lista )
        i = 0
        j = 0
        conjuntoF = []
        while i < A and j < B:
            if self.__lista[i] < otro.__lista[j]:
                conjuntoF.append( self.__lista[i] )
                i += 1
            elif otro.__lista[j] < self.__lista[i]:
                conjuntoF.append( otro.__lista )
                j += 1
            else:
                conjuntoF.append( self.__lista[i] )
                i += 1
                j += 1
        if i < A:
            while i < A:
                conjuntoF.append( self.__lista[i] )
                i += i
        elif j < B:
            while j < B:
                conjuntoF.append( otro.__lista[j] )
                j += 1
        return conjuntoF
    
    def __sub__ (self, otro):
        conjuntoF = []
        for i in self.__lista:
            if i not in otro.__lista:
                conjuntoF.append( i )
        return conjuntoF #para que sea de tipo conjuntos retorno Conjunto( conjuntoF )
    
    def __eq__ (self, otro):
        return self.__lista == otro.__lista