import pygame
import numpy as np
import time


pygame.init()

ancho, alto = 500, 500
screen = pygame.display.set_mode((ancho, alto))
fondo = 25, 25, 25
screen.fill(fondo)

celdasX, celdasY = 100, 100
celdaAncho = ancho/celdasX
celdaAlto = alto/celdasY

estado = np.zeros((celdasX, celdasY))
estado[5, 3] = 1
estado[5, 4] = 1
estado[5, 5] = 1

estado[11, 11] = 1
estado[12, 12] = 1
estado[13, 12] = 1
estado[13, 11] = 1
estado[13, 10] = 1

while True:

    nuevoEstado = np.copy(estado)
    screen.fill(fondo)

    evento = pygame. event.get()

    for ev in evento:
        if ev.type == pygame.KEYDOWN:
            exit()

    for y in range(0, celdasY):
        for x in range(0, celdasX):

            numVecinos = estado[(x-1) % celdasX, (y-1) % celdasY] + \
                estado[(x-1) % celdasX, y % celdasY] + \
                estado[(x-1) % celdasX, (y+1) % celdasY] + \
                estado[x % celdasX, (y-1) % celdasY] + \
                estado[x % celdasX, (y+1) % celdasY] + \
                estado[(x+1) % celdasX, (y-1) % celdasY] + \
                estado[(x+1) % celdasX, y % celdasY] + \
                estado[(x+1) % celdasX, (y+1) % celdasY]

            if estado[x, y] == 0 and numVecinos == 3:
                nuevoEstado[x, y] = 1
            elif estado[x, y] == 1 and (numVecinos < 2 or numVecinos > 3):
                nuevoEstado[x, y] = 0

            poly = [
                (x * celdaAncho, y * celdaAlto),
                ((x+1) * celdaAncho, y * celdaAlto),
                ((x+1) * celdaAncho, (y+1) * celdaAlto),
                (x * celdaAncho, (y+1) * celdaAlto)
            ]

            if nuevoEstado[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

    estado = np.copy(nuevoEstado)
    pygame.display.flip()
time.sleep(0.1)
