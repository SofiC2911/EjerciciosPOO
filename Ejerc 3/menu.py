from ManejadorRegMeteo import manejadorMeteo


class Menu:
    def __init__(self):
        self.__switcher = {1:self.opcion1,
                           2:self.opcion2,
                           3:self.opcion3,
                           4:self.salir
                           }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self,op,obList):
        if (type(obList) == manejadorMeteo) and (type(op) == int):
            func=self.__switcher.get(op, lambda: print("Opción no válida"))
            func(obList)
        else:
            print('Parametros de tipo incorrecto')
        
    def salir(self):
        print('Salio de la aplicacion')
        
    def opcion1(self,obList):
        if type(obList) == manejadorMeteo:
            print('---------------- MAXIMO -------------  ')
            obList.Maximo()
            print('---------------- MINIMO -------------  ')
            obList.Minimo()
        else:
            print('Error de parametro en opción')
    
    def opcion2(self,obList):
        if type(obList) == manejadorMeteo:
            obList.Promedio()
        else:
            print('Error de parametro en opción')
    
    def opcion3(self,obList):
        if type(obList) == manejadorMeteo:
            obList.Mostrar()
        else:
            print('Error de parametro en opción')