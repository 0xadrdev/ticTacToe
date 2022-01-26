from pickletools import TAKEN_FROM_ARGUMENT1


class Jugador:
    def __init__(self, numero):
        self.numero = numero
        self.ganador = False

    def añadir_ficha(self,ficha):
        self.ficha = ficha

    def ficha(self):
        return self.ficha

class Tablero:
    def __init__(self, tamaño):
        self.matriz = []
        for i in range(tamaño):
            self.matriz.append(['-'] * tamaño)
        print(self.matriz)
    
    def imprimir(self): 
        print('---+' * len(self.matriz))
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                print(f' {self.matriz[i][j]} ', end="|")
            print()
            print('---+' * len(self.matriz))
        print()
    
    def consultar_matriz(self):
        return self.matriz

    def movimiento_correcto(self, x, y):
        if x >= 0 and x < len(self.matriz) and y >= 0 and y < len(self.matriz[0]):
            if self.matriz[x][y] == 'X' or self.matriz[x][y] == 'O':
                return False
            return True
        return False

    def movimiento(self, x, y, jugador):
        self.matriz[x][y] = jugador.ficha

    def comprobar_diagonal_principal(self, jugador):
        pass
    def comprobar_diagonal_secundaria(self, jugador):
        pass
    def comprobar_filas(self, jugador):
        pass
    def comprobar_columnas(self,jugador)
        pass
