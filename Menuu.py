from Menu import *
import pygame

from creador import *
from pruba import Juego



pygame.init()

clock = pygame.time.Clock()
salir = False
screen = pygame.display.set_mode((1280, 700))
while not salir:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                idPartida = menus()
                nombre = menus()
                jugador_Blanco = menus()
                _id_jugador_Blanco = menus()
                jugador_Negro = menus()
                _id_jugador_Negro = menus()
                #crearPartida
                Juego()
            if event.key == pygame.K_2:
                nombrePersonaje = menus()
                eloPersonaje = menus()
                Juego()
                #crearPersonaje
            if event.key == pygame.K_3:
                partida = menus()
                #cargar partida
            if event.key == pygame.K_4:
                pygame.quit()
                sys.exit()


    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(30)