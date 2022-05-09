#from ViajeroFrecuente import viajeroFrecuent
from ManejViajero import manejViaje
from menu import Menu

if __name__ == '__main__':

    listaViaje = manejViaje()

    listaViaje.CargaLV()

    print(listaViaje)

    m = Menu()

    numViajFre = int(input('Ingrese numero de viajero frecuente: '))
    while numViajFre>0:
        indice = listaViaje.BuscarIndice(numViajFre)
        
        if indice == -1:
            print('el numero ingresado no corresponde a ningun viajero frecuente')
        else:
            salir = False
            unViajero = listaViaje.BuscarViajero(indice)
            while not salir:
                print("---------------- MENU --------------")
                print('1 - Consultar cantidad de millas \n2 - Acumular millas \n3 - Canjear millas \n4 - Salir')
                opci = int(input('Ingrese opcion: '))
                m.opcion(opci,unViajero)
                salir = opci == 4
    
        numViajFre = int(input('Ingrese numero de viajero frecuente, ingreso finaliza con -1: '))
    
    listaViaje.MostrarLista()