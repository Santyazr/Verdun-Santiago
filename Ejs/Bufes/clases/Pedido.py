from .Persona import Persona
from .Plato import Plato
from .Profesor import Profesor
from .Alumno import Alumno
from date import datetime


class Pedido(Alumno,Profesor):
    lista_pedidos = []
    fech_creacion = None
    persona = None
    plato = None
    fech_deEntrega = None
    entregado = False
    precio_pedido=None


    def __init__(self):
        self.lista_pedidos=[]

    def set_pedido(self,per,pla,e):
        self.persona=(per)
        self.plato=(pla)
        self.fech_deEntrega=(e)

    def terminado(self, f):
        self.fech_creacion = (f)

    def set_estado(self):
        self.entregado= True



    def eliminar_pedido(self,p):
        for item in Pedido
            if p == Pedido()
            item.Pedido()==None

    def calc_Pedido(self,precioTotal_c):
        if desc is not None:
            self.precioTotal_c=(Profesor.desc(int) - Plato.Precio)
            self.precio_pedido=(precioTotal_c)
        else
            self.precio_pedido=(precioTotal_c)


    def modificacion(self, Nfech_deEntrega=None, Nplato=None, Nfecha_deEntrega=None, Nfech_creacion=None):
        for item in Pedido:
           if fech_deEntrega is not None:
               item.fech_deEntrega = Nfech_deEntrega
           if plato is not None:
               item.plato = Nplato
           if fech_creacion is not None:
               item.fech_creacion = Nfech_creacion




