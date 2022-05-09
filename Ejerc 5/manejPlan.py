import csv
from planAhorro import PlanA

class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []
        
    def __str__ (self):
        s = " "
        for plan in self.__lista:
            s += str( plan ) + '\n'
        return s
    
    def test (self):
        archivo = open( 'planes.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        b = True
        for fila in reader:
            if b:
                b = not b
            else:
                cod = int( fila[0] )
                modelo = fila[1]
                version = fila[2]
                prec = int( fila[3] )
                cantC = int( fila[4] )
                unPlan = PlanA( cod, modelo, version, prec, cantC )
                self.__lista.append( unPlan )
        archivo.close()
       
    def Actualizar (self): #opcion1
        for i in range( len( self.__lista ) ):
            print('----------> Plan ',i+1)
            print('Codigo: {} - Modelo: {} - Version: {}'.format( self.__lista[i].getCod(), self.__lista[i].getModelo(), self.__lista[i].getVersion() ))
            valor = int(input('Ingresa el nuevo valor del plan: '))
            self.__lista[i].setPrec( valor )
        print('***Valores actualizados correctamente ***')
        
    
    def MostrarValor (self): #opcion2
        prec = int(input('Ingrese un valor: '))
        b = 0
        for i in range( len( self.__lista ) ):
            valor = (self.__lista[i].getPrec() // self.__lista[i].getCantCuotas()) + self.__lista[i].getPrec() * 0.10
            print('valores',valor)
            if valor <= prec:
                b += 1
                print('-----> Plan valor: ',valor)
                print('Codigo: {} - Modelo: {} - Version: {}'.format( self.__lista[i].getCod(), self.__lista[i].getModelo(), self.__lista[i].getVersion() )) 
            
        if b == 0:
            print('No se encontro un valor menor al valor ingresado, lo sentimos.')    
            
    
    def MostrarMonto (self): 
          for i in range( len( self.__lista ) ):
              valorC = (self.__lista[i].getPrec() // self.__lista[i].getCantCuotas()) + self.__lista[i].getPrec() * 0.10
              monto = self.__lista[i].getCuotaLicitar() * valorC
              print('Para el plan {} se debe pagar: {}'.format( i + 1, monto ))
              
    def Modificar (self):
        cod = int(input('Ingrese el codigo de un plan: '))
        b = 0
        for i in range( len( self.__lista ) ):
            if cod == self.__lista[i].getCod():
                valor = int(input('Ingrese nuevo valor para las cuotas a licitar: '))
                self.__lista[i].setCuotaLicitar( valor )  #llama al metodo de clase set para cambiar el valor
                print('*** Valor actualizado ***')
                b += 1
        if b == 0:
            print('Codigo ingresado incorrecto')