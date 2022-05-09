import csv
import numpy as np
from integrante import Integrante

class ManejadorI:
    __cantidad = 0
    __dimension = 0
    __incremento = 11
    
    def __init__ (self, dimension, incremento = 11):
        self.__arreglo = np.empty( dimension, dtype = Integrante )
        self.__cantidad = 0
        self.__dimension = dimension
        
    def __str__ (self):
        s = ""
        for integrante in self.__arreglo:
            s += str( integrante ) + '\n'
        return s
    
    def agregar (self, unIntegrante):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize( self.__dimension )
        self.__arreglo[ self.__cantidad ] = unIntegrante
        self.__cantidad += 1
    
    def test (self):
        archivo = open( 'integrantesProyecto.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera =  True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                ide = fila[0]
                nom = fila[1]
                dni = fila[2]
                cat = fila[3]
                rol = fila[4]
                unIntegrante = Integrante( ide, nom, dni, cat, rol )
                self.agregar( unIntegrante )
        archivo.close()
    
    def ContarInte(self, ide):
        if type( ide ) == str:
            cont  = 0
            for i in range( self.__cantidad ):
                if self.__arreglo[i].getIdProyecto() == ide:
                    cont += 1
            return cont
        else:
            print('error de tipo en contar los ids')
    
    def obtenerDirector (self, ide): #recibo el id de proyecto
        bandera = False
        i = 0
        while bandera == False and i < self.__cantidad:
            if self.__arreglo[i].getIdProyecto() == ide:
                if self.__arreglo[i].getRol() == 'director':
                    if self.__arreglo[i].getCategory() == 'I' or self.__arreglo[i].getCategory() == 'II':
                        bandera = not bandera
            i += 1
        return bandera
    
    def obtenerCoDirector (self, ide):
        bandera = False
        i = 0
        while bandera == False and i < self.__cantidad:
            if self.__arreglo[i].getIdProyecto() == ide:
                if self.__arreglo[i].getRol() == 'codirector':
                    if self.__arreglo[i].getCategory() == 'I' or self.__arreglo[i].getCategory() == 'II' or self.__arreglo[i].getCategory() == 'III':
                        bandera = not bandera
            i += 1
        return bandera
    
    def puntoDE (self, ide):
        dire = 0
        co = 0
        ambos = 0
        i = 0
        while i < self.__cantidad:
            if self.__arreglo[i].getIdProyecto() == ide:
                if self.__arreglo[i].getRol() == 'codirector':
                    co = 1
                elif self.__arreglo[i].getRol() == 'director':
                    dire = 1
            i += 1
            
        if co == 0 and dire == 0:
            print('no tiene ninguno de los 2')
            return False
        elif co == 0:
            print('El Proyecto debe tener un Codirector')
        elif dire == 0:
            print('El Proyecto debe tener un Director')