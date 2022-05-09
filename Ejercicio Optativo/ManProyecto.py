import csv
from proyecto import Proyecto

class ManejadorP:
    __lista = []
    
    def __init__ (self):
        self.__lista = []
        
    def __str__ (self):
        s = ""
        for proyecto in self.__lista:
            s += str( proyecto ) + '\n'
        return s
    
    def agregar (self, unProyecto):
        self.__lista.append( unProyecto )
    
    def test (self):
        archivo = open( 'proyectos.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                ide = fila[0]
                titulo = fila[1]
                palabra = fila[2]
                unProyecto = Proyecto( ide, titulo, palabra, 0 )
                self.agregar( unProyecto )
        archivo.close()
        
    def obtenerId (self, i):
        return self.__lista[i].getIdProyecto()
    
    def PuntoA (self, cant, i):
        if type( cant ) == int:
            if cant >= 3:
                self.__lista[i].setPuntaje( 10 )
            elif cant < 3:
                self.__lista[i].setPuntaje( -20 )
            else:
                print('El Proyecto debe tener como mínimo 3 integrantes') 
        else:
            print('error de tipo en punto a')
            
    def puntoB (self, bandera, i):
        if type( bandera ) == bool:
            if bandera:
                self.__lista[i].setPuntaje( 10 )
            else:
                self.__lista[i].setPuntaje( -5 )
                print('El Director del Proyecto debe tener categoría I o II.')
        else: 
            print('error de tipo en punto b')
            
    def puntoC (self, bandera, i):
        if type( bandera ) == bool:
            if bandera:
                self.__lista[i].setPuntaje( 10 )
            else:
                self.__lista[i].setPuntaje( -5 )
                print('El Codirector del Proyecto debe tener como mínimo categoría III')
        else: 
            print('error de tipo en punto b')
    
    def puntoF (self, i):
        self.__lista[i].setPuntaje( -10 )
        
    def listar (self):
        primero = 0
        for i in range( 1, 2 ):
            if self.__lista[primero] > self.__lista[i]:
                print(self.__lista[primero])
                primero += 1
            elif self.__lista[i] > self.__lista[primero]:
                print(self.__lista[i])
                primero += 1
            else:
                primero += 1