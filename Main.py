import csv
from ClaseEmail import Email
from ClaseListaEmail import ListaEmail

if __name__=='__main__':
    print("Ingrese los siguientes datos")

    nombre = input("Nombre: ")
    idCuenta = input ("Id de la cuenta: ")
    dominio = input ("Dominio de la cuenta: ")
    tipoDominio = input ("Tipo de dominio de la cuenta: ")
    contrasena = input ("Contrasena: ")

    UnEmail = Email(idCuenta, dominio, tipoDominio, contrasena)

    print(f"Estimado {nombre} te enviaremos tus mensajes a la direccion {UnEmail.__str__()}")

    UnEmail.CambioContrasena()

    print("A continuacion se creara una instancia de la clase Email")
    x = input("Ingrese nuevo Email: ")
    OtroEmail = Email()
    OtroEmail.crearCuenta(x)

    print("A continuacion se lee un achivo")
    dominio = input("Ingrese un dominio: ")
    cont = 0
    ManejadorEmails = ListaEmail()
    archivo = open("archivo.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for fila in reader:
        ElEmail = Email(fila[0], fila[1], fila[2], fila[3])
        ManejadorEmails.Agregar(ElEmail)
        if fila[1] == dominio:
            cont = cont + 1
    print(f"La cantidad de direcciones Email con dominio {dominio} es de: {cont}")
    ManejadorEmails.Mostrar()
    archivo.close()