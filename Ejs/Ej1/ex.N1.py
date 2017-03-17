from clases.N1 import Alumno
from datetime import date

a=Alumno()
a.setNombre="Jorge"

a.setApellido="Sacarias"

a.setFecha=(date(2017,3,17))

a.agregarNota(7)

a.agregarNota(8)

print(a.Prom())
print(a.maxNota())
print(a.minNota())