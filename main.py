import pygame, sys
from pygame.locals import *
pygame.init()

green = (0, 200, 200)
ventana = pygame.display.set_mode((700,700))
pygame.display.set_caption("Martorille chess")

Board = pygame.image.load("/home/melman/Escritorio/Tablero.jpg")
posX, posY = 0, 0
ventana.blit(Board,(posX,posY))
ball = pygame.image.load("/home/melman/Escritorio/rsz_melma_puntito.png")

posbX = 150
posbY= 150
ventana.blit(ball, (posbX, posbY))

while True:



    for evento in pygame.event.get():



        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == 109: #mouse izq 1 der 3
            posbX = posbX + 100
            ventana.blit(Board, (posX, posY))
            ventana.blit(ball, (posbX, posbY))

        pygame.display.update()

