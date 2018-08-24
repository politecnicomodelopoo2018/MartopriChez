import pygame, sys
from pygame.locals import *
from Clases import rey
pygame.init()

ventana = pygame.display.set_mode((700,700))
pygame.display.set_caption("Martorille chess")

Board = pygame.image.load("/home/melman/Escritorio/board.png")
posX, posY = 0, 0
ventana.blit(Board,(posX,posY))
ball = pygame.image.load("/home/melman/Escritorio/rsz_melma_puntito.png")
posbX = 5
posbY= 5
ventana.blit(ball, (posbX, posbY))
pepe = rey()
all_sprites = pygame.sprite.Group()
all_sprites.add(pepe)
print(pepe.rect.y)
pepe.rect.y = pepe.rect.y+1
while True:
    all_sprites.draw(ventana)



    for evento in pygame.event.get():
        print(evento)

        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN and evento.key == 109: #mouse izq 1 der 3
            posbX = posbX + 100
            ventana.blit(Board, (posX, posY))
            ventana.blit(ball, (posbX, posbY))

        pygame.display.update()

