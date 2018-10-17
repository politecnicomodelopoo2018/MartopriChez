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

import pymysql

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1280, 700))

active = False
text = ''
salir = False
while not salir:
    for event in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and 100 + 20 > mouse[0] and 100 + 20 > mouse[1]:
            font = pygame.font.Font(None, 32)
            clock = pygame.time.Clock()
            input_box = pygame.Rect(500, 300, 140, 32)
            color_inactive = pygame.Color('lightskyblue3')
            color_active = pygame.Color('dodgerblue2')

            color = color_inactive
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pygame.draw.rect(screen, color, input_box, 2)
            pygame.display.flip()
            print(text)
            clock.tick(30)

            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    salir = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

