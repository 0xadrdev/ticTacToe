from pickletools import TAKEN_FROM_ARGUMENT1

class color:
    green = "\x1b[1;32m"
    red = "\x1b[1;31m" 
    yellow = "\x1b[1;33m"
    black = "\x1b[1;30m" 
    end = "\x1b[0m" 

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
    
    # def imprimir(self): 
    #     print()
    #     for i in range(len(self.matriz)): print(f' {i}  ', end="")
    #     print()
    #     print('---+' * len(self.matriz))
    #     for i in range(len(self.matriz)):
    #         for j in range(len(self.matriz[0])):
    #             print(f' {self.matriz[i][j]} ', end="|")
    #         print(f' {i}')
    #         print('---+' * len(self.matriz))
    #     print()

    def imprimir(self): 
        print()
        for i in range(len(self.matriz)): print(f'{color.green} {i}  {color.end}', end="")
        print()
        print('---+' * len(self.matriz))
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if self.matriz[i][j] == 'X':
                    print(f' {color.red}{self.matriz[i][j]} {color.end}', end="|")
                elif self.matriz[i][j] == 'O':
                    print(f' {color.yellow}{self.matriz[i][j]} {color.end}', end="|")
                else:
                    print(f' {color.black}{self.matriz[i][j]} {color.end}', end="|")

            print(f'{color.green} {i}{color.end}')
            print('---+' * len(self.matriz))
        print()

    def movimiento_correcto(self, x, y):
        if x >= 0 and x < len(self.matriz) and y >= 0 and y < len(self.matriz[0]):
            if self.matriz[x][y] == 'X' or self.matriz[x][y] == 'O':
                return False
            return True
        return False

    def movimiento(self, x, y, jugador):
        self.matriz[x][y] = jugador.ficha

    def comprobar_diagonal_principal(self, jugador):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[0])):
                if i == j and self.matriz[i][j] != jugador.ficha:
                    return False
        return True 

    def comprobar_diagonal_secundaria(self, jugador):
        contador = len(self.matriz) - 1
        for i in range(len(self.matriz[0])):
            if self.matriz[i][contador] != jugador.ficha:
                return False
            contador -= 1
        return True

    def comprobar_filas(self, jugador):
        filas = []
        for i in range(len(self.matriz)):
            estado_fila = True 
            for j in range(len(self.matriz)):
                if self.matriz[i][j] != jugador.ficha:
                    estado_fila = False
                    break
            filas.append(estado_fila)
        
        if True in filas:
            return True 
        return False

    def comprobar_columnas(self,jugador):
        columnas = [] 

        for j in range(len(self.matriz[0])):
            estado_columna = True
            for i in range(len(self.matriz)):
                if self.matriz[i][j] != jugador.ficha:
                    estado_columna = False 
                    break 
            columnas.append(estado_columna)
                
        if True in columnas:
            return True
        return False
