import pymysql
import time
from ClasesTablero import *
from bdd import *
from Clase_Partida import *

class GM(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        if GM.instance is None:
            GM.instance = object.__new__(cls)
            GM.instance.lista_Jugadores = []
            GM.instance.lista_Partidas = []

        return Tablero.instance

    def descargar_partidas(self,id_partida):

        obj_partida = BD().run("select * from Partida where idPartida = " + str(id_partida))
        dic_mov = BD().run("select * from Posiciones where idPartida = " + str(id_partida))
        a=Partida()
        a.jugador_Blanco = obj_partida["Jugador_idJugador"]
        a.jugador_Negro = obj_partida["Jugador_idJugador1"]
        a._id = obj_partida["idPartida"]
        a.lista_mov=dic_mov
        return a

    def recrear_partida(self,partida):
        Tablero().crear_pieza
        for item in partida.lista_mov:
            for item2 in Tablero().listapieza:
                if item["Pieza"] ==  item2._id:
                    for item3 in Tablero().lista_bloques:
                        if item3.Nombre == item["Posicion"]:
                            item2.mover(item3.poscx,item3.poscy)
                            item2.comer()
                            Tablero().imprimir()
                            time.sleep(3)

    def descarga_datos(self):

        jugador=BD().run("select * from Jugador")
        for item in jugador:
            a = jugador()
            a.crear_jugador(item["idJugador"],item["Nombre"],item["elo"])

        partidas=BD().run("select * from Partida")
        for item in partidas:
            xD = BD().run("select Nombre from Jugador where idJugador =" + item["Jugador_idJugador"])
            xD1 = BD().run("select Nombre from Jugador where idJugador =" + item["Jugador_idJugador"])
            b = Partida()
            b.crear_partida(item["idPartida"],item["Nombre"],xD,item["Jugador_idJugador"],xD1,item["Jugador_idJugador"])