from Tripulacion import Tripulantes
from Personas import Persona
from .Avion import Aviones
class Vuelo (object):
    avion_mod=None
    list_pasaj=[]
    list_trip=[]
    fech_salida=None
    hora_salida=None
    origen=None
    destino=None
    cod_vuelo=None

    def __init__(self):
        self.lista_pasaj=[]
        self.lista_trip=[]

    def set_vuelo(self, cod, mod, f, h, o, d, T, P):
        self.codigo_vuelo=cod
        self.avion_mod=mod
        self.fecha_salida=f
        self.hora_salida=h
        self.origen=o
        self.destino=d
        self.list_pasaj.append(P)
        self.list_trip.append(T)

    def buscar_vuelo (self, codev):
        for item in Vuelo:
            if item.cod_vuelo==codev:
                return item


    def Nomina (self):
        lista=[]
        for pasajero in self.list_pasaj:
            lista.append(pasajero)
        for item in lista:
            print (item.nombre)
        return lista

    def VuelosSinTripulacion(self):
        return len(self.list_trip)



    def vueloXdia (self):
        list_vueloosXdia=[]
        for item in Vuelo:
            for item2 in Vuelo:
                if item != item2 and item.fech_salida:==item2.fech_salida
                mal mal mal mal mal

