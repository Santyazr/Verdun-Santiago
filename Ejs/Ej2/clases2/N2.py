class Materias (object):
    nombre=""
    notas=[]


    def setNombre(self,nombre):
        self.nombre=str(nombre)

    def agregarNota(self,notas):
        self.notas.append(notas)

    def Prom(self):
        return sum(self.notas)/len(self.notas)

    def maxProm(self):
        #algo

    def minProm(self):
        #algo

    def promGen(self):
         #algo

     class Alumno (object):
    materias=[]
    def __init__(self):
        self.materias[]