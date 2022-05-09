class PlanA:
    __codigo = 0
    __modelo = ''
    __version = ''
    __precio = 0
    __cantCuotas = 84 
    __cuotaLicitar = 15 
    
    def __init__(self, cod, modelo, version, prec, cuotas):
        self.__codigo = cod
        self.__modelo = modelo
        self.__version = version
        self.__precio = prec
        self.__cantCuotas = cuotas
                
    @classmethod
    def getCuotaLicitar (cls):
        return cls.__cuotaLicitar  
    
    @classmethod
    def setCuotaLicitar (cls, valor):
        if type( valor ) == int:
            cls.__cuotaLicitar =   valor   
        
    @classmethod
    def getCantCuotas (cls):
        return cls.__cantCuotas      
                
    def __str__ (self): 
        return '{} {} {} {} {} {} '.format(self.__codigo, self.__modelo, self.__version, self.__precio, self.getCantCuotas(), self.getCuotaLicitar())
    
    def getCod (self):
        return self.__codigo
    
    def getModelo (self):
        return self.__modelo
    
    def getVersion (self):
        return self.__version
    
    def setPrec(self, valor):
        if type( valor ) == int:
            self.__precio = valor
        else:
            print('Error de tipo en plan ahorro')
    
    def getPrec (self):
        return self.__precio