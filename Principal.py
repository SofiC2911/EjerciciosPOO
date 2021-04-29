# -*- coding: utf-8 -*-
import csv

from ClaseEmail import email

if __name__ == '__main__':
    idCuenta = input('idCuenta: ')
    dominio = input('dominio: ')
    tipoDom = input('tipo de dominio: ')
    contraseña = input('contraseña: ')
    correo = email(idCuenta,dominio,tipoDom,contraseña)
    

    nombre = input('Ingrese nombre del usuario: ')
    
    print('Estimado {} te enviaremos tus mensajes a la direccion {}'.format(nombre,correo.retornaEmail()))
    
    print('Cambio de contraseña')
    correo.cambiarContra()
    
    email.crearCuenta('informatica.fcefn@gmail.com')
    email.crearCuenta('wicc2019@unsj-cuim.edu')
    email.crearCuenta('juanLiendro1957@yahoo.com')
    
    archi = open('RegCorreo.csv')
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