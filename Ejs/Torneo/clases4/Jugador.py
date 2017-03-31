class Jugador (object):
    nombre=""
    fecha_nac=None
    num_cami=None

    def set_nombre(self,n):
        self.nombre=str(n)

    def set_fechaNac(self, f):
        self.fecha_nac=(f)

    def set_numCam(self,N):
        self.num_cami=(N)