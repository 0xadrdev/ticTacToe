from pickletools import TAKEN_FROM_ARGUMENT1


class Jugador:
    def __init__(self, ficha):
        self.ficha = ficha 



class Tablero:
    def __init__(self, tamaño):
        self.matriz = ['-'] * tamaño
        for i in range(len(self.matriz)):
            self.matriz[i] = ['-'] * tamaño
            print

    def imprimir_tablero(self): 
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                print(self.matriz[i][j], end=" | ")
            print()
            

        pass
