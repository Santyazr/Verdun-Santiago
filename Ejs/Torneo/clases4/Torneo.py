class Torneo (object):

    Lis_equipos=[]
    Lis_partidos=[]

    def set_partidos(self,e):
        if e in self.Lis_equipos:
            return false
        self.Lis_equipos.append(e)
        return true
    def lis_p(self,p):
        if p in self.Lis_partidos:
            return false
            self.Lis_equipos.append(p)
            return true


