import pymysql
import time
from ClasesPiezas import *
from ClasesTablero import *
from bdd import *
import datetime

class Partida(object):

    _id=None
    Nombre=None
    jugador_Blanco=None
    _id_jugador_Blanco=None
    jugador_Negro=None
    _id_jugador_Negro = None

    def __init__(self):

        self.lista_mov=[]

    def crear_partida(self,Nombre,jb,_idjb,jn,_idjn):

        self.Nombre = Nombre
        self.jugador_Blanco = jb
        self._id_jugador_Blanco = _idjb
        self.jugador_Negro = jn
        self._id_jugador_Negro = _idjn


    def guardar_mov(self,pieza):

        for item in Tablero().lista_Bloques:
            if item.poscx == pieza.posx and item.poscy == pieza.posy:
                nombre=item.Nombre

        a = movimientos()
        a.crear_mov(self._id,pieza._id,nombre,pieza.color)

    def crearEnBdd(self):
        BD().run("Insert INTO Partidas values (null ,'" + str(self.Nombre) + "'," + str(self._id_jugador_Blanco) + "," + str(self._id_jugador_Negro) + ")")
        h = BD().run("select idPartida from Partidas where Nombre = '"+ self.Nombre +"' and Jugador_idJugador = "+ str(self._id_jugador_Blanco) +" and Jugador_idJugador1 = "+ str(self._id_jugador_Negro))
        dasdasd=h.fetchall()
        self._id=dasdasd[0]["idPartida"]

class jugador(object):

    _id=None
    Nombre=None
    elo=1000

    def __init__(self):

        self.Partidas_Jugadas= []


    def crear_jugador(self,Nombre,elo):

        self.Nombre=Nombre
        if elo != 0:
            self.elo= elo
        else:
            self.elo = 1000
        self.crear_jugadorbdd()
        id=BD().run("select idJugador from Jugador where Nombre = '"+ str(self.Nombre) +"' and elo ="+ str(self.elo) +";")
        asd=id.fetchall()
        self._id=asd[0]["idJugador"]

    def crear_jugadorbdd(self):

        BD().run("INSERT INTO Jugador Values (null,'"+str(self.Nombre) +"',"+ str(self.elo) +")")

class movimientos(object):

    id_partida = None
    id_pieza = None
    id_bloque = None
    color_pieza = None

    def crear_mov_interno(self,idp,idpi,idblo,cop):
        self.id_partida = int(idp)
        self.id_pieza = int(idpi)
        self.id_bloque = idblo
        self.color_pieza = cop

    def crear_mov(self,idp,idpi,idblo,cop):
        self.id_partida = idp
        self.id_pieza = idpi
        self.id_bloque = idblo
        self.color_pieza = cop
        self.guardar_mov()

    def guardar_mov(self):

        BD().run("Insert INTO Posiciones values (Null ," + str(self.id_partida) + "," + str(self.id_pieza) +",'"+ self.id_bloque +"','"+self.color_pieza +"')")