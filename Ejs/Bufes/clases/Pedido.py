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
    entregado = None
    precio_pedido=None


    def __init__(self):
        self.lista_pedidos=[]

    def set_pedido(self,per,pla,e):
        self.persona=(per)
        self.plato=(pla)
        self.fech_deEntrega=(e)

    def set_estado(self,bool):
        self.entregado=bool

    def terminado(self,f):
        self.fech_creacion=(f)

    def eliminar_pedido(self,p):
        for item in Pedido
            if p == Pedido()
            Pedido()==None

    def calc_Pedido(self,precioTotal_c):
        if desc is not None:
            self.precioTotal_c=(Profesor.desc(int) - Plato.Precio)
            self.precio_pedido=(precioTotal_c)
        else
            self.precio_pedido=(precioTotal_c)


    def modificacion(self, Nfech_deEntrega=None, Nplato=None, Nfecha_deEntrega=None, Nfech_creacion=None):
        for item in Pedido:
           if fech_deEntrega is not None:
               self.date_of_creation = Nfech_deEntrega
           if plato is not None:
               self.plato = Nplato
           if fech_deEntrega is not None:
               self.fech_deEntrega = Nfecha_deEntrega
           if fech_creacion is not None:
               self.fech_creacion = Nfech_creacion




