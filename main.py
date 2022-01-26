import random
from clases import Jugador, Tablero


def movimiento_jugador(x,y,jugador, tablero):
    # Si no es la maquina el numero es 1, la maquina siempre tiene el número 2.
    if jugador.numero == 1:  
        if tablero.movimiento_correcto(x,y) == False:
            x = int(input(f'Introduce un número de la fila correcto, del 0 al {len(tablero.matriz) - 1}: '))
            y = int(input(f'Introduce un número de la columna correcto, del 0 al {len(tablero.matriz) - 1}:'))
            while tablero.movimiento_correcto(x,y) != True:
                x = int(input(f'Introduce un número de la fila correcto, del 0 al {len(tablero.matriz) - 1}: '))
                y = int(input(f'Introduce un número de la columna correcto, del 0 al {len(tablero.matriz) - 1}:'))
            print(tablero.matriz)
            tablero.movimiento(x,y,jugador)
        else:
            tablero.movimiento(x,y,jugador)
    else:
        if tablero.movimiento_correcto(x,y) == False:
            x = random.randint(0,len(tablero.matriz) - 1)
            y = random.randint(0,len(tablero.matriz) - 1)
            while tablero.movimiento_correcto(x,y) != True:
                x = random.randint(0,len(tablero.matriz) - 1)
                y = random.randint(0,len(tablero.matriz) - 1)
            tablero.movimiento(x,y,jugador)
        else:
            tablero.movimiento(x,y,jugador)
        


def comprobación_ganador(tablero, jugador):
    if tablero.comprobar_diagonal_principal(jugador) or tablero.comprobar_diagonal_secundaria(jugador) or tablero.comprobar_filas(jugador) or tablero.comprobar_columnas(jugador):
        return True
    
def error(mensaje):
    print(mensaje)
    exit()

def main():
    print('Bienvenido al tres en ralla, donde puedes elegir el tamaño del tablero.\n ')

    try: 
        tamaño_tablero = int(input('Introduce el tamaño del tablero: '))
    except:
        error('No ha introducido un número entero, porfavor reinicie el juego para volver a intentarlo.')

    ficha_jugador_1 = input('El jugador 1 quiere jugar con ficha "X" o "O" ?: ')

    if ficha_jugador_1 == "X":
        fichas = ['X','O']
        print('Por lo tanto el jugador 2, la maquina será la ficha "O"')

    elif ficha_jugador_1 == "O":
        fichas = ['O','X']
        print('Por lo tanto el jugador 2, la maquina será la ficha "X"')

    else: 
        error('No ha introducido una ficha valida, porfavor reinicie el juego para volver a intentarlo. ')
    
    # Se crean los jugadores con sus respectivas fichas. 

    jugadores = []
    for i in range(1, 3): jugadores.append(Jugador(i))
    for i in range(len(jugadores)): jugadores[i].añadir_ficha(fichas[i])

    # Se crea el tablero. 
    
    tablero = Tablero(tamaño_tablero)

    print("El tablero creado ha sido el siguiente: \n")
    tablero.imprimir()

    hay_ganador = False
    # Empieza el juego. 

    while hay_ganador == False:
        for i in range(len(jugadores)):
            print(f'Turno del jugador {jugadores[i].numero}: ')
            if i == 0: 
                try:
                    fila = int(input(f'Introduce el número de la fila, del 0 al {tamaño_tablero - 1}: '))
                    columna = int(input(f'Introduce el número de la columna, del 0 al {tamaño_tablero - 1}: '))
                    print()    
                except:
                    error('No ha introducido un número entero, porfavor reinicie el juego para volver a intentarlo.')
                movimiento_jugador(fila,columna,jugadores[i],tablero)
                
                if comprobación_ganador(tablero, jugadores[i]):
                    hay_ganador = True
            else:
                movimiento_jugador(fila,columna,jugadores[i],tablero)
                if comprobación_ganador(tablero, jugadores[i]):
                    hay_ganador = True
            tablero.imprimir()

    else:
        for jugador in jugadores:
            if jugador.ganador == True:
                print(f'El jugador {jugador.numero} ha ganado, felicidades. ')
                print(f'El tablero, ha quedado finalmente de la siguiente manera: ')
                tablero.imprimir()
                
main()