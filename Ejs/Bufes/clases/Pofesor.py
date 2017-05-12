from .Persona import Persona

class Profesor(Persona):
    desc = None
#me da error con el tema del import
    f = open("Profesores.txt", "w+")
    for item in f:
        f.write(item.Persona.nombre + "-" + item.Persona.apellido +
        "-" + item.Persona.dni+ "-" +item.desc)
        f.close()

    def set_desc(self,d):
        self.desc=(d)

    def modificacionProf(self,Nnombre = None ,Napellido = None, Ndni = None, Ndescuento = None ):
        for item in Pedido:
           if fech_deEntrega is not None:
               item.nombre = Nnombre
           if apellido is not None:
               item.apellido = Napellido
           if fech_deEntrega is not None:
               item.dni = Ndni
           if fech_creacion is not None:
               item.descuento = Ndescuento