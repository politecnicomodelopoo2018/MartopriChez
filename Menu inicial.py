from Menu import*
import pygame
from pygame.locals import *
from creador import *
pygame.init()
clock = pg.time.Clock()
salir = False
screen = pygame.display.set_mode((1280, 700))
while not salir:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                a = menus()
                b = menus()
                c = menus()
                d = menus()
                e = menus()
                f = menus()
                #crearPartida
            if event.key == pygame.K_2:
                j = menus()
                #crearPersonaje
            if event.key == pygame.K_3:
                partida = menus()
                #cargar partida
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pg.display.flip()
    clock.tick(30)