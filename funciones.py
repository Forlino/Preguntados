def crear_sublista(lista, clave):
    '''
    Brief:
    Crea una sublista a partir de una lista de diccionarios, extrayendo un valor específico indicado por la clave.

    Parámetros:
    lista: La lista de diccionarios de la cual se extraerán los valores.
    clave: La clave que indica qué valor se debe extraer de cada diccionario en la lista.

    Retorno:
    Una lista que contiene los valores extraídos de cada diccionario.
    '''
    sublista = []
    for pregunta in lista:
        sublista.append(pregunta[clave])

    return sublista

def detectar_colision(posicion_mouse, diccionario_boton):
    '''
    Brief:
    Detecta si la posición del mouse colisiona con un botón representado por un diccionario de coordenadas.

    Parámetros:
    posicion_mouse: Una tupla que contiene las coordenadas (x, y) de la posición del mouse.
    diccionario_boton: Un diccionario que contiene las coordenadas (x, y), ancho y alto del botón.

    Retorno:
    True si hay colisión entre la posición del mouse y el botón, False en caso contrario.
    '''
    x_mouse = posicion_mouse[0]
    y_mouse = posicion_mouse[1]
    x = diccionario_boton['x']
    y = diccionario_boton['y']
    ancho = diccionario_boton['ancho']
    alto = diccionario_boton['alto']

    flag_colision_x = x_mouse >= x and x_mouse <= x + ancho
    flag_colision_y = y_mouse >= y and y_mouse <= y + alto

    return flag_colision_x and flag_colision_y