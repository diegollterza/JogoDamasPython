import pygame
from Casa import Casa


class Tabuleiro:
    rows = 8
    columns = 8

    def __init__(self):
        self.grid = [[Casa() for j in range(self.rows)] for i in range(self.columns)]
    def getRows(self):
        return self.rows

    def getColumns(self):
        return self.columns

    @property
    def getGrid(self):
        return self.grid



