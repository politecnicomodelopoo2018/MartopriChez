import pygame, sys
from pygame.locals import *
from ClasesPiezas import *
a = pygame.image.load("/home/melman/Escritorio/rsz_melma_puntito.png")
ventana = pygame.display.set_mode((700,700))

class Tablero(object):

    instance = None

    def __init__(self):
        self.imagen = "/home/melman/Escritorio/Tablero.jpg"


    def __new__(cls, *args, **kwargs):
        if Tablero.instance is None:
            Tablero.instance = object.__new__(cls)
            Tablero.instance.lista_Piezas = []
            Tablero.instance.lista_Bloques = []
        return Tablero.instance

    #resive los todos los posibles movimientos y los imprime con la pelota verde
    def posibles_mov(self,pieza):#imrpime los posibles mov de laqs piezas en la clase tablero
        lista_a_imprimir = pieza.posibles_movimientos()
        print(lista_a_imprimir)
        for item in lista_a_imprimir:

            ventana.blit(a,(item[0], item[1]))

    #despues de un mov llamar a esta funcion para imprimir una pieza
    def imprimir(self):

        ventana.blit(self.imagen(0,0))
        for item in self.lista_Piezas:
            if item.viva:
                ventana.blit(item.imagen(item.posx,item.posy))




class Bloque(object):

    Nombre = None
    traducciony = None
    traduccionx = None
    poscx = None
    poscy = None
    Vacio = None