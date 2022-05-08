from email import Email
from manejador import Manejador

if __name__ == '__main__':

    nombre = input('Ingrese nombre del usuario: ')
    idCuenta = input('idCuenta: ')
    dominio = input('dominio: ')
    tipo = input('tipo de dominio: ')
    contra = input('contraseña: ')
    correo = Email(idCuenta,dominio,tipo,contra)


    print('Estimado {} te enviaremos tus mensajes a la dirección {}'.format(nombre,correo.retornaEmail()))
    
    print('\n ----- Cambio de contraseña------ ')
    correo.cambiarContra()

    Email.crearCuenta('informatica.fcefn@gmail.com')

    correo.buscarRepetido()
