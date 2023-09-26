import pygame
from constantes import *
from datos import lista
from funciones import *

pygame.init() #Se inicializa pygame


PANTALLA = pygame.display.set_mode((W, H)) # Se crea una ventana

pygame.display.set_caption("Preguntados") # Nombre de la ventana

icono = pygame.image.load("imagenes/icono.png") # carga el icono
pygame.display.set_icon(icono)
# se cargan las distintas imagenes utilizadas
img_willy = pygame.image.load("imagenes/Willy.png") 
img_dialogo = pygame.image.load("imagenes/dialogo.png") 
img_dialogo = pygame.transform.scale(img_dialogo, (700, 250))
# el tipo de fuente para la letra
fuente_pregunta = pygame.font.SysFont("arial", 25)

fuente_boton_pregunta = pygame.font.SysFont("arial", 25)

fuente_opciones = pygame.font.SysFont("arial", 30)

fuente_score = pygame.font.SysFont("arial", 45)

msg_boton_pregunta = fuente_boton_pregunta.render("Pregunta", True, "#1C1F21")
msg_boton_reiniciar = fuente_boton_pregunta.render("Reiniciar", True, "#1C1F21")

sublista_preguntas = crear_sublista(lista, 'pregunta')
sublista_opcion_a = crear_sublista(lista, 'a')
sublista_opcion_b = crear_sublista(lista, 'b')
sublista_opcion_c = crear_sublista(lista, 'c')
sublista_correctas = crear_sublista(lista, 'correcta')

score = 0

flag_esta_jugando = False

flag_game_over = False

pregunta_actual = -1

vidas = 2

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: 
            pygame.quit() #cierra el juego
            exit()
        elif evento.type == pygame.MOUSEBUTTONDOWN: # Si hace 1 click el usuario
            pos = pygame.mouse.get_pos() #pos = posicion del mouse
            if detectar_colision(pos, BOTON_REINICIAR):
                vidas = 2
                pregunta_actual = 0
                score = 0
                flag_esta_jugando = True
                flag_game_over = False

            if flag_esta_jugando == False:
                if detectar_colision(pos, BOTON_PREGUNTA):
                    pregunta_actual += 1
                    flag_esta_jugando = True
                    vidas = 2
            elif flag_game_over == False:
                opcion_elegida = None
                if detectar_colision(pos, OPCION_A):
                    opcion_elegida = 'a'
                elif detectar_colision(pos, OPCION_B):
                    opcion_elegida = 'b'
                elif detectar_colision(pos, OPCION_C):
                    opcion_elegida = 'c'
                
                if opcion_elegida != None:
                    if sublista_correctas[pregunta_actual] == opcion_elegida:
                        score += 10
                        flag_esta_jugando = False
                    else:
                        vidas -= 1
            
    PANTALLA.fill("#F3CDBE")
    PANTALLA.blit(img_willy, (750,300))
    PANTALLA.blit(img_dialogo, (50,150))

    


    


    # Boton pregunta
    pygame.draw.rect(PANTALLA, "#EB866F", (BOTON_PREGUNTA['x'],
                                           BOTON_PREGUNTA['y'],
                                           BOTON_PREGUNTA["ancho"],
                                           BOTON_PREGUNTA["alto"]), 0, 30)
    PANTALLA.blit(msg_boton_pregunta, (52, 53))


    # Boton Reiniciar
    pygame.draw.rect(PANTALLA, "#EDFF68", (BOTON_REINICIAR['x'],
                                           BOTON_REINICIAR['y'],
                                           BOTON_REINICIAR["ancho"],
                                           BOTON_REINICIAR["alto"]), 0, 30)
    PANTALLA.blit(msg_boton_reiniciar, (865, 53))

    # Franja de abajo
    pygame.draw.rect(PANTALLA, "#B4E4DA", (0,H - 250, W, 250))

    # Boton de Opcion a
    pygame.draw.rect(PANTALLA, "#160E33", (OPCION_A['x'],
                                           OPCION_A['y'],
                                           OPCION_A["ancho"],
                                           OPCION_A["alto"]), 0, 30)

    # Boton de Opcion b
    pygame.draw.rect(PANTALLA, "#160E33", (OPCION_B['x'],
                                           OPCION_B['y'],
                                           OPCION_B["ancho"],
                                           OPCION_B["alto"]), 0, 30)
    # Boton de Opcion c
    pygame.draw.rect(PANTALLA, "#160E33", (OPCION_C['x'],
                                           OPCION_C['y'],
                                           OPCION_C["ancho"],
                                           OPCION_C["alto"]), 0, 30)
    if vidas == 0:
        flag_esta_jugando = False

    if pregunta_actual >= len(lista):
        flag_game_over = True

    if flag_game_over == False:
        if flag_esta_jugando == True and pregunta_actual != -1:

            texto_pregunta = sublista_preguntas[pregunta_actual]
            texto_opcion_a = sublista_opcion_a[pregunta_actual]
            texto_opcion_b = sublista_opcion_b[pregunta_actual]
            texto_opcion_c = sublista_opcion_c[pregunta_actual]

            msg_opcion_a = fuente_opciones.render(texto_opcion_a, True, "#F6F7EB")
            msg_opcion_b = fuente_opciones.render(texto_opcion_b, True, "#F6F7EB")
            msg_opcion_c = fuente_opciones.render(texto_opcion_c, True, "#F6F7EB")

            PANTALLA.blit(msg_opcion_a, (190, 641))
            PANTALLA.blit(msg_opcion_b, (440, 641))
            PANTALLA.blit(msg_opcion_c, (690, 641))
        else:
            texto_pregunta = "Toque pregunta para continuar"
    else:
        texto_pregunta = f"Tu Puntaje final es: {score}"

    # bliteo texto pregunta
    msg_pregunta = fuente_pregunta.render(texto_pregunta, True, "#1C1F21")
    PANTALLA.blit(msg_pregunta, (100, 222))

    texto_score = f"Score: {score}"
    msg_score = fuente_score.render(texto_score, True, "#F6F7EB")
    PANTALLA.blit(msg_score, (430, 40))

    pygame.display.update() # actualiza la pantalla todo el tiempo