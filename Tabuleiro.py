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
        for row in range(self.rows):
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


    def canContinueEating(self, row, column, white_turn):
        if white_turn:
            _casa = Casa(Casa().WHITE)
        else:    
            _casa = Casa(Casa().BLACK)
        if row > 1 and column > 1:
            if self.grid[row-1][column-1].getValor() == _casa.getValorInverso() and self.grid[row-2][column-2].getValor() == Casa().NONE:
                self.grid[row][column].setCor(self.RED)
                return True
        if row > 1 and column < 6:
            if self.grid[row-1][column+1].getValor() == _casa.getValorInverso() and self.grid[row-2][column+2].getValor() == Casa().NONE:
                self.grid[row][column].setCor(self.RED)
                return True
        if row < 6 and column > 1:
            if self.grid[row+1][column-1].getValor() == _casa.getValorInverso() and self.grid[row+2][column-2].getValor() == Casa().NONE:
                self.grid[row][column].setCor(self.RED)
                return True
        if row < 6 and column < 6:
            if self.grid[row+1][column+1].getValor() == _casa.getValorInverso() and self.grid[row+2][column+2].getValor() == Casa().NONE:
                self.grid[row][column].setCor(self.RED)
                return True


    def eating(self, last_row,last_column, row, column, white_turn):
        if white_turn:
            if self.grid[row][column].getValor() == Casa().NONE and row == last_row - 2 and last_row > 1:
                if column == last_column - 2 and last_column > 1:
                    if self.grid[last_row-1][last_column-1].getValor() == Casa.BLACK:
                        self.grid[row][column].setValor(Casa().WHITE)
                        self.grid[last_row][last_column].setValor(Casa().NONE)
                        self.grid[last_row - 1][last_column - 1].setValor(Casa().NONE)
                        return True
                if column == last_column + 2 and last_column < 6:
                    if self.grid[last_row-1][last_column+1].getValor() == Casa.BLACK:
                        self.grid[row][column].setValor(Casa().WHITE)
                        self.grid[last_row][last_column].setValor(Casa().NONE)
                        self.grid[last_row - 1][last_column + 1].setValor(Casa().NONE)
                        return True
        else:
             if self.grid[row][column].getValor() == Casa().NONE  and last_row < 6 and row == last_row + 2:
                if column == last_column - 2  and last_column > 1:
                    if self.grid[last_row+1][last_column-1].getValor() == Casa.WHITE:
                        self.grid[row][column].setValor(Casa().BLACK)
                        self.grid[last_row][last_column].setValor(Casa().NONE)
                        self.grid[last_row + 1][last_column - 1].setValor(Casa().NONE)
                        return True
                if column == last_column + 2  and last_column < 6:
                    if self.grid[last_row+1][last_column+1].getValor() == Casa.WHITE:
                        self.grid[row][column].setValor(Casa().BLACK)
                        self.grid[last_row][last_column].setValor(Casa().NONE)
                        self.grid[last_row + 1][last_column + 1].setValor(Casa().NONE)
                        return True
        return False

    def eatingAfterEating(self, last_row, last_column, row, column, white_turn):
        if white_turn:
            _casa = Casa(Casa().WHITE)
        else:    
            _casa = Casa(Casa().BLACK)
        if last_row > 1 and last_column > 1:
            if self.grid[last_row-1][last_column-1].getValor() == _casa.getValorInverso() and self.grid[last_row-2][last_column-2].getValor() == Casa().NONE:
                if column == last_column - 2 and row == last_row - 2:
                    self.grid[row][column].setValor(_casa.getValor())
                    self.grid[last_row][last_column].setValor(Casa().NONE)
                    self.grid[last_row - 1][last_column - 1].setValor(Casa().NONE)
                    return True
        if last_row > 1 and last_column < 6:
            if self.grid[last_row-1][last_column+1].getValor() == _casa.getValorInverso() and self.grid[last_row-2][last_column+2].getValor() == Casa().NONE:
                if column == last_column - 2 and row == last_row + 2:
                    self.grid[row][column].setValor(_casa.getValor())
                    self.grid[last_row][last_column].setValor(Casa().NONE)
                    self.grid[last_row - 1][last_column + 1].setValor(Casa().NONE)
                    return True
        if last_row < 6 and last_column > 1:
            if self.grid[last_row+1][last_column-1].getValor() == _casa.getValorInverso() and self.grid[last_row+2][last_column-2].getValor() == Casa().NONE:
                if column == last_column + 2 and row == last_row - 2:
                    self.grid[row][column].setValor(_casa.getValor())
                    self.grid[last_row][last_column].setValor(Casa().NONE)
                    self.grid[last_row + 1][last_column - 1].setValor(Casa().NONE)
                    return True
        if last_row < 6 and last_column < 6:
            if self.grid[last_row+1][last_column+1].getValor() == _casa.getValorInverso() and self.grid[last_row+2][last_column+2].getValor() == Casa().NONE:
                if column == last_column + 2 and row == last_row + 2:
                    self.grid[row][column].setValor(_casa.getValor())
                    self.grid[last_row][last_column].setValor(Casa().NONE)
                    self.grid[last_row + 1][last_column + 1].setValor(Casa().NONE)
                    return True
        return False

