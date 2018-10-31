from Menu import*
import pygame
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
screen = pygame.display.set_mode((1600, 800))
board = pygame.image.load("/home/melman/Escritorio/Gmail/MENU.png")
ventana.blit(board, (0, 0))

while not salir:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                x=1920
                y=1080
                d ="/home/melman/Escritorio/Gmail/nuevapartidanombre.png"
                nombre = menus.tomarStrings(d,x,y)
                d ="/home/melman/Escritorio/Gmail/nomjugblanco.png"
                jugador_Blanco = menus.tomarStrings(d,x,y)
                d ="/home/melman/Escritorio/Gmail/idjugadorblanco.png"
                _id_jugador_Blanco = menus.tomarStrings(d,x,y)
                d ="/home/melman/Escritorio/Gmail/nombre jugador negro.png"
                jugador_Negro = menus.tomarStrings(d,x,y)
                d ="/home/melman/Escritorio/Gmail/idjugadornegro.png"
                _id_jugador_Negro = menus.tomarStrings(d,x,y)
                a = Partida()
                a.crear_partida(nombre, jugador_Blanco, _id_jugador_Blanco, jugador_Negro, _id_jugador_Negro)
                a.crearEnBdd()
                Juego(a)

            if event.key == pygame.K_2:
                x =1920
                y =1080
                f ="/home/melman/Escritorio/Gmail/NOMBREPJ.png"
                nombrePersonaje = menus.tomarStrings(f,x,y)
                f ="/home/melman/Escritorio/Gmail/ELOPG.png"
                eloPersonaje = menus.tomarStrings(f,x,y)

                eloPersonaje=int(eloPersonaje)
                a = jugador()
                a.crear_jugador(nombrePersonaje,eloPersonaje)

            if event.key == pygame.K_3:
                x=856
                y=500
                j ="/home/melman/Escritorio/Gmail/idpartidacargar.png"
                partida = menus.tomarStrings(j,x,y)
                partida = int(partida)
                a = GM().descargar_partidas(partida)
                GM().recrear_partida(a)


            if event.key == pygame.K_4:
                pygame.quit()
                sys.exit()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    pygame.display.flip()
    clock.tick(30)