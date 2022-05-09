class Cama:
    __idCama = int
    __habitacion = int
    __estado = bool
    __NyA = str
    __diagnostico = str
    __fechaI = str
    __fechaA = str
    
    def __init__ (self, idcama, habitacion, estado, nya, diag, fechaI, fechaA):
        self.__idCama = idcama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__NyA = nya
        self.__diagnostico = diag
        self.__fechaI = fechaI
        self.__fechaA = fechaA
        
    def __str__ (self):
        return 'Id Cama:{} hab:{} estado:{} AyN:{} diag:{} Ingreso:{} Alta:{}'.format( self.__idCama, self.__habitacion, self.__estado, self.__NyA, self.__diagnostico, self.__fechaI, self.__fechaA )
    
    def getNombre (self):
        return self.__NyA
    
    def setFechaAlta (self, fecha):
        self.__fechaA = fecha
        
    def getIdCama (self):
        return self.__idCama
    
    def getHabitacion (self):
        return self.__habitacion
    
    def getDiagnostico (self):
        return self.__diagnostico
    
    def getFechaI (self):
        return self.__fechaI
    
    def getFechaA (self):
        return self.__fechaA
    
    def setNombre (self, nom): #cambia a None
        self.__NyA = nom
        
    def setEstado (self, valor):  #cambia a False
        self.__estado = valor

    def getEstado (self):
        return self.__estado