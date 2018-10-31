from ClasesTablero import *

def selec_reyes():
    for item in Tablero().lista_Piezas:
        if item._id == 0 and item.color == "Blanco":
            rey_blanco = item
        if item._id == 0 and item.color == "Negro":
            rey_negro = item
    return rey_blanco,rey_negro

def jaque(self):

    list_aux = []
    list_aux2 = []

    for item in Tablero().lista_Piezas:

        if item.color != self.color:

            list_aux += item.posibles_movimientos()

    for item in list_aux:
        if item[0] == self.posx and item[1] == self.posy:
           list_aux2.append(item)

    return list_aux2