#from Meteorologia import Registro
from ManejadorRegMeteo  import manejadorMeteo

from menu import Menu

if __name__ == '__main__':
    D = 2 #usaremos solo 2 dias para el test de prueba
    H = 24

    ListaReg = manejadorMeteo(D,H)
    ListaReg.testPrueba()

    m = Menu()

    salir = False
    
    while not salir:
        print("---------------- MENU --------------")
        print('1 - Mostrar para cada variable el día y la hora de menor y mayor valor. \n2 - Indicar la temperatura promedio mensual por cada hora \n3 - Dado un número de día listar los valores de las 3 variables para cada hora del día dado. \n4 - Salir')
        opci = int(input('Ingrese opcion: '))
        m.opcion(opci,)
        salir = opci == 4