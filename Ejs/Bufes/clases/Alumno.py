from .Persona import Persona

class Alumno (Persona):
    divicion = None

    f = open("Alumnos.txt", w +)
    for item in f:
        f.write(item.nombre) + "-" + item.apellido + "-" + item.dni+"-"+item.divicion)
        f.close()

    def set_divicion(self,d):
        self.divicion=(d)


    def modificacionAlum(self,Nnombre = None ,Napellido = None, Ndni = None, Ndivicion = None ):
        for item in Pedido:
           if fech_deEntrega is not None:
               item.nombre = Nnombre
           if apellido is not None:
               item.apellido = Napellido
           if fech_deEntrega is not None:
               item.dni = Ndni
           if fech_creacion is not None:
               item.divicion = Ndivicion

