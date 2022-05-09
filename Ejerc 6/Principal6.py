from ManViajero import Manejador
from menu import Menu

if __name__ == '__main__':
    listaViajero = Manejador()
    listaViajero.test()
    #print( listaViajero )
    
    m = Menu()
    
    salir = True
    while salir:
        print('-------------------- MENU --------------------')
        print('1. Consultar cantidad de millas \n2. Acumular millas \n3. Canjear millas \n4. Salir')  
        op = input('Opcion: ')
        m.opcion( op, listaViajero )
        print( listaViajero )