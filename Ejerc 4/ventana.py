class Ventana:
    __titulo = ''
    __xSI = 0
    __ySI = 0
    __xID = 0
    __yID = 0
    
    def __init__(self, titulo = None, xSI = 0, ySI = 0, xID = 500, yID = 500):
        self.__titulo = titulo
        self.__xSI = xSI
        self.__ySI = ySI
        self.__xID = xID
        self.__yID = yID
        
    def mostrar (self):
        print('Titulo {} \nCoordenada x superior izquierda {} Coordenada y superior izquierda {} \nCoordenada x inferior derecha {} Coordenada y inferior derecha {}'
              .format( self.__titulo, self.__xSI, self.__ySI, self.__xID, self.__yID ))
    
    def getTitulo (self):
        return self.__titulo
    
    def alto (self): #alto es el eje de las y
        res = self.__yID - self.__ySI
        return res
    
    def ancho (self): #ancho es el eje de las x
        res = self.__xID - self.__xSI
        return res
    
    def moverDerecha (self, num):   
        if self.__xSI + num <= 500 and self.__xID + num <= 500:
            self.__xSI += num
            self.__xID += num
        else:
             print('No se puede mover la ventana, Error')
             
    def moverIzquierda (self, num):
        if self.__xSI - num >= 0 and self.__xID - num >= 0:
            self.__xSI -= num
            self.__xID -= num
        else:
             print('No se puede mover la ventana, Error')
             
    def bajar (self, num = 0):
        if self.__yID + num <= 500 and self.__ySI + num <= 500:
            self.__ySI += num
            self.__yID += num
        else:
            print('No se puede mover la ventana, Error')
            
    def subir (self, num = 0):
        if self.__yID - num >= 0 and self.__ySI - num:
            self.__ySI -= num
            self.__yID -= num
        else:
            print('No se puede mover la ventana, Error')