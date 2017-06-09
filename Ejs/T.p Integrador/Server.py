import pymysql
class Empleado (object):
    dni=None
    nombre=None
    apellido=None
    telefono=None
    direccion=None

Db=pymysql.connect (host="localhost",
                    user="alumno",
                    password="alumno",
                    Db='Empleaditos',autocommit=True)

dni=input()
nombre=input()
apellido=input()
telefono=input()
direccion=input()
c=Db.cursor()
c.execute("insert into Empleados values('"+dni+"','"+nombre+"','"+apellido+"', '"+telefono+"', '"+direccion+"')" )
Db.close()
