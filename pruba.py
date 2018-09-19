import pygame, sys
from pygame.locals import *
from ClasesPiezas import *
from ClasesTablero import *



pygame.init()

ventana = pygame.display.set_mode((700,700))
red = (255, 0, 0)
blue = (0, 255, 0)

Board = pygame.image.load("/home/melman/Escritorio/Tablero.jpg")
posX, posY = 0, 0
pygame.display.set_caption("Martorille chess")
ball = pygame.image.load("/home/melman/Escritorio/rsz_153617249791251.png")
ventana.blit(Board,(posX,posY))
posbX = 230
posbY= 450
ventana.blit(ball, (posbX, posbY))

rey = rey()
rey.color = "Blanco"
rey.posy = 500
rey.posx = 500
rey.viva = True

reina = reina()
reina.color = "Blanco"
reina.posy = 120
reina.posx = 120
reina.imagen = pygame.image.load("/home/melman/Escritorio/piezas/reina_Blanco.png")
reina.viva = True
ventana.blit(reina.imagen,(reina.posx, reina.posy))
Tablero().lista_Piezas.append(reina)
rey.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Blanco.png")
ventana.blit(Board, (posX, posY))
ventana.blit(rey.imagen,(rey.posx, rey.posy))
Tablero().lista_Piezas.append(rey)

Tablero().crear_Bloques()

pepin = 0
while True:


    for evento in pygame.event.get():
        mouse = pygame.mouse.get_pos()

        ventana.blit(reina.imagen, (reina.posx, reina.posy))



        for item in range(64):
            if Tablero().lista_Bloques[item].traduccionx + 82 > mouse[0]> Tablero().lista_Bloques[item].traduccionx and\
                    Tablero().lista_Bloques[item].traducciony + 82 > mouse[1]> Tablero().lista_Bloques[item].traducciony \
                    and evento.type == pygame.MOUSEBUTTONDOWN and Tablero().lista_Bloques[item].Vacio == False:

               print(Tablero().lista_Bloques[item].Nombre)


        if evento.type == QUIT:
            pygame.quit()
            sys.exit()


        pygame.display.update()

