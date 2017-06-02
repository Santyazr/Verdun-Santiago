class Pasajero (Persona):
    nece_espe=None
    vip=None
    millas=None


    def set_pasajero (self, mmillas, vvip, nece):
        self.millas=mmillas
	    self.vip=bool(vvip)
	    self.nece_espe=nece

    def list_especiales ():
	list_especiales=[]
	for item in Pasajero:
		if item.nece_espe or item.vip is not null:
			print (nece_especial)
			list_especiales.append(pasajero)

    def Pasaj_Espec ():
        list_vip=[]
        list=[]
        for item in list_vuelos:
            for item2 in list_pasaj:
                if item2 not in item.list_pasaj:
                    if item2.vip != None:
                        if item2.necesidades_especiales != None:
                            listavip.append (item2.nece_espe)
                        list_vip.append(item2.dni)
                    else :
                        if item2.nece_espe != None:
                            lista.append (item2.neces_espe)
                            lista.append (item2.dni)


