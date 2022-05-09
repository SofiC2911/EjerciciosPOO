import csv
from ViajeroFrecuente import viajeroFrecuente

class manejViaje:
    __listaV = []


    def __init__(self):
        self.__listaV = []
    
    def CargaLV(self):
        archivo = open('RegViajeros.csv')
        reader = csv.reader(archivo,delimiter=';')

        b = True

        for i in reader:
            if b:
                b= not b
            else:
                num = int(i[0])
                dni = i[1]
                nomb = i[2]
                apell = i[3]
                milla = int(i[4])
                unViaj = viajeroFrecuente(num,dni,nomb,apell,milla)
                self.__listaV.append(unViaj)
        
        archivo.close()
    
    def BuscarIndice(self, numViaj):
        if (type(numViaj) == int):
            indice = -1
            for i, obViaj in (enumerate(self.__listaV)):
                if obViaj.getIdViaje() == numViaj:
                    indice = i
                    #return indice
        else:
            print('Parametros de tipo incorrecto')
            indice = -1
        
        return indice
    
    def BuscarViajero(self,ind):
        if (type(ind) == int):
            viajero = self.__listaV[ind]
            return viajero
    
    def MostrarLista(self):
        print(self.__listaV[:4])
    