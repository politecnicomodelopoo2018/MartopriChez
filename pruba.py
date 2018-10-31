
import pygame, sys
from pygame.locals import *
from ClasesPiezas import *
from ClasesTablero import *




pygame.init()
def Juego(partida):
        turno = "Blanco"
        crearpiezas()


        ventana = pygame.display.set_mode((700,700))

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

        while True:

            for evento in pygame.event.get():
                mouse = pygame.mouse.get_pos()

                keys = pygame.key.get_pressed()
                if keys[K_LEFT]:
                    for item in Tablero().lista_Bloques:

                        if item.traduccionx + 82 > mouse[0] > item.traduccionx and \
                                item.traducciony + 82 > mouse[1] > item.traducciony \
                                and item.Vacio is False:

                            for pieza in Tablero().lista_Piezas:

                                if pieza.posx == item.poscx and pieza.posy == item.poscy and pieza.viva == True and pieza.color == turno:
                                    lista_de_posibles_mov = Tablero().posibles_mov(pieza)
                                    pygame.display.update()
                                    turno=Tablero().no_me_rompas_las_bolas_maxi(lista_de_posibles_mov, pieza,turno)
                                    partida.guardar_mov(pieza)
                                    pieza.comer()
                                    Tablero().imprimir()
                                    Tablero().esta_Vaciox2()





                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()





        # pygame.display.update()


def crearpiezas():
    x = 0
    y = 2
    cont = 2
    for item in range(8):
        a = peon()
        a._id = cont
        x += 1
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/peon_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)
        cont = cont + 1

    x = 0
    y = 7
    cont = 10
    for item in range(8):
        a = peon()
        a._id = cont
        x += 1
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/peon_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)
        cont = cont + 1

    y = 1
    x = 4

    a = rey()
    a.color = "Blanco"
    a._id = 0
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)
    y = 8
    x = 5

    a = rey()
    a._id = 1
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 5

    a = reina()
    a.color = "Blanco"
    a._id = 18
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/reina_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)
    y = 8
    x = 4

    a = reina()
    a.color = "Negro"
    a._id = 19
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/reina_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 2

    a = caballo()
    a._id = 20
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 7

    a = caballo()
    a._id = 21
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 2
    a = caballo()
    a._id = 22
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 7
    a = caballo()
    a._id = 23
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 3

    a = alfil()
    a._id = 24
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 6

    a = alfil()
    a._id = 25
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 6
    a = alfil()
    a._id = 26
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 3
    a = alfil()
    a._id = 27
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 1
    a = torre()
    a._id = 28
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 8
    a = torre()
    a._id = 29
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 1
    a = torre()
    a._id = 30
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 8
    a = torre()
    a._id = 31
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)