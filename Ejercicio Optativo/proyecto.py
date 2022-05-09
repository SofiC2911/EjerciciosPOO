class Proyecto:
    __idProyecto : str
    __titulo : str
    __palabraClave : str
    __puntos = int
    
    def __init__ (self, ide, titu, clave, punto):
        self.__idProyecto = ide 
        self.__titulo = titu
        self.__palabraClave = clave
        self.__puntos = 0
    
    def __str__ (self):
        return ('Id Proyecto: {} Titulo: {} Palabras Clave: {} Puntos: {}'.format( self.__idProyecto, self.__titulo, self.__palabraClave, self.__puntos ))
    
    def getIdProyecto (self):
        return self.__idProyecto
    
    def setPuntaje (self, num):
        if type( num ) == int:
            self.__puntos += num
            
    def __gt__ (self, otro):
        return self.__puntos > otro.__puntos