import pygame
from Casa import Casa


class Tabuleiro:
    rows = 8
    columns = 8
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)


    def __init__(self):
        self.grid = [[Casa() for j in range(self.rows)] for i in range(self.columns)]
        for row in range(self.rows):
            for column in range(self.columns):
                if (row + column) % 2 == 0:
                    self.grid[row][column].setCor(self.WHITE)
                    if row < 3:
                        self.grid[row][column].setValor(Casa().BLACK)
                    if row > 4:
                        self.grid[row][column].setValor(Casa().WHITE)
                else:
                    self.grid[row][column].setCor(self.BLACK)

    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns

    @property
    def getGrid(self):
        return self.grid

    def hasToEat(self, white_turn):
        _flag = False
        for row in range(self.rows):
            for column in range(self.columns):
                if white_turn:
                    if row > 1 and column > 1 and self.grid[row][column].getValor() == Casa().WHITE and self.grid[row - 1][column - 1].getValor() == Casa().BLACK:
                        if self.grid[row-2][column - 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
                    if row > 1 and column < 6 and self.grid[row][column].getValor() == Casa().WHITE and self.grid[row - 1][column + 1].getValor() == Casa().BLACK:
                        if self.grid[row-2][column + 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
                else:
                    if row < 6 and column > 1 and self.grid[row][column].getValor() == Casa().BLACK and self.grid[row + 1][column - 1].getValor() == Casa().WHITE:
                        if self.grid[row+2][column - 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
                    if row < 6 and column < 6 and self.grid[row][column].getValor() == Casa().BLACK and self.grid[row + 1][column + 1].getValor() == Casa().WHITE:
                        if self.grid[row+2][column + 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
        return _flag



    def redraw(self):
        for row, column in range(self.rows), range(self.column):
            for column in range(self.columns):
                if (row + column) % 2 == 0:
                    self.grid[row][column].setCor(self.WHITE)
                else:
                    self.grid[row][column].setCor(self.BLACK)     
    


    def countPecas(self, white_turn):
        if white_turn:
            _casa = Casa().WHITE
        else:
            _casa = Casa().BLACK
        _count = 0
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[row][column].getValor() == _casa:
                    _count += 1
        return _count


    def canContinueEating(self, white_turn):
        _flag = False
        if white_turn:
            _casa = Casa(Casa().WHITE)
        else:
            _casa = Casa(Casa().BLACK)

        for row in range(self.rows):
            for column in range(self.columns):
                if white_turn:
                    if row > 1 and column > 1 and self.grid[row][column].getValor() == _casa.getValor() and self.grid[row - 1][column - 1].getValor() == _casa.getValorInverso():
                        if self.grid[row-2][column - 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
                    if row > 1 and column < 6 and self.grid[row][column].getValor() == _casa.getValor() and self.grid[row - 1][column + 1].getValor() == _casa.getValorInverso():
                        if self.grid[row-2][column + 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
                    if row < 6 and column > 1 and self.grid[row][column].getValor() == _casa.getValor() and self.grid[row + 1][column - 1].getValor() == _casa.getValorInverso():
                        if self.grid[row+2][column - 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
                    if row < 6 and column < 6 and self.grid[row][column].getValor() == _casa.getValor() and self.grid[row + 1][column + 1].getValor() == _casa.getValorInverso():
                        if self.grid[row+2][column + 2].getValor() == Casa().NONE:
                            self.grid[row][column].setCor(self.RED)
                            _flag = True
        return _flag







