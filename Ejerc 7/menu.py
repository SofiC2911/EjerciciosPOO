from ManViajero import Manejador
from os import system

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.salir,
        }

    def opcion (self, op, objetoLista):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2' or op == '3':
            func( objetoLista )
        else:
            func()
                
    def opcion1 (self, objV): #quien tiene igual cantidad de millas opcion1
        #system('cls')
        print('**** Comparar Millas ****')
        num = int(input('Ingrese el numero del viajero: '))
        i = objV.buscarIndice( num )
        viajero = objV.getViajero( i )
        print(viajero)
        #millas = int(input('Ingrese cantidad de millas recorridas que desea comparar: '))
        objV.comparar( viajero )

    def opcion2 (self, objV): #acumular millas opcion2
        #system('cls')
        print('**** Acumular Millas ****')
        num = int(input('Ingrese el numero del viajero: '))
        i = objV.buscarIndice( num )
        viajero = objV.getViajero( i )
        print(viajero)
        acum = int(input('Ingrese cantidad de millas recorridas que desea acumular: '))
        objV.acumularMillas(acum, viajero, i)

    def opcion3 (self, objV): #canjear millas opcion3
        #system('cls')
        print('**** Canjear Millas ****')
        num = int(input('Ingrese el numero del viajero : '))
        i = objV.buscarIndice( num )
        viajero = objV.getViajero( i )
        print(viajero)
        canje = int(input('Ingrese cantidad de millas a canjear: '))
        objV.canjearMillas( canje, viajero, i )
        
    def salir (self):
        print('Salir')