import csv
from ClaseEmail import Email

class ListaEmail:
    __listaEmails = []

    def __init__(self):
        self.__listaEmails = []

    def Agregar(self, v1):
        self.__listaEmails.append(v1)

    def Mostrar(self):
        UnEmail = Email()
        for UnEmail in self.__listaEmails:
            print(UnEmail)