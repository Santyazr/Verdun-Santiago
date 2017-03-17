from clases.N1 import Alumno
from datetime import date

al=Alumno()
al.setNombre="Jorge"

al.setApellido="Sacarias"

al.setFecha=(date(2017,3,17))

al.agregarNota(7)

al.agregarNota(8)

print(al.Prom())
print(al.maxNota())
print(al.minNota())