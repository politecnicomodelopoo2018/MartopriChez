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

    def crear_partida(self,_id,Nombre,jb,_idjb,jn,_idjn):

        self._id = _id
        self.Nombre = Nombre
        self.jugador_Blanco = jb
        self._id_jugador_Blanco = _idjb
        self.jugador_Negro = jn
        self._id_jugador_Negro = _idjn


    def guardar_mov(self,pieza,partida):

        for item in Tablero().lista_Bloques:
            if item.poscx == pieza.posx and item.poscy == pieza.posy:
                nombre=item.Nombre

        BD().run("Insert INTO Posiciones values (Null ,'" + partida._id + "," + pieza._id +","+ nombre +","+pieza.color +"')")


class jugador(object):

    _id=None
    Nombre=None
    elo=None

    def __init__(self):

        self.Partidas_Jugadas= []


    def crear_jugador(self,id,Nombre,elo):

        self._id = id
        self.Nombre=Nombre
        self.elo=elo