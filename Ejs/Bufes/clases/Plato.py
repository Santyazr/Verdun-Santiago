
class Plato(object):
    nombre = None
    Precio = None

    def set_Plato(self,n,p):
        self.nombre=(n)
        self.precio=(p)

        f= open ("Platos.txt","w+")
        for item in f:
            f.write (item.nombre+"-----------*"+item.precio)
            f.close()

    def eliminar_pla(self,p):
        for item in Plato:
            if p == Plato():
               Plato()==None