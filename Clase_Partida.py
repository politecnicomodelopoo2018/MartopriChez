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

        BD().run("Insert INTO Posiciones values (Null ," + str(self._id) + "," + str(pieza._id) +",'"+ nombre +"','"+pieza.color +"')")

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


    def crear_jugador(self,id,Nombre,elo):

        self._id = id
        self.Nombre=Nombre
        self.elo= elo