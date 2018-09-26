import pygame, sys
from pygame.locals import *
from ClasesPiezas import *
from ClasesTablero import *



pygame.init()


y = 1
x = 4


a = rey()
a.color = "Blanco"
a.posx = x
a.posy = y
a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Blanco.png")
a.viva = True
a.var_inicial = True
Tablero().lista_Piezas.append(a)
y = 8
x = 5

a = rey()
a.color = "Negro"
a.posx = x
a.posy = y
a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Negro.png")
a.viva = True
a.var_inicial = True
Tablero().lista_Piezas.append(a)





ventana = pygame.display.set_mode((700,700))
red = (255, 0, 0)
blue = (0, 255, 0)

Board = pygame.image.load("/home/melman/Escritorio/Tablero.jpg")
posX, posY = 0, 0
pygame.display.set_caption("Martorille chess")
ball = pygame.image.load("/home/melman/Escritorio/rsz_153617249791251.png")
ventana.blit(Board, (posX, posY))
Tablero().lista_Piezas.append(rey)

Tablero().crear_Bloques()

pepin = 0
while True:
    for item in Tablero().lista_Piezas:
        for item2 in Tablero().lista_Bloques:
            if item2.poscx == item.posx and item2.poscy == item.posy:
                ventana.blit(item.imagen, (item2.traduccionx + 20, item2.traducciony + 5))
                item2.esta_Vacio()

    for evento in pygame.event.get():
        mouse = pygame.mouse.get_pos()



        for item in range(64):
            if Tablero().lista_Bloques[item].traduccionx + 82 > mouse[0]> Tablero().lista_Bloques[item].traduccionx and\
                    Tablero().lista_Bloques[item].traducciony + 82 > mouse[1]> Tablero().lista_Bloques[item].traducciony \
                    and evento.type == pygame.MOUSEBUTTONDOWN and Tablero().lista_Bloques[item].Vacio == False:
                for item2 in Tablero().lista_Piezas:
                    if item2.posx == Tablero().lista_Bloques[item].poscx and item2.posy == Tablero().lista_Bloques[item].poscy:
                        Tablero().posibles_mov(item2)#faltan los rayos x del peon
                        list_aux = item2.posibles_movimientos()
                        pygame.display.update()
                        while True:
                            for item3 in list_aux:
                                for item_bloques in Tablero().lista_Bloques:
                                    print ("tu vieja")
                                    if item_bloques.poscx == item3[0] and item_bloques.poscy == item3[1] and evento.type == pygame.MOUSEBUTTONDOWN and mouse[0] == item_bloques.traduccionx and mouse[1] == item_bloques.traducciony:
                                        item2.mover(item3[0],item3[1])
                                        ventana.blit(item2.imagen, (item_bloques.traduccionx, item_bloques.traducciony))
                                        break


            if evento.type == QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

