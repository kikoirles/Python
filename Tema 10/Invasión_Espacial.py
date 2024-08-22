# bibliotecas al instalar ()
# pygame instalar de forma externa de la pagina

import pygame
import random
import math
from pygame import mixer
import io

def fuente_bytes (fuente):
    # Abre el archivo TTF en modo lectura binaria
    with open(fuente, 'rb') as f:
    # Lee todos los bytes del archivo y los alamacena en una variable
        ttf_bytes = f.read()
    # Crea un objeto BytesIO a partir de los bytes del archivo TTF
    return io.BytesIO(ttf_bytes)

# inicializar pygame
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo
pygame.display.set_caption("Invasion Espacial")
# Icono 32px
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
#fondo
fondo = pygame.image.load("Fondo.jpg")

# agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# jugador variables
img_jugador = pygame.image.load("cohete.png")
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0


# enemigo variables
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantida_enemigos = 8


for e in range(cantida_enemigos):
    img_enemigo.append(pygame.image.load("enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# bala variables
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 530
bala_x_cambio = 0
bala_y_cambio = 0.5
bala_visible = False

# Puntaje
puntaje = 0
fuente_como_bytes = fuente_bytes("freesansbold.ttf")
fuente = pygame.font.Font(fuente_como_bytes, 32)
texto_x = 10
texto_y = 10

# Texto final de juego
fuente_final = pygame.font.Font(fuente_como_bytes, 40)
def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (200, 250))

# funcion mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntos: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))



# funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# funcion enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

# Funcion dispara bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 16))

# Funcion detectar colision
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False

# hacer pantalla funcional para que salga del bulce cuando pulsemos X
se_ejecuta = True
while se_ejecuta:

    # rgb pantalla
    # pantalla.fill((205, 144, 228))
    # fondo de imagen
    pantalla.blit(fondo,(0,0))

    # Iterar lo eventos
    for evento in pygame.event.get():

        # evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # comprobaciones evento si el usuario pulsa una tecla
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.2
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = +0.2
                # Disparar bala
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.set_volume(0.1)
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(jugador_x, bala_y)

        # comprobaciones evento si el usuario suelta una tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modificar posiscion jugador
    jugador_x += jugador_x_cambio


    # mantener detro de bordes jugador
    if jugador_x <= 1:
        jugador_x = 1
    elif jugador_x >= 735:
        jugador_x = 735

    # modificar posiscion enemigo
    for e in range(cantida_enemigos):

        # fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantida_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    # mantener detro de bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 735:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        # colision
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.set_volume(0.1)
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= bala_y_cambio




    jugador(jugador_x,jugador_y)


    mostrar_puntaje(texto_x, texto_y)

    # actualizar
    pygame.display.update()
