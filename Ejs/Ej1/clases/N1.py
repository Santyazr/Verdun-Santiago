
class Alumno (object):
    nombre= ""
    apellido=""
    fechaNac= None
    notas=[]

    def setNombre(self,nombre):
        self.nombre=str(nombre)

    def setApellido(self,apellido):
        self.apellido=str(apellido)

    def setFecha(self,fecha):
        self.fechaNac=fecha

    def agregarNota(self,notas):
        self.notas.append(notas)

    def minNota(self,):
        return min(self.notas)

    def maxNota(self):
        return max(self.notas)

    def Prom(self):
        return sum(self.notas)/len(self.notas)