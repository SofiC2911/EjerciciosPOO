import csv
from Meteorologia import Registro

class manejadorMeteo:
    __litaMes = []

    def __init__(self,D,H):
        
        self.__litaMes = [[0 for i in range (H)] for j in range (D)]
    
    def __str__(self): 

        s = ''
        for fila in range (len(self.__litaMes)):
            for columna in range (len(self.__litaMes[fila])):
                s += str(self.__litaMes[fila][columna]) + '\n'
        
        return s
    
    def testPrueba (self):
        archivo = open('Junio.csv')
        reader = csv.reader(archivo, delimiter = ',')
        b = True
        for fila in reader:
            if b:
                b = not b
            else:
                d = int(fila[0])  
                h = int(fila[1])   
                t = int(fila[2])   
                humed = int(fila[3])    
                p = int(fila[4])      
                unReg = Registro(t,humed,p)
                self.__listaMes[d-1][h] =unReg
        
        archivo.close()
    
    def maximo(self):
        tMax = 0
        huMax = 0
        pMax = 0

        for d in range(len(self.__listaMes)):
            for h in range(24):
                if tMax < self.__listaMes[d][h].getTem():
                    tMax = self.__listaMes[d][h].getTem()
                    diaT = d + 1
                    horaT = h
                if huMax < self.__listaMes[d][h].getHum():
                    humM = self.__listaMes[d][h].getHum()
                    diaH = d + 1
                    horaH = h
                if pMax < self.__listaMes[d][h].getPres():
                    pMax = self.__listaMes[d][h].getPres()
                    diaP = d + 1
                    horaP = h

        print('------------- Temperatura -------------')
        print('Dia {:2} hora {:2} - temperatura mayor: {:4}'. format( diaT, horaT, tMax ))
        
        print('------------- Humedad -------------')
        print('Dia {:2} hora {:2} - humedad mayor: {:4}'. format( diaH, horaH, huMax ))
        
        print('------------- Presion -------------')
        print('Dia {:2} hora {:2} - presion mayor: {:4}'. format( diaP, horaP, pMax ))
    
    def minimo (self): 
        tMin = 9999999
        huMin = 9999999
        pMin = 9999999
        for d in range( len( self.__listaMes ) ):
            for h in range( 24 ):
                if tMin > self.__listaMes[d][h].getTem():
                    tMin = self.__listaMes[d][h].getTem()
                    diaT = d + 1
                    horaT = h
                if huMin > self.__listaMes[d][h].getHum():
                    huMin = self.__listaMes[d][h].getHum()
                    diaH = d + 1
                    horaH = h
                if pMin > self.__listaMes[d][h].getPres():
                    pMin = self.__listaMes[d][h].getPres()
                    diaP = d + 1
                    horaP = h
        print('------------- Temperatura -------------')
        print('Dia {} hora {} - temperatura menor: {}'. format( diaT, horaT, tMin ))
        
        print('------------- Humedad -------------')
        print('Dia {} hora {} - humedad menor: {}'. format( diaH, horaH, huMin ))
        
        print('------------- Presion -------------')
        print('Dia {} hora {} - presion menor: {}'. format( diaP, horaP, pMin ))

    def Promedio (self):
        lisProm = [ 0 for i in range( 24 )]
        
        for d in range( len( self.__listaMes) ):
            for h in range( 24 ):
                lisProm[h] += self.__listaMes[d][h].getTemp()

        for i in range( 24 ):
            print('Hora {:2}:00 tuvo un promedio: {:6}'.format( i, lisProm[i]/2 ))
            
    def Mostrar (self):
        d = int(input('Ingrese un dia: '))
        print('{:2}    {:4}   {:6}   {:8}'.format('Hora', 'Temperatura', 'Humedad', 'Presion'))
        for h in range( 24 ):
             print('{:2}:00    {:4}   {:10}   {:8}'.format( h, self.__listaMes[d-1][h].getTemp(), self.__listaMes[d-1][h].getHum(), self.__listaMes[d-1][h].getPres()))