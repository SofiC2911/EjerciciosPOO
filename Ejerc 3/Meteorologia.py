class Registro:
    __temperatura: 0
    __humedad: 0
    __presion: 0

    def __init__(self,t,h,p):
        self.__temperatura = t
        self.__humedad = h
        self.__presion = p
    
    def __str__(self):
        return ('Temperatura {} - Humedad {} - Presion {}'.format(self.__temperatura,self.__humedad,self.__presion))
    
    def getTemp(self):
        return self.__temperatura
    
    def getHum(self):
        return self.__humedad
    
    def getPres(self):
        return self.__presion