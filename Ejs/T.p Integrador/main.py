
from clase1.Ordenador import Listado

listado=Listado()
def menu():
    print("1) Agregar empleado.")
    print("2) Eliminar empleado.")
    print("3) Buscar empleado.")
    print("4) Modificar empleado .")
    print("5) Salir")

while True:

    menu()

    tecla=input()
    if tecla =='1':
        print("Ingrese el nombre del empleado que quiera agregar.")
        n = input()
        print("Ingrese apellido.")
        a = input()
        print("Ingrese dni.")
        d = input()
        listado.set_Emp(n ,a ,d)


    if tecla=='2':
        print("Ingrese el DNI del empleado que quiera eliminar.")
        el_dni= input()
        listado.rem_Emp(el_dni)


    if tecla =='3':
        print("Ingresa dni del buscado.")
        d = input()
        listado.search_Emp(d)

    if tecla == '4':
        print("Ingrese dni del empleado que quieras cambiar.")
        dni0 = input()
        print("Ingrese el nuevo nombre.")
        n = input()
        print("Ingrese nuevo apellido.")
        a = input()
        print("Nuevo dni.")
        d = input()
        listado.change_Emp(dni0, n, a, d)

    if tecla=='5':
        break