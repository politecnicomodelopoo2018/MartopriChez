import pygame, sys
from pygame.locals import *
from ClasesPiezas import *
import time

a = pygame.image.load("/home/melman/Escritorio/rsz_melma_puntito.png")
ventana = pygame.display.set_mode((700,700))

class Tablero(object):

    instance = None

    def __init__(self):
        self.imagen = pygame.image.load("/home/melman/Escritorio/Tablero.jpg")


    def __new__(cls, *args, **kwargs):
        if Tablero.instance is None:
            Tablero.instance = object.__new__(cls)
            Tablero.instance.lista_Piezas = []
            Tablero.instance.lista_Bloques = []
        return Tablero.instance

    #resive los todos los posibles movimientos y los imprime con la pelota verde
    def posibles_mov(self,pieza):#imrpime los posibles mov de laqs piezas en la clase tablero
        lista_a_imprimir = pieza.posibles_movimientos()
        list_aux = []
        for mov in lista_a_imprimir:
            for item in self.lista_Bloques:
                if item.poscy == mov[1] and item.poscx == mov[0]:
                    list_aux.append(item)
        for item in list_aux:

            ventana.blit(a,(item.traduccionx, item.traducciony))
        return lista_a_imprimir

    #despues de un mov llamar a esta funcion para imprimir una pieza
    def imprimir(self):

        ventana.blit(self.imagen, (0,0))
        for item in self.lista_Piezas:
            for item_bloques in self.lista_Bloques:
                if item.viva and item.posx == item_bloques.poscx and item.posy == item_bloques.poscy:
                    ventana.blit(item.imagen,(item_bloques.traduccionx + 20,item_bloques.traducciony + 5))
                    pygame.display.update()


    def crear_Bloques(self):

        traducy = 595
        # 82 y
        # 81 x
        y = 1
        xprima=0
        for item in range(8):
            x = 0
            xprima +=1
            print("entre2")
            traducx = 24
            for item in range(8):
                x += 1

                print("entre")


                a = Bloque()
                pepe = chr(64 + x)
                pepe = str(pepe)
                pepen = str(xprima)
                una_var = (pepe + pepen)
                a.Nombre = una_var
                a.poscx = x
                a.poscy = y
                a.vacio = True
                a.traduccionx = traducx
                a.traducciony = traducy
                Tablero().lista_Bloques.append(a)
                traducx += 81
                print(a)

            y += 1
            traducy -= 82

    def no_me_rompas_las_bolas_maxi(self, list_aux,pieza,evento,mouse):#mover las piezas

        ym,xm=0,0
        while True:
            for event in pygame.event.get(KEYUP):
                for item in list_aux:

                    if event.key == K_SPACE:
                        xm=mouse[0]
                        ym=mouse[1]
                        print(xm,ym)
                        for item_bloques in Tablero().lista_Bloques:
                            cy = item_bloques.poscy
                            cx = item_bloques.poscx
                            print(cx,cy)
                            if item_bloques.traduccionx + 82 > xm and xm > item_bloques.traduccionx and \
                                     item_bloques.traducciony + 82 > ym and ym > item_bloques.traducciony:
                                pieza.mover(cx,cy)
                                return


class Bloque(object):

    Nombre = None
    traducciony = None
    traduccionx = None
    poscx = None
    poscy = None
    Vacio = None

    def esta_Vacio(self):

        for item in Tablero().lista_Piezas:
            if item.posx == self.poscx and item.posy == self.poscy:
                self.Vacio = False
                return
        self.Vacio = True
