#peon
x=0
y=2
for item in range(8):
    a=peon()
    x += 1
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/peon_Blanco.png")
    a.viva = True
    a.var_inicial = True
x=0
for item in range(8):
    a=peon()
    x += 1
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/peon_Negro.png")
    a.viva = True
    a.var_inicial = True

y=1
x=1

for item in range(2):
    a=torre()
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen =pygame.image.load("/home/melman/Escritorio/piezas/torre_Blanco.png")
    a.viva = True
    a.var_inicial = True
    x += 7
    Tablero().lista_Piezas.append(a)
y=8
x=1

for item in range(2):
    a=torre()
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen =pygame.image.load("/home/melman/Escritorio/piezas/torre_Negro.png")
    a.viva = True
    a.var_inicial = True
    x += 7
    Tablero().lista_Piezas.append(a)

y=1
x=2

for item in range(2):
    a=caballo()
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen =pygame.image.load("/home/melman/Escritorio/piezas/caballo_Blanco.png")
    a.viva = True
    a.var_inicial = True
    x += 5
    Tablero().lista_Piezas.append(a)
y=8
x=2

for item in range(2):
    a=torre()
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen =pygame.image.load("/home/melman/Escritorio/piezas/caballo_Negro.png")
    a.viva = True
    a.var_inicial = True
    x += 5
    Tablero().lista_Piezas.append(a)

y = 1
x = 3

for item in range(2):
    a = alfil()
    a.color = "Blanco"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Blanco.png")
    a.viva = True
    a.var_inicial = True
    x += 3
    Tablero().lista_Piezas.append(a)
y = 8
x = 3

for item in range(2):
    a = alfil()
    a.color = "Negro"
    a.posx = x
    a.posy = y
    a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/alfil_Negro.png")
    a.viva = True
    a.var_inicial = True
    x += 3
    Tablero().lista_Piezas.append(a)

y = 1
x = 4


a = reina()
a.color = "Blanco"
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
a.posx = x
a.posy = y
a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/reina_Negro.png")
a.viva = True
a.var_inicial = True
Tablero().lista_Piezas.append(a)


y = 1
x = 4


a = rey()
a.color = "Blanco"
a.posx = x
a.posy = y
a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Blanco.png")
a.viva = True
a.var_inicial = True
Tablero().lista_Piezas.append(a)
y = 8
x = 5

a = rey()
a.color = "Negro"
a.posx = x
a.posy = y
a.imagen = pygame.image.load("/home/melman/Escritorio/piezas/rey_Negro.png")
a.viva = True
a.var_inicial = True
Tablero().lista_Piezas.append(a)

