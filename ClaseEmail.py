import re

class Email:
    __idCuenta = 0
    __dominio = 0
    __tipo_dominio = 0
    __contrasena = 0

    def __init__(self, v1 = "ejemplo", v2 = "gmail", v3 = "com", v4 = 0):
        self.__idCuenta = v1
        self.__dominio = v2
        self.__tipo_dominio = v3
        self.__contrasena = v4

    def __str__(self):
        return(self.__idCuenta+"@"+self.__dominio+"."+self.__tipo_dominio)

    def retornaEmail(self):
        return(self.__idCuenta+"@"+self.__dominio+"."+self.__tipo_dominio)

    def getDominio(self):
        return(self.__dominio)

    def CambioContrasena(self):
        contrasenaNueva = 0

        while (self.__contrasena != contrasenaNueva):
            print("A continuacion se necesita cambiar la contrasena ingresada")
            print("Ingrese la contrasena de forma correcta")
            contrasenaNueva = input("Contrasena: ")
            if (self.__contrasena == contrasenaNueva):
                print("contrasenas coicidente")
            else:
                print("contrasenas no coincidentes")

        self.__contrasena = input("nueva contrasena: ")

    def crearCuenta(self, x):
        x = x.split("@")
        self.__idCuenta = x[0]
        x[0] = x[1]
        x.pop()
        x = "".join(x)
        x = x.split(".", 1)
        self.__dominio = x[0]
        self.__tipo_dominio = x[1]