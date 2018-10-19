import pygame, sys
from pygame.locals import *
from ClasesPiezas import *
import time

a = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/Bola_naranja.png")
ventana = pygame.display.set_mode((700,700))

class Tablero(object):

    instance = None

    def __init__(self):
        self.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/Tablerooooooo.png")


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

    def crearpiezas(self):
        x = 0
        y = 2
        cont = 10
        for item in range(8):
            a = peon()
            a._id = cont
            x += 1
            a.color = "Blanco"
            a.posx = x
            a.posy = y
            a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/peon_Blanco.png")
            a.viva = True
            a.var_inicial = True
            self.lista_Piezas.append(a)
            cont += 1
        x = 0
        y = 7
        cont = 2
        for item in range(8):
            a = peon()
            a_id = cont
            x += 1
            a.color = "Negro"
            a.posx = x
            a.posy = y
            a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/peon_Negro.png")
            a.viva = True
            a.var_inicial = True
            Tablero().lista_Piezas.append(a)
            cont += 1

        y = 1
        x = 4

        a = rey()
        a.color = "Blanco"
        a._id = 1
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/rey_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)
        y = 8
        x = 5

        a = rey()
        a._id = 0
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/rey_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 5

        a = reina()
        a.color = "Blanco"
        a._id = 20
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/reina_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)
        y = 8
        x = 4

        a = reina()
        a.color = "Negro"
        a._id = 21
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/reina_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 2

        a = caballo()
        a._id = 40
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/caballo_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 7

        a = caballo()
        a._id = 41
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/caballo_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 8
        x = 2
        a = caballo()
        a._id = 42
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/caballo_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 8
        x = 7
        a = caballo()
        a._id = 42
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/caballo_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 8
        x = 3

        a = alfil()
        a._id = 50
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/alfil_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 8
        x = 6

        a = alfil()
        a._id = 54
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/alfil_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 6
        a = alfil()
        a._id = 55
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/alfil_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 3
        a = alfil()
        a._id = 57
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/alfil_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 1
        a = torre()
        a._id = 56
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/torre_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 1
        x = 8
        a = torre()
        a._id = 57
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/torre_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 8
        x = 1
        a = torre()
        a._id = 58
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/torre_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

        y = 8
        x = 8
        a = torre()
        a._id = 59
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/aprisinsetti/Escritorio/Gmail/torre_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

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

            traducx = 24
            for item in range(8):
                x += 1




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


            y += 1
            traducy -= 82

    def no_me_rompas_las_bolas_maxi(self, list_aux,pieza):#mover las piezas

        ym,xm=0,0
        cx,cy=0,0

        while True:

            mouse = pygame.mouse.get_pos()

            for event in pygame.event.get():

                    keys = pygame.key.get_pressed()

                    for item in list_aux:


                        if keys[K_SPACE]:
                            xm = mouse[0]
                            ym = mouse[1]
                            for item_bloques in Tablero().lista_Bloques:

                                if item_bloques.traduccionx + 82 > xm > item_bloques.traduccionx and \
                                        item_bloques.traducciony + 82 > ym > item_bloques.traducciony:

                                    cy=item_bloques.poscy
                                    cx=item_bloques.poscx

                                    if cx == item[0]  and cy == item[1]:
                                        if pieza.color == "Blanco":
                                            if pieza._id == 1 and pieza.var_inicial and cx == 2:

                                                for item in Tablero().lista_Piezas:
                                                    if item._id==56:

                                                        item.mover(3,item.posy)
                                            if pieza._id == 1 and pieza.var_inicial and cx == 6:
                                                for item in Tablero().lista_Piezas:
                                                    if item._id==57:
                                                        item.mover(5, item.posy)
                                        if pieza.color == "Negro":
                                            if pieza._id == 0 and pieza.var_inicial and cx == 3:

                                                for item in Tablero().lista_Piezas:
                                                    if item._id == 58:
                                                        item.mover(4, item.posy)
                                            if pieza._id == 0 and pieza.var_inicial and cx == 7:
                                                for item in Tablero().lista_Piezas:
                                                    if item._id == 59:
                                                        item.mover(6, item.posy)
                                        pieza.mover(cx, cy)
                                        return
                    if keys[K_1]:
                        return

    def esta_Vaciox2(self):
        for item in self.lista_Bloques:
            item.esta_Vacio()




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

