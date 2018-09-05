import pygame, sys
from pygame.locals import *

class pieza(object):
    color=None
    posx=None
    posy=None
    imagen=None
    viva=None

class rey(pieza):

    def posibles_movimientos(self):

        posibles_mov = []

        VariableParaImprimiry=self.posy + 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx+ 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            lista_aux = []
            lista_aux.append(VariableParaImprimirx)
            lista_aux.append(VariableParaImprimiry)
            posibles_mov.append(lista_aux)

        return posibles_mov

