import csv
from viajero import Viajero

class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def __str__(self):      #muestra informacion de la lista
        s = ""
        for viajero in self.__lista:
            s += str( viajero ) + '\n'
        return s
        
    def agregarViajero (self, viajero): #agrega un viajero a la lista
        self.__lista.append(viajero)
        
    def test (self): #instancia los objetos con la informacion del csv
        archivo = open( 'registroViajeros.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                ide = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millas = int(fila[4])
                unViajero = Viajero( ide, dni, nombre, apellido, millas )
                self.agregarViajero( unViajero )
        archivo.close()

    def buscarIndice(self, clave):
        i = 0
        while i < len(self.__lista):
            if self.__lista[i].getIdentificador() == clave:
                return i
            i = i + 1        
            
    def getViajero (self, indice): #dado un indice devuelve el objeto solicitado
        print('esto es getViajero', self.__lista[indice])
        return self.__lista[ indice ]
    
    def comparar (self, viajero):
        for i in range( len( self.__lista ) ):
            if viajero == self.__lista[i].getcantidadMillas():
                print('izquierda',viajero, self.__lista[i].getcantidadMillas())
            # if self.__lista[i].getcantidadMillas() == viajero:
            #     print('derecha',viajero, self.__lista[i].getcantidadMillas())

    def acumularMillas (self, acum, viajero, indice): #opcion2
        viajero = acum + viajero 
        self.__lista[indice] = viajero
        print(viajero)
        print('Valor de millas actualizado con exito!')

    def canjearMillas(self, canje, viajero, indice):
        if viajero >= canje:
            viajero = canje - viajero
            self.__lista[indice] = viajero
            print(viajero)
            print('Valores de millas actualizado, el canje se realizo con exito!')
        else:
            print('Error al canjear millas, no posee las suficientes para canjear')  