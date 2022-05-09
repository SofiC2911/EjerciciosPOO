from medicamento import Medicamento
import csv

class ManejadorMed:
    __lista = []
    
    def __init__ (self):
        self.__lista = []
    
    def __str__ (self):
        s = ""
        for medicamento in self.__lista:
            s += str( medicamento ) + '\n'
        return s
    
    def agregar (self, unMedicamento):
        self.__lista.append( unMedicamento )
    
    def test (self):
        archivo = open( 'medicamentos.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                idC = int(fila[0])
                idM = int(fila[1])
                nom = fila[2]
                droga = fila[3]
                pre = fila[4]
                cant = fila[5]
                precio = int(fila[6])
                unMedicamento = Medicamento( idC, idM, nom, droga, pre, cant, precio )
                self.agregar( unMedicamento )
        archivo.close()
        
    def mostrar (self, idC):
        precio = 0
        print('{:20} {:20} {:14} {:14}'.format( 'Medicamento/Monodroga', 'Presentacion', 'Cantidad', 'Precio' ))
        for i in range( len( self.__lista ) ):
            if idC == self.__lista[i].getIdCama():
                precio += self.__lista[i].getPrecio()
                print('{:20} {:20} {:14} {:8}'.format( self.__lista[i].getNombre(), self.__lista[i].getPresentacion(), self.__lista[i].getCantidad(), self.__lista[i].getPrecio() ))
        print('Total adeudado: ', precio)