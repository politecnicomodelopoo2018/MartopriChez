import pygame, sys
from pygame.locals import *
from ClasesTablero import *

class pieza(object):
    color=None
    posx=None
    posy=None
    imagen=None
    viva=None

class rey(pieza):

    inicial = None

    def posibles_movimientos(self):


        for item in Tablero().lista_Piezas:
            if not (item.imagen == self.imagen):
                lista_total = +item.posibles_movimientos

        posibles_mov = []

        VariableParaImprimiry=self.posy + 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx+ 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        posibles_mov=+self.enroque()

        return posibles_mov

    def enroque(self):

        for item in Tablero().lista_Piezas:
            if item.posx == 1 and item.posy == 1 and item.color == "Blanco" and item.__class__.__name__ == "Torre":
                torre1 = item
            if item.posx == 8 and item.posy == 1 and item.color == "Blanco" and item.__class__.__name__ == "Torre":
                torre2 = item
        if self.inicial == True and torre1.inicial == True:
            x = self.posx-2
            y = self.posy
            lista =+ [[x,y]]
        if self.inicial == True and torre2.inicial == True:
            x = self.posx+2
            y = self.posy
            lista =+ [[x,y]]

        return lista

    def mover(self,x,y):

        self.posy = y
        self.posx = x

