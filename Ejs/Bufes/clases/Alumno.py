from .Persona import Persona

class Alumno (Persona):
    divicion = None

    def set_divicion(self,d):
        self.divicion=(d)
