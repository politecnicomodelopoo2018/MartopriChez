import pymysql
import pygame as pg
import pygame, sys
from pygame.locals import *
pygame.init()
class menus(object):

    @staticmethod
    def tomarStrings():

        screen = pygame.display.set_mode((1280, 700))

        active = False
        text = ''
        salir = False
        font = pg.font.Font(None, 32)
        clock = pg.time.Clock()
        input_box = pg.Rect(500, 300, 140, 32)#Los dos primeros son la posicion,los dos segundos son el tamaño
        color_inactive = pg.Color('lightskyblue3')
        color_active = pg.Color('dodgerblue2')
        color = color_inactive
        while not salir:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    salir = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            print(text)
                            salir= True
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode


            screen.fill((252, 252, 252))
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            pg.draw.rect(screen, color, input_box, 2)
            pg.display.flip()
            clock.tick(30)

        return text