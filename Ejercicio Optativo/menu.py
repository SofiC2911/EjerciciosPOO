from ManProyecto import ManejadorP
from ManIntegrante import ManejadorI

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.salir
        }

    def opcion (self, op, objetoLista, objetoArreglo):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2':
            func( objetoLista, objetoArreglo )
        else:
            func()

    def opcion1 (self, objLista, objArreglo):  
        if type( objLista ) == ManejadorP and type( objArreglo ) == ManejadorI:
            print('************************* Punto 1 *************************')
            #corte de control
            for i in range( 3 ):
                num = objLista.obtenerId( i ) #obtengo el id de proyecto por el indice
                cant = objArreglo.ContarInte( num ) #obtengo la cantidad de integrantes por proyecto, le envio el id proyecto
                print('cantidad en menu ',cant)
                objLista.PuntoA( cant, i )  #carga el punto a por cantidad de integrantes
                bandera = objArreglo.obtenerDirector( num )
                objLista.puntoB( bandera, i )
                bandera = objArreglo.obtenerCoDirector( num )
                objLista.puntoC( bandera, i )
                flag = objArreglo.puntoDE( num )
                if flag == False:
                    objLista.puntoF()
        else:
            print('Error de tipo en menu')
        
    def opcion2 (self, objLista, objArreglo):  
        if type( objLista ) == ManejadorP and type( objArreglo ) == ManejadorI:
            print('************************* Punto 2 *************************')
            #sobrecarga __gt__ > mayor
            objLista.listar()
        else:
            print('Error de tipo en menu')
        
    def salir (self):
        print('Usted salio del programa')