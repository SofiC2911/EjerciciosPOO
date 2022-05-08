import re, csv

class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __contraseña = ''

    def __init__(self, id, dominio,tipoD,contrase):
        self.__idCuenta = id
        self.__dominio = dominio
        self.__tipoDom = tipoD
        self.__contraseña = contrase
    
    def __str__(self):
        return "%s %s %s %s " % (self.__idCuenta, self.__dominio, self.__tipoDom, self.__contraseña)
    
    def retornaEmail(self):
        return self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDom
    
    def getDominio(self):
        return self.__dominio
    
    def cambiarContra(self):
        cont = input('contraseña actual: ')
        
        if (cont == self.__contraseña):
            nueva = input('Nueva contraseña: ')
            self.__contraseña = nueva
            print('Su contraseña fue actualizada correctamente')
            
        else:
            print('contraseña incorrecta')


    def crearCuenta(correoElec): 
        
        if type(correoElec) == str:
            if (re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoElec.lower())):
                print('\ncorreo: \n',correoElec)
                parte1 = re.split(r'[@]', correoElec)
                print('parte1: ',parte1)
                parte2 = re.split(r'[.]', parte1[1])
                print('parte2: ',parte2)
                idC = parte1[0]
                print('idC: ',idC)
                domi = parte2[0]
                tiD = parte2[1]
                contra = '123'
                e = Email(idC,domi,tiD,contra)
                e.mostrarCorreo()
        else:
            print('parametros con tipo incorrectos')
    
    def mostrarCorreo(self):
        print('\n idCuenta: {}'.format(self.__idCuenta))
        print('\n dominio: {}'.format(self.__dominio) )
        print('\n tipo de dominio: {}'.format(self.__tipoDom))
        print('\n contraseña: {}'.format(self.__contraseña))

    