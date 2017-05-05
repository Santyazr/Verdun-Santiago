class Empleado (object):
    nombre = ""
    fech_nac = ""
    disp = []



    def set_nombre(self,n):
        self.nombre = str(n)

    def set_fecha(self,f):
        self.fecha_nac = (f)

    def agre_disp(self, d):
        self.disp.append(d)
