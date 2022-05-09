from cama import Cama
import csv
import numpy as np

class ManejadorCama:
    __cantidad = 0
    __dimension = 0
    __incremento = 3
    
    def __init__ (self, dimension, incremento = 5):
        self.__arreglo = np.empty( dimension, dtype = Cama )
        self.__cantidad = 0
        self.__dimension = dimension
    
    def __str__ (self):
        s = ""
        for cama in self.__arreglo:
            s += str( cama ) + '\n'
        return s
    
    def agregar (self, unaCama):
        if self.__cantidad == self.__dimension: #pregunta cuando el arreglo inicial se lleno
            self.__dimension += self.__incremento
            self.__arreglo.resize( self.__dimension ) #agrega mas espacio de memoria
        self.__arreglo[ self.__cantidad ] = unaCama #asigna un objeto a la componente del arreglo
        self.__cantidad += 1
    
    def test (self):
        archivo = open( 'camas.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idC = int(fila[0])
                hab = int(fila[1])
                estado = bool(fila[2])
                nom = fila[3]
                diag = fila[4]
                ing = fila[5]
                alta = fila[6]
                aux = nom.split(',')
                nom = aux[0] + aux[1]
                unaCama = Cama( idC, hab, estado, nom, diag, ing, alta )
                self.agregar( unaCama )
        archivo.close()
    
    def mostrar (self, i):
        print('Paciente: {:10}    Cama: {:1}  Habitacion: {:2} '.format( self.__arreglo[i].getNombre(), self.__arreglo[i].getIdCama(), self.__arreglo[i].getHabitacion() ))
        print('Diagnostico: {:10}  Fecha de internacion: {:10}'.format( self.__arreglo[i].getDiagnostico(), self.__arreglo[i].getFechaI() ))
        print('Fecha de alta: {:2}'.format( self.__arreglo[i].getFechaA() ))
        self.__arreglo[i].setEstado( False )
        self.__arreglo[i].setNombre( None )

    def buscarNombre (self, nom):
        bandera = True
        i = 0
        idC = None
        while bandera and i < self.__cantidad:
            if nom == self.__arreglo[i].getNombre():
                bandera = False
                idC = self.__arreglo[i].getIdCama()
            else:
                i += 1
        if idC == None:
            print('El nombre solicitado no se encontro')
        else:
            return idC
        
    def darAlta (self, fecha, i):
        if type( fecha ) == str:
            self.__arreglo[i - 1].setFechaAlta( fecha )
            self.__arreglo[i - 1].setEstado( False )
            self.__arreglo[i - 1].setNombre( None )
            print('La fecha de alta se actualizo con exito!')
        else:
            print('Error de tipo al actualizar la fecha')
    
    def mostrarDiag(self, diag):
        cont  = 0
        for i in range( self.__cantidad ):
            if diag == self.__arreglo[i].getDiagnostico():
                if self.__arreglo[i].getEstado():
                    cont += 1
                    print('Paciente: {:10}    Cama: {:1}  Habitacion: {:2} Ingreso: {:4}'.format( self.__arreglo[i].getNombre(), self.__arreglo[i].getIdCama(), self.__arreglo[i].getHabitacion(), self.__arreglo[i].getFechaI() )) 
        if cont == 0:
            print('No se encontro ningun paciente con ese diagnostico')