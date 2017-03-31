from datetime import date
from clases4.Jugador import Jugador
from clases4.Equipo import Equipo
from clases4.Partido import Partido
from clases4.Torneo import Torneo

jug=Jugador()
jug2=Jugador()
jug3=Jugador()
jug4=Jugador()
jug5=Jugador()
jug6=Jugador()
jug7=Jugador()
jug8=Jugador()
jug9=Jugador()
jug10=Jugador()

equi=Equipo()
equi2=Equipo()

part=Partido()

tor=Torneo()

jug.set_nombre("Pedro")
jug.set_fechaNac (1989,12,3)
jug.set_numCam(2)

jug2.set_nombre("Carlos")
jug2.set_fechaNac (1988,10,30)
jug2.set_numCam(5)

jug3.set_nombre("Teodoro")
jug3.set_fechaNac (1989,7,14)
jug3.set_numCam(7)

jug4.set_nombre("Penelope")
jug4.set_fechaNac (1987,16,12)
jug4.set_numCam(14)

jug5.set_nombre("Ramona")
jug5.set_fechaNac (1989,29,9)
jug5.set_numCam(9)

jug6.set_nombre("Jorge")
jug6.set_fechaNac (1989,2,7)
jug6.set_numCam(20)

jug7.set_nombre("Marcos")
jug7.set_fechaNac (1989,23,4)
jug7.set_numCam(4)

jug8.set_nombre("Fernando")
jug8.set_fechaNac (1990,6,1)
jug8.set_numCam(19)

jug9.set_nombre("Nigaro")
jug9.set_fechaNac (1990,21,2)
jug9.set_numCam(10)

jug10.set_nombre("Mercedes")
jug10.set_fechaNac (1988,4,5)
jug.set_numCam(11)


equi=("Montoneros")
equi.set_agreJug(jug)
equi.set_agreJug(jug2)
equi.set_agreJug(jug3)
equi.set_agreJug(jug4)
equi.set_agreJug(jug5)
equi.capi(jug4)

equi2=("Inversores")
equi.set_agreJug(jug6)
equi.set_agreJug(jug7)
equi.set_agreJug(jug8)
equi.set_agreJug(jug9)
equi.set_agreJug(jug10)
equi.capi(jug9)







