import pymysql
import time
from ClasesPiezas import *
from ClasesTablero import *
from bdd import *
from Clase_Partida import *

class Partida(object):

    _id=None
    Nombre=None
    jugador_Blanco=None
    _id_jugador_Blanco=None
    jugador_Negro=None
    _id_jugador_Negro = None

    def __init__(self):

        self.lista_mov=[]

    def crear_partida(self):


        BD().run("Insert INTO Partida values (Null ,'" + self.Nombre + "," + self._id_jugador_Blanco + "," + self._id_jugador_Negro + "')")

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

    def calcular_elo(self):