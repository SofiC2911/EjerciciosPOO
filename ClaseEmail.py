# -*- coding: utf-8 -*-
import re

class email:

    __idCuenta = ''
    __dominio = ''
    __tipoDom = ''
    __contraseña = ''

    def __init__(self, idCuenta, dominio, tipoDom, contraseña):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDom = tipoDom
        self.__contraseña = contraseña
    
    def retornaEmail(self):
        return '' + self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDom
    
    def getDominio(self):
        return self.__dominio
    
    def cambiarContra(self):
        cont = input('contraseña actual: ')
        print ('contraseña actual: ', self.__contraseña)
        if (cont == self.__contraseña):
            nueva = input('Nueva contraseña: ')
            self.__contraseña = nueva
            print ('contraseña nueva: ', self.__contraseña)
        else:
            print('contraseña incorrecta')

    def crearCuenta(correoElec):
        if (re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correoElec.lower())):
            print('correo: ',correoElec)
            parte1 = re.split(r'[@]', correoElec)
            parte2 = re.split(r'[.]', parte1[1])
            idC = parte1[0]
            domi = parte2[0]
            tiD = parte2[1]
            contra = input('contraseña: ')
            e = email(idC,domi,tiD,contra)
            e.mostrarC()
    
    def mostrarC(self):
        print('idCuenta: {}'.format(self.__idCuenta))
        print('dominio: {}'.format(self.__dominio) )
        print('tipo de dominio: {}'.format(self.__tipoDom))
        print('contraseña: {}'.format(self.__contraseña))