class Integrante:
    __idProyecto: str
    __AyN : str
    __dni: str
    __categoria : str
    __rol : str
    
    def __init__ (self, id, ayn, dni, cat, rol):
        self.__idProyecto = id
        self.__AyN = ayn
        self.__dni = dni
        self.__categoria = cat
        self.__rol = rol
    
    def __str__ (self):
        return ('Id Proyecto: {} Apellido y Nombre: {} Dni: {} Categoria: {} Rol: {}'.format( self.__idProyecto, self.__AyN, self.__dni, self.__categoria, self.__rol ))
    
    def getIdProyecto (self):
        return self.__idProyecto
    
    def getRol (self):
        return self.__rol
    
    def getCategory (self):
        return self.__categoria