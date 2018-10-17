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

    def movimientos_invalidos(self):
        lista_total = []
        for item in Tablero().lista_Piezas:
            if item.posx == self.posx and not item.posy == self.posy and item.color == pieza.color:
                lista_total += item.posibles_movimientos()

        return lista_total

    def comer(self):
        for pieza in Tablero().lista_Piezas:
            for bloque in Tablero().lista_Bloques:
                if self.posx == pieza.posx and self.posy == pieza.posy and pieza._id != self._id and pieza.color != self.color:
                    pieza.viva = False

    def diferenciar(self):
        listita = []
        for pieza in Tablero().lista_Piezas:
            if pieza.color == self.color and pieza.viva:
                listaaux = []
                listaaux.append(pieza.posx)
                listaaux.append(pieza.posy)
                listita.append(listaaux)
        return listita

    def diferenciarColor(self):
        listita = []
        for pieza in Tablero().lista_Piezas:
            if pieza.color != self.color and pieza.viva:
                listaaux = []
                listaaux.append(pieza.posx)
                listaaux.append(pieza.posy)
                listita.append(listaaux)
        return listita


    def rayosX(self):
        vacia = []
        return vacia

    def mover(self,x,y):

        for bloque in Tablero().lista_Bloques:
            if self.posx == bloque.poscx and self.posy == bloque.poscy:
                bloque.Vacio = True

        self.posy = y
        self.posx = x
        self.inicial()


    def posibles_movimientos(self):

        return False

    def inicial(self):

         self.var_inicial = False


class rey(pieza):

    def jaque(self):

        list_aux = []
        list_aux2 = []

        for item in Tablero().lista_Piezas:

            if not item.color == self.color:
                list_aux += item.posibles_movimientos(False)

        for item in list_aux:
            if item[0] == self.posx and item[1] == self.posy:
                list_aux2.append(item)
        return list_aux2


    def posibles_movimientos(self, chequearJaque=True):

        lista_total_de_lugares=self.diferenciar()
        lista_total = self.movimientos_invalidos()
        if chequearJaque:
            lista_donde_atacan = self.jaque()


        posibles_mov = []

        VariableParaImprimiry=self.posy + 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx,VariableParaImprimiry] in lista_donde_atacan:
                            lista_aux = []
                            lista_aux.append(VariableParaImprimirx)
                            lista_aux.append(VariableParaImprimiry)
                            posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)
        VariableParaImprimiry = self.posy - 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)
        VariableParaImprimiry = self.posy + 0
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)

        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx - 1

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)
        VariableParaImprimiry = self.posy + 1
        VariableParaImprimirx = self.posx + 0

        if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
            if not [VariableParaImprimirx,VariableParaImprimiry] in lista_total:
                if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_donde_atacan:
                        lista_aux = []
                        lista_aux.append(VariableParaImprimirx)
                        lista_aux.append(VariableParaImprimiry)
                        posibles_mov.append(lista_aux)

        posibles_mov += self.enroque(lista_donde_atacan)

        return posibles_mov

    def enroque(self,lista_donde_atacan):
        lista_total_de_lugares = self.diferenciar()
        if self.color == "Blanco":
            lista = []
            torre1=None
            torre2=None

            for bloque in Tablero().lista_Bloques:
                if bloque.esta_Vacio() == False:
                    return
            for item in Tablero().lista_Piezas:

                if item._id == 56:
                    torre1 = item
                if item._id == 57:
                    torre2 = item

            if self.var_inicial == True and torre1.var_inicial == True:
                x = self.posx-2
                y = self.posy
                if not [x, y] in lista_total_de_lugares:
                   if not [x,y] in lista_donde_atacan:
                        lista += [[x,y]]
            if self.var_inicial == True and torre2.var_inicial == True:
                x = self.posx+2
                y = self.posy
                if not [x, y] in lista_total_de_lugares:
                    if not [x, y] in lista_donde_atacan:
                        lista += [[x,y]]
            return lista
        else:
            lista = []
            torre1 = None
            torre2 = None
            for item in Tablero().lista_Piezas:
                if item._id == 58:
                    torre1 = item
                if item._id == 59:
                    torre2 = item
            if self.var_inicial == True and torre1.var_inicial == True:
                x = self.posx - 2
                y = self.posy
                if not [x, y] in lista_total_de_lugares:
                    lista += [[x, y]]
            if self.var_inicial == True and torre2.var_inicial == True:
                x = self.posx + 2
                y = self.posy
                if not [x, y] in lista_total_de_lugares:
                    lista += [[x, y]]
            return lista


class caballo(pieza):

    def posibles_movimientos(self,a):
        reyx = 0
        reyy = 0
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

            i += 1

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
        reyx = 0
        reyy = 0
        lista_de_mov_posibles = []
        lista_color_opuesto = self.diferenciarColor()
        lista_total_de_lugares = self.diferenciar()
        lista_totalx = []
        if1 = True
        if2 = True
        if3 = True
        if4 = True

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

                i += 1

                list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx
                if if1:

                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if1 = False
                        else:
                                if1 = False


                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx
                if if2:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if2 = False
                        else:
                                if2 = False

                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx + i
                if if3:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if3 = False
                        else:
                                if3 = False

                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx - i
                if if4:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if4 = False
                        else:
                                if4 = False

            return lista_de_mov_posibles
        vacia = []
        return vacia


class alfil(pieza):

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
        lista_color_opuesto = self.diferenciarColor()
        lista_total_de_lugares = self.diferenciar()
        lista_totalx = []
        if1 = True
        if2 = True
        if3 = True
        if4 = True




        for item in Tablero().lista_Piezas:#ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):

                lista_totalx += item.rayosX()

        if [reyx, reyy] not in lista_totalx:

            i = 0
            for item in range(8):

                i += 1

                list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx + i
                if if1:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if1 = False
                        else:
                                if1 = False

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx - i
                if if2:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if2 = False
                        else:
                            if2 = False

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx + i
                if if3:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if3 = False
                        else:
                            if3 = False

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx - i
                if if4:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                if4 = False
                        else:
                            if4 = False


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
        posibles_mov = []
        if1 = True
        if2 = True
        if3 = True
        if4 = True
        if5 = True
        if6 = True
        if7 = True
        if8 = True

        lista_total_de_lugares = self.diferenciar()
        lista_total = self.movimientos_invalidos()
        lista_color_opuesto = self.diferenciarColor()



        for item in Tablero().lista_Piezas:#ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):

                lista_totalx += item.rayosX()

        if [reyx, reyy] not in lista_totalx:
            i = 0
            for item in range(8):

                i += 1

                list_aux = []

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx + i
                if if1:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:


                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if1 = False
                        else:
                                if1 = False

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx - i
                if if2:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if2 = False
                        else:
                            if2 = False
                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx + i

                if if3:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if3 = False
                        else:
                            if3 = False

                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx - i
                if if4:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if4 = False
                        else:
                            if4 = False
                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx + i

                if if5:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if5 = False
                        else:
                            if5 = False

                VariableParaImprimiry = self.posy
                VariableParaImprimirx = self.posx - i
                if if6:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if6 = False
                        else:
                            if6 = False

                VariableParaImprimiry = self.posy - i
                VariableParaImprimirx = self.posx
                if if7:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                list_aux = []
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if7 = False
                        else:
                            if7 = False
                VariableParaImprimiry = self.posy + i
                VariableParaImprimirx = self.posx
                if if8:
                    if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:

                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                posibles_mov.append(list_aux)
                                if [VariableParaImprimirx, VariableParaImprimiry] in lista_color_opuesto:
                                    if8 = False
                        else:
                            if8 = False

        return posibles_mov
        # vacia = []
        # return vacia


class peon(pieza):

    def posibles_movimientos(self):
        reyx = 0
        reyy = 0
        lista_de_mov_posibles = []
        lista_total_de_lugares = self.diferenciar()
        lista_de_opuestos = self.diferenciarColor()
        lista_totalx = []
        for item in Tablero().lista_Piezas:  # ataque al rey por rayosx
            if item.__class__.__name__ == "rey" and self.color == item.color:
                reyx = item.posx
                reyy = item.posy
            if not (item.imagen == self.imagen and item.color == self.color):
                lista_totalx += item.rayosX()


        if self.color == "Blanco":
            if  [reyx , reyy] not in lista_totalx:

                list_aux = []
                VariableParaImprimiry = self.posy + 1
                VariableParaImprimirx = self.posx

                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_de_opuestos :
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
                            list_aux = []

                for comer in Tablero().lista_Piezas:
                    if comer.posx == self.posx + 1 and comer.posy == self.posy + 1 and comer.color != self.color:
                            list_aux.append(self.posx+1)
                            list_aux.append(self.posy+1)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []

                    if comer.posx == self.posx - 1 and comer.posy == self.posy + 1 and comer.color != self.color:
                            list_aux.append(self.posx-1)
                            list_aux.append(self.posy+1)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []



        else:
            if  [reyx, reyy] not in lista_totalx:
                list_aux = []
                VariableParaImprimiry = self.posy - 1
                VariableParaImprimirx = self.posx

                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_de_opuestos:
                            list_aux.append(VariableParaImprimirx)
                            list_aux.append(VariableParaImprimiry)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []

                VariableParaImprimiry = self.posy -2
                VariableParaImprimirx = self.posx

                if not (VariableParaImprimirx < 0 or 8 < VariableParaImprimirx or 8 < VariableParaImprimiry or 0 > VariableParaImprimiry):
                    if not [VariableParaImprimirx, VariableParaImprimiry] in lista_total_de_lugares:
                        if not [VariableParaImprimirx, VariableParaImprimiry] in lista_de_opuestos:
                            if self.var_inicial:
                                list_aux.append(VariableParaImprimirx)
                                list_aux.append(VariableParaImprimiry)
                                lista_de_mov_posibles.append(list_aux)

                for comer in Tablero().lista_Piezas:
                    if comer.posx == self.posx - 1 and comer.posy == self.posy - 1 and comer.color != self.color:
                            list_aux.append(self.posx-1)
                            list_aux.append(self.posy-1)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []

                    if comer.posx == self.posx + 1 and comer.posy == self.posy - 1 and comer.color != self.color:
                            list_aux.append(self.posx+1)
                            list_aux.append(self.posy-1)
                            lista_de_mov_posibles.append(list_aux)
                            list_aux = []


        return lista_de_mov_posibles

