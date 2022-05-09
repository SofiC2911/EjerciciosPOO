from manejPlan import Manejador
from menu import Menu

if __name__ == '__main__':
    listaPlan = Manejador()
    listaPlan.test()
    print(listaPlan)
    
    m = Menu()
    
    salir = False
    while not salir:
        print("---------------- MENU --------------")
        print('1 - Actualizar el valor del vahiculos \n2 - Mostrar por precio menor al ingresado \n3 - Mostrar monto que debe ser pagado \n4 - Modificar cuotas para licitar \n5 - Salir')
        opci = int(input('Ingrese opcion: '))
        m.opcion(opci,listaPlan)
        salir = opci == 4