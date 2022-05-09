from ManIntegrante import ManejadorI
from ManProyecto  import ManejadorP
from menu import Menu

if __name__ == '__main__':
    #primer cosa que tengo que hacer es actualizar el valor del auto
    listaProyecto = ManejadorP()
    listaProyecto.test()  #punto 1
    print( listaProyecto )
    
    arregloIntegrante = ManejadorI( 11, 6 )
    arregloIntegrante.test()  #punto 2
    print( arregloIntegrante )
        
    menu = Menu()
    
    salir = False
    while not salir:
        print('-------------------- MENU --------------------')
        print('1. Calculas los puntos por Proyecto')
        print('2. Listar los datos de los Proyectos ordenados')
        print('3. Salir')
        
        op = input('Opcion: ')
        salir = menu.opcion( op, listaProyecto, arregloIntegrante )
        print( listaProyecto )