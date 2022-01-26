from clases import Jugador, Tablero

def movimiento_aleatorio():
    pass

def movimiento_ficha(x,y,jugador):
    pass

def comprobación_final_juego():
    pass

def error(mensaje):
    print(mensaje)
    exit()

def main():
    print('Bienevenido al tres en ralla juego, donde puedes elegir el tamaño del tablero. ')
    try: 
        tamaño_tablero = int(input('Introduce el tamaño del tablero: '))
    except:
        error('No ha introducido un número entero, porfavor reinicie el juevo para volver a intentarlo.')

    ficha_jugador_1 = input('El jugador 1 quiere jugar con ficha "X" o "O" ?: ')

    if ficha_jugador_1 == "X":
        ficha_jugador_2 = "O"
        print('Por lo tanto el jugador 2 será la ficha "O"')
    elif ficha_jugador_1 == "O":
        ficha_jugador_2 = "X"
        print('Por lo tanto el jugador 2 será la ficha "X"')
    else: 
        error('No ha introducido una ficha valida, porfavor reinicie el juevo para volver a intentarlo. ')
        
    jugador1 = Jugador(ficha_jugador_1) 
    jugador2 = Jugador(ficha_jugador_2) 

    tablero = Tablero(tamaño_tablero)

    print("El tablero creado ha sido el siguiente: ")
    tablero.imprimir_tablero()




main()