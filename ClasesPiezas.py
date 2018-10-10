import pygame, sys
from pygame.locals import *
from ClasesTablero import *


class pieza(object):
    _id = None
    color = None
    posx = None
    posy = None
    imagen = None
    viva = None
    var_inicial = True

    def comer(self):
        for pieza in Tablero().lista_Piezas:
            if self.posx == pieza.posx and self.posy == pieza.posy and pieza._id != self._id and pieza.color != self.color:
                pieza.viva = False
    def rayosX(self):
        vacia = []
        return vacia

    def mover(self,x,y):

        self.posy = y
        self.posx = x
        self.inicial()

    def posibles_movimientos(self):

        return False

    def inicial(self):

         self.var_inicial = False

class rey(pieza):

    def movimientos_invalidos(self):
        lista_total = []
        for item in Tablero().lista_Piezas:
            print("hodfdfdla")
            if item.posx == self.posx and not item.posy == self.posy:
                lista_total += item.posibles_movimientos()

        return lista_total

    def posibles_movimientos(self):

        lista_total_de_lugares=[]
        lista_total = self.movimientos_invalidos()


        for item in Tablero().lista_Piezas:#no salta sobre piesas del mismo color
            if self.posy != item.posy and self.posx != item.posx and self.color == item.color:
                print(9)
                lista_aux = []
                lista_aux.append(item.posx)
                lista_aux.append(item.posy)
                lista_total_de_lugares.append(lista_aux)


        posibles_mov = []

        VariableParaImprimiry=self.posy + 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total_de_lugares:
                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx+ 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            #if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                lista_aux = []
                lista_aux.append(VariableParaImprimirx)
                lista_aux.append(VariableParaImprimiry)
                posibles_mov.append(lista_aux)

        #posibles_mov += self.enroque()

        return posibles_mov

    def enroque(self):

        lista = []

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


class caballo(pieza):

    def posibles_movimientos(self):

        lista_totalx = []

        lista_total_de_lugares=[]
        for item in Tablero().lista_Piezas:#no salta sobre piesas del mismo color
            if self.posy != item.posy and self.posx != item.posx and self.color == item.color:
                lista_aux = []
                lista_aux.append(item.posx)
                lista_aux.append(item.posy)
                lista_total_de_lugares.append(lista_aux)

        for item in Tablero().lista_Piezas:#ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):
                print(item)
                lista_totalx += item.rayosX()

        if [reyx , reyy] not in lista_totalx:

            posibles_mov = []


            VariableParaImprimiry=self.posy + 2
            VariableParaImprimirx = self.posx -1

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy + 2
            VariableParaImprimirx = self.posx + 1

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy + 1
            VariableParaImprimirx = self.posx + 2

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy - 1
            VariableParaImprimirx = self.posx + 2

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy - 2
            VariableParaImprimirx = self.posx + 1

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy - 2
            VariableParaImprimirx = self.posx - 1

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy - 1
            VariableParaImprimirx = self.posx - 2

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)

            VariableParaImprimiry = self.posy + 1
            VariableParaImprimirx = self.posx - 2

            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    lista_aux = []
                    lista_aux.append(VariableParaImprimirx)
                    lista_aux.append(VariableParaImprimiry)
                    posibles_mov.append(lista_aux)



            return posibles_mov

        vacia=[]
        return vacia


class torre(pieza):

    def rayosx(self):

        lista_de_rayosx = []

        i = 0

        for item in range(8):

            i=+1

            list_aux = []

            VariableParaImprimiry = self.posy + i
            VariableParaImprimirx = self.posx
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy - i
            VariableParaImprimirx = self.posx
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy
            VariableParaImprimirx = self.posx + i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy
            VariableParaImprimirx = self.posx - i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)

        return lista_de_rayosx

    def posibles_movimientos(self):

        lista_de_mov_posibles = []

        lista_total_de_lugares = []

        lista_totalx = []

        for item in Tablero().lista_Piezas:#no salta sobre piesas del mismo color
            if self.posy != item.posy and self.posx != item.posx and self.color == item.color:
                lista_aux = []
                lista_aux.append(item.posx)
                lista_aux.append(item.posy)
                lista_total_de_lugares.append(lista_aux)

        for item in Tablero().lista_Piezas:#ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):
                lista_totalx += item.rayosX()

        if [reyx , reyy] not in lista_totalx:
            i = 0
            for item in range(8):

                i = +1

                list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx + i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx - i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)


            return lista_de_mov_posibles
        vacia = []
        return vacia


class alfil(pieza):

    def rayosx(self):

        lista_de_rayosx = []

        i = 0

        for item in range(8):

            i+=1

            list_aux = []

            VariableParaImprimiry = self.posy + i
            VariableParaImprimirx = self.posx + i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy - i
            VariableParaImprimirx = self.posx - i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy -i
            VariableParaImprimirx = self.posx + i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy + i
            VariableParaImprimirx = self.posx - i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)

        return lista_de_rayosx

    def posibles_movimientos(self):
        reyx = 0
        reyy = 0
        lista_de_mov_posibles = []

        lista_total_de_lugares = []

        lista_totalx = []

        for item in Tablero().lista_Piezas:#no salta sobre piesas del mismo color
            if self.posy != item.posy and self.posx != item.posx and self.color == item.color:
                lista_aux = []
                lista_aux.append(item.posx)
                lista_aux.append(item.posy)
                lista_total_de_lugares.append(lista_aux)

        for item in Tablero().lista_Piezas:#ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):
                print(item)
                lista_totalx += item.rayosX()

        if [reyx , reyy] not in lista_totalx:
            i = 0
            for item in range(8):

                i = +1

                list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx + i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx - i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx + i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx - i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)


            return lista_de_mov_posibles
        vacia = []
        return vacia


class reina(pieza):

    def rayosx(self):

        lista_de_rayosx = []

        i = 0

        for item in range(8):

            i += 1

            list_aux = []

            VariableParaImprimiry = self.posy + i
            VariableParaImprimirx = self.posx + i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy - i
            VariableParaImprimirx = self.posx - i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy - i
            VariableParaImprimirx = self.posx + i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy + i
            VariableParaImprimirx = self.posx - i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy + i
            VariableParaImprimirx = self.posx
            if not ( VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy - i
            VariableParaImprimirx = self.posx
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy
            VariableParaImprimirx = self.posx + i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)
                list_aux = []

            VariableParaImprimiry = self.posy
            VariableParaImprimirx = self.posx - i
            if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                list_aux.append(VariableParaImprimirx)
                list_aux.append(VariableParaImprimiry)
                lista_de_rayosx.append(list_aux)

        return lista_de_rayosx

    def posibles_movimientos(self):
        reyx = 0
        reyy = 0
        lista_totalx =[]

        lista_de_mov_posibles = []

        lista_total_de_lugares = []

        for item in Tablero().lista_Piezas:#no salta sobre piesas del mismo color
            if self.posy != item.posy and self.posx != item.posx and self.color == item.color:
                lista_aux = []
                lista_aux.append(item.posx)
                lista_aux.append(item.posy)
                lista_total_de_lugares.append(lista_aux)

        for item in Tablero().lista_Piezas:#ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):
                print (item)
                lista_totalx += item.rayosX()

        if [reyx, reyy] not in lista_totalx:
            i = 0
            for item in range(8):

                i += 1
                print(i)
                list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx + i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx - i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx + i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx - i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []
                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx + i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx - i
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx
                if not (
                        VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx
                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)

        return lista_de_mov_posibles
        # vacia = []
        # return vacia


class peon(pieza):

    def posibles_movimientos(self):
        reyx = 0
        reyy = 0
        lista_de_mov_posibles = []
        lista_total_de_lugares = []
        lista_totalx = []
        for item in Tablero().lista_Piezas:  # ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):
                lista_totalx += item.rayosX()

        for item in Tablero().lista_Piezas:#no salta sobre piesas del mismo color
            if self.posy != item.posy and self.posx != item.posx:
                lista_aux = []
                lista_aux.append(item.posx)
                lista_aux.append(item.posy)
                lista_total_de_lugares.append(lista_aux)
        if self.color == "Blanco":
            if  [reyx , reyy] not in lista_totalx:
                list_aux = []
                VariableParaImprimiry = self.posy + 1
                VariableParaImprimirx = self.posx

                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy + 2
                VariableParaImprimirx = self.posx

                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        if self.var_inicial:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)

        else:
            if  [reyx, reyy] not in lista_totalx:
                list_aux = []
                VariableParaImprimiry = self.posy - 1
                VariableParaImprimirx = self.posx

                if not (
                        VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        list_aux.append(VariableParaImprimirx)
                        list_aux.append(VariableParaImprimiry)
                        lista_de_mov_posibles.append(list_aux)
                        list_aux = []

                VariableParaImprimiry = self.posy -2
                VariableParaImprimirx = self.posx

                if not (
                        VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        if self.var_inicial:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)

        return lista_de_mov_posibles

