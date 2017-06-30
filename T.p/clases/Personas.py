from .Avion import Aviones
from datetime import date
class Persona(object):
    nombre = None
    apellido = None
    fecha_nac = None
    dni = None


    def setPersona(self, nombree, apellidoo, f , dnii):

        self.nombre = nombree
        self.apellido = apellidoo
        self.fecha_nac = f
        self.dni = dnii


    def buscar_persona(self, d):
        for item in Aviones:
            if item.dni==d:
                return item


    def set_edad(self):
        dia_hoy = date.today()
        fecha = self.fecha_nac
        año = fecha[6] + fecha[7] + fecha[8] + fecha[9]
        self.Edad = dia_hoy.year - int(año)

        return self.Edad









