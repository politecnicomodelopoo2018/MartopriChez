import pymysql
import time
from ClasesTablero import *
from bdd import *
from Clase_Partida import *
from pruba import *

class GM(object):


    instance = None

    def __new__(cls, *args, **kwargs):
        if GM.instance is None:
            GM.instance = object.__new__(cls)
            GM.instance.lista_Jugadores = []
            GM.instance.lista_Partidas = []

        return GM.instance

    def descargar_partidas(self,id_partida):

        obj_partida = BD().run("select * from Partidas where idPartida = " + str(id_partida)+";")
        dic_mov = BD().run("select * from Posiciones where Partidas_idPartida = " + str(id_partida)+";")
        dic_mov = dic_mov.fetchall()
        movs = []
        for item in dic_mov:
            a = movimientos()
            a.crear_mov_interno(item["Partidas_idPartida"],item["Pieza"],item["Posicion"],item["Color"])

            movs.append(a)
        a=Partida()
        algo = obj_partida.fetchall()

        nm = algo[0]["Nombre"]
        jB = algo[0]["Jugador_idJugador"]
        jn = algo[0]["Jugador_idJugador1"]
        a.lista_mov=movs
        jbn,jnn = self.descarga_datos(jB,jn)
        a.crear_partida(nm,jbn.Nombre,jbn._id,jnn.Nombre,jnn._id )
        return a

    def recrear_partida(self,partida):

        crearpiezas()

        ventana = pygame.display.set_mode((700, 700))

        Board = pygame.image.load("/home/melman/Escritorio/Tablero.jpg")
        posX, posY = 0, 0
        pygame.display.set_caption("Martorille chess")
        ventana.blit(Board, (posX, posY))

        Tablero().crear_Bloques()

        for item in Tablero().lista_Piezas:
            for item2 in Tablero().lista_Bloques:
                if item2.poscx == item.posx and item2.poscy == item.posy:
                    ventana.blit(item.imagen, (item2.traduccionx + 20, item2.traducciony + 5))
                    item2.esta_Vacio()
        pygame.display.update()

        for item in partida.lista_mov:
            for item2 in Tablero().lista_Piezas:
                if item.id_pieza ==  item2._id:
                    for item3 in Tablero().lista_Bloques:
                        if item3.Nombre == item.id_bloque:
                            item2.mover(item3.poscx,item3.poscy)
                            item2.comer()
                            Tablero().imprimir()
                            time.sleep(3)
                            pygame.display.update()

    def descarga_datos(self,Blanco,Negro):

        jugadorb=BD().run("select * from Jugador where idJugador = "+ str(Blanco) +";")
        jugadorn = BD().run("select * from Jugador where idJugador = " + str(Negro) + ";")
        jugadorb=jugadorb.fetchall()
        jugadorn=jugadorn.fetchall()
        a = jugador()
        a.crear_jugador(jugadorb[0]["Nombre"],jugadorb[0]["elo"])
        b = jugador()
        b.crear_jugador(jugadorn[0]["Nombre"], jugadorn[0]["elo"])
        return a,b



