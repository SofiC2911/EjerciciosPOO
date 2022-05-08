from email import Email

import csv

class Manejador:
    __lista = []
    
    def __init__(self):
        self.__lista = []

    def agregarCorreo (self, unEmail):
        self.__lista.append( unEmail )
    
    def verificar(self,unEmail,password):
        if type( unEmail ) == str:
            if unEmail.find('@') != -1:
                aux = unEmail.split('@')
                idC = aux[0]
                if aux[1].find('.') != -1:
                    domTipoDom = aux[1].split('.')
                    dom = domTipoDom[0]
                    tipoDom = domTipoDom[1]
                    otroEmail = Email( idC, dom, tipoDom, password)
                    return otroEmail
                else:
                    print('Error al crear correo, no posee dom o tipo dominio ---->', unEmail)
            else:
                print('Error al crear correo, no posee @ o idCuenta ---->', unEmail)
        else:
            print('Error de tipo en verificar cuenta')
                
    def crearCorreo(self):
        archi = open('RegistroCorreo.csv')
        reader = csv.reader(archi,delimiter=';')
        b = True
        for i in reader:
            if b:
                b = not b
            else:
                mail = i[0]
                v = self.verificar(mail,i[1])
                if v:

    def buscarRepetido(self):
        archi = open('RegistroCorreo.csv')
        reader = csv.reader(archi,delimiter=';')
        c = 0
        b = True
        dom = input('ingrese dominio a buscar: ')
        for i in reader:
            if b:
                b = not b
            elif i[1] == dom:
                c += 1
    
        print ('el dominio solicitado se repite {} veces'.format(c))
        archi.close()