
from ClasesTablero import *
from ClasesPiezas import *



def crearpiezas():
    x = 0
    y = 2
    cont = 2
    for item in range(8):
        a = peon()
        a._id = cont
        x += 1
        a.color = "Blanco"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/peon_Blanco.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)

    x = 0
    y = 7
    cont = 2
    for item in range(8):
        a = peon()
        a._id = cont
        x += 1
        a.color = "Negro"
        a.posx = x
        a.posy = y
        a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/peon_Negro.png")
        a.viva = True
        a.var_inicial = True
        Tablero().lista_Piezas.append(a)


    y = 1
    x = 4

    a = rey()
    a.color = "Blanco"
    a._id = 1
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)
    y = 8
    x = 5

    a = rey()
    a._id = 0
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 5

    a = reina()
    a.color = "Blanco"
    a._id = 20
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/reina_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)
    y = 8
    x = 4

    a = reina()
    a.color = "Negro"
    a._id = 21
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/reina_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 2

    a = caballo()
    a._id = 40
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 7

    a = caballo()
    a._id = 41
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 2
    a = caballo()
    a._id = 42
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 7
    a = caballo()
    a._id = 42
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/caballo_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 3

    a = alfil()
    a._id = 50
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 6

    a = alfil()
    a._id = 54
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 6
    a = alfil()
    a._id = 55
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 3
    a = alfil()
    a._id = 57
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 1
    a = torre()
    a._id = 56
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 1
    x = 8
    a = torre()
    a._id = 57
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Blanco.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 1
    a = torre()
    a._id = 58
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)

    y = 8
    x = 8
    a = torre()
    a._id = 59
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/torre_Negro.png")
    a.viva = True
    a.var_inicial = True
    Tablero().lista_Piezas.append(a)