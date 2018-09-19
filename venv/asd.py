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