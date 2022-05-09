class Medicamento:
    __idCama = int
    __idMedicamento = int
    __nombre = str
    __monodroga = str
    __presentacion = str
    __cantAplicada = str
    __precio = float
    
    def __init__ (self, idcama, idmed, nombre, droga, prese, cant, precio):
        self.__idCama = idcama
        self.__idMedicamento = idmed
        self.__nombre = nombre
        self.__monodroga = droga
        self.__presentacion = prese
        self.__cantAplicada = cant 
        self.__precio = precio
        
    def __str__ (self):
        return 'Id Cama:{} id Med:{} Nombre:{} Droga:{} Presentacion:{} Cant:{} Precio:{}'.format( self.__idCama, self.__idMedicamento, self.__nombre, self.__monodroga, self.__presentacion, self.__cantAplicada, self.__precio )
    
    def getIdCama (self):
        return self.__idCama
    
    def getNombre (self):
        return self.__nombre
    
    def getPresentacion (self):
        return self.__presentacion
    
    def getCantidad (self):
        return self.__cantAplicada
    
    def getPrecio (self):
        return self.__precio