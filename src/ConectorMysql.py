import peewee
from peewee import *
import datetime


db = MySQLDatabase('Monitoreo', user='root', password='123456')


class servidores(peewee.Model):
        Ipservidor = peewee.CharField(primary_key=True, max_length=50)
        Procesador = peewee.CharField()
        ProcesosCorriendo = peewee.CharField()
        UsuariosConectados = peewee.CharField()
        SO = peewee.CharField()
        Version_SO = peewee.CharField()
        class Meta:
                database=db
                db_table='infoserver'

if not servidores.table_exists():
                servidores.create_table()


def abmbd (ip,proc,pscor,ucon,so,vso):
        try:
                server = servidores.get(servidores.Ipservidor == ip)
                server = servidores.update(Procesador=proc,ProcesosCorriendo=pscor,UsuariosConectados=ucon,SO=so,Version_SO=vso).execute()
        except servidores.DoesNotExist:
                server = servidores.create(Ipservidor=ip,Procesador=proc,ProcesosCorriendo=pscor,UsuariosConectados=ucon,SO=so,Version_SO=vso)

