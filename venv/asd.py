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

def no_me_rompas_las_bolas_maxi(self,list_aux):
    while True:
        for item3 in list_aux:
            for item_bloques in Tablero().lista_Bloques:
                print(list_aux)
                print(item3[0])
                print(item3[1])

                if evento.type == pygame.MOUSEBUTTONDOWN and \
                        item_bloques.traduccionx + 82 > mouse[0] > item_bloques.traduccionx and \
                        item_bloques.traducciony + 82 > mouse[1] > item_bloques.traducciony:
                    item2.mover(item3[0], item3[1])
                    print("tu vieja")
                    ventana.blit(item2.imagen, (item_bloques.traduccionx, item_bloques.traducciony))
                    return


Tablero().no_me_rompas_las_bolas_maxi(lista_de_posibles_mov, pieza, evento, mouse)

if evento.type == pygame.KEYDOWN and hola != 0:
    mouse2 = pygame.mouse.get_pos()

    for bloque in Tablero().lista_Bloques:
        for buscar in Tablero().lista_Piezas:
            print("hola")

            if buscar.nombre == piezamover:
                buscar.posx = 3
                Tablero().imprimir()
                hola = 0
                print(piezamover)
                piezamover = ""

            if buscar.posx == bloque.poscx and buscar.posy == bloque.poscy:
                bloque.Vacio = False

if evento.type == QUIT:
    pygame.quit()
    sys.exit()

pygame.display.update()

if evento.type == QUIT:
    pygame.quit()
    sys.exit()

pygame.display.update()

