from manejPlan import Manejador

class Menu:

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.opcion4,
            '5': self.salir
        }

    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self,op,obLista):
        if (type(obLista) == Manejador) and (type(op) == int):
            func=self.__switcher.get(op, lambda: print("Opción no válida"))
            func(obLista)
        else:
            print('Parametros de tipo incorrecto')

    def opcion1 (self, obLista):  
        if type( obLista ) == Manejador:
            print('************************* Actualizacion *************************')
            obLista.Actualizar()
        else:
            print('Error de tipo en menu')
        
    def opcion2 (self, obLista): 
        if type( obLista ) == Manejador:
            print('************************* Mostrar valor de cuota inferior al ingresado *************************')
            obLista.MostrarValor()
        else:
            print('Error de tipo en menu')
        
    def opcion3 (self, obLista): 
        if type( obLista ) == Manejador:
            print('************************* Mostrar monto para licitar vehiculo *************************')
            obLista.MostrarMonto()
        else:
            print('Error de tipo en menu')
    
    def opcion4 (self, obLista):
        if type( obLista ) == Manejador:
            print('************************* Mosdificar cantidad de cuotas a licitar *************************')
            obLista.Modificar()
        else:
            print('Error de tipo en menu')
        
    def salir (self, obLista):
        print('Usted salio de la aplicación')
