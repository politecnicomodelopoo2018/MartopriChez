from Menu import*
import pygame
from creador import *
from pruba import Juego
from ClasesTablero import Tablero
from Clase_Partida import Partida
from bdd import *
from Mezcla import *


data = BD()

data.setConnection("127.0.0.1", "root", "alumno", "mydb")
print(data.run("Select * from Jugador;"))

pygame.init()

clock = pygame.time.Clock()
salir = False
screen = pygame.display.set_mode((1280, 700))
while not salir:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                nombre = menus.tomarStrings()
                jugador_Blanco = menus.tomarStrings()
                _id_jugador_Blanco = menus.tomarStrings()
                jugador_Negro = menus.tomarStrings()
                _id_jugador_Negro = menus.tomarStrings()
                a = Partida()
                a.crear_partida(nombre, jugador_Blanco, _id_jugador_Blanco, jugador_Negro, _id_jugador_Negro)
                a.crearEnBdd()
                Juego(a)

            if event.key == pygame.K_2:
                nombrePersonaje = menus.tomarStrings()
                eloPersonaje = menus.tomarStrings()
                #crearPersonaje
            if event.key == pygame.K_3:
                partida = menus.tomarStrings()
                a = GM().descargar_partidas(partida)
                GM().recrear_partida(a)

                #cargar partida
            if event.key == pygame.K_4:
                pygame.quit()
                sys.exit()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(30)