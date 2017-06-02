class Aviones(object):
    mod = None
    cant_pasaj = None
    cant_trip = None

    def set_avion (self, mode, pasaj, trip):
        self.mod = mode
        self.cant_pasaj = pasaj
        self.cant_trip = trip


    def buscar_avion (self, mode):
        for item in Aviones:
            if item.mod== mode:
                return Aviones


