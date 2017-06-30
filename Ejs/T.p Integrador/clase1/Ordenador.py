from clase1.Lista import Empleado

class Listado(object):
    Lista_Emp=[]

    def __init__(self):
        self.Lista_Emp=[]

    def set_Emp(self,n ,a ,d):
        E = Empleado()
        E.nombre = str(n)
        E.apellido = str(a)
        E.dni = d
        self.Lista_Emp.append(E)
        print (self.Lista_Emp)


    def rem_Emp(self, d):
        el_dni = d
        for item in self.Lista_Emp:
            if item.dni == el_dni:
                self.Lista_Emp.remove(item)

    def search_Emp(self,d):
        el_dni = d
        for item in self.Lista_Emp:
            if item.dni == el_dni:
                print("---",item.nombre,"---")



    def change_Emp(self,dni0, n, a, d):
        el_dni = dni0
        for item in self.Lista_Emp:
            if item.dni == el_dni:
                item.nombre = str(n)
                item.apellido = str(a)
                item.dni = d


