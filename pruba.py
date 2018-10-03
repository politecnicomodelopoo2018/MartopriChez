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
for item in Tablero().lista_Piezas:
    for item2 in Tablero().lista_Bloques:
        if item2.poscx == item.posx and item2.poscy == item.posy:
            ventana.blit(item.imagen, (item2.traduccionx + 20, item2.traducciony + 5))
            item2.esta_Vacio()
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

                        if pieza.posx == item.poscx and pieza.posy == item.poscy:
                            lista_de_posibles_mov = Tablero().posibles_mov(pieza)
                            print(lista_de_posibles_mov)
                            pygame.display.update()
                            Tablero().no_me_rompas_las_bolas_maxi(lista_de_posibles_mov, pieza, evento, mouse)
                            Tablero().imprimir()




        if evento.type == QUIT:
            pygame.quit()
            sys.exit()



        pygame.display.update()

