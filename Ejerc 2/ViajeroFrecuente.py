class viajeroFrecuente:

    __numViajero = 0
    __dni = 0
    __nombre = ''
    __apellido = ''
    __millasAcum = 0
    
    def __init__(self,numV,dni,nomb,apel,milla):
        
        self.__numViajero = numV
        self.__dni = dni
        self.__nombre = nomb
        self.__apellido = apel
        self.__millasAcum = milla
    
    def cantidadTotalMillas(self):
        return self.__millasAcum
    
    def acumularMillas(self,cant):
        self.__millasAcum += cant
    
    def canjearMillas(self,canje):
        if canje <= self.__millasAcum:
            self.__millasAcum -= canje
            print('Sus millas fueron canjeadas con exito')
        else:
            print('Sus millas no son suficientes para ser canjeadas')
        
    def getIdViaje(self):
        return self.__numViajero