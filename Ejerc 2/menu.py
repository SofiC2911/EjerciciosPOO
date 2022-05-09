from ViajeroFrecuente import viajeroFrecuente

class Menu:
    def __init__(self):
        self.__switcher = {1:self.opcion1,
                           2:self.opcion2,
                           3:self.opcion3,
                           4:self.salir
                           }
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self,op,obViaj):
        if (type(obViaj) == viajeroFrecuente) and (type(op) == int):
            func=self.__switcher.get(op, lambda: print("Opción no válida"))
            func(obViaj)
        else:
            print('Parametros de tipo incorrecto')
    
    def opcion1(self,obViaj):
        if type(obViaj) == viajeroFrecuente:
            #cantidad = obViaj.cantidadTotalMillas()
            print('Las cantidades de millas recorridas es de: ', obViaj.cantidadTotalMillas()) #cantidad
        else:
            print('error de parametro en opcion 1')
    
    def opcion2(self,obViaj):
        if type(obViaj) == viajeroFrecuente:
            cant = int(input('Ingrese cantidad de millas a acumular: '))
            obViaj.acumularMillas(cant)
        else:
            print('error de parametro en opcion 2')

    def opcion3(self,obViaj):
        if type(obViaj) == viajeroFrecuente:
            cantCanje = int(input('Ingrese cantidad de millas a canjear: '))
            obViaj.canjearMillas(cantCanje)
        else:
            print('error de parametro en opcion 3')
    
    def salir(self,obViaj):
        print('Salio de la aplicacion')