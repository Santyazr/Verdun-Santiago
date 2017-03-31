class Equipo (object):
    nombre=""
    disp=[]
    cap=""
    list_jugadores=[]
    barrio=""


    def set_agreJug(self,j):
        self.list_jugadores.append(j)

    def mod_disp(self,d,t,a):
        self,disp[d][t]=bool(a)

    def capi(self,j):
        self.cap=str(j)