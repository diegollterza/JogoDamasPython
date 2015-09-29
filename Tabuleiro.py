import pygame
import Casa


class Tabuleiro:
    grid = []
    rows = 8
    columns = 8


    def getRows(self):
        return self.rows.get()

    def getColumns(self):
        return self.columns.get()

    @property
    def getGrid(self):
        #Criando o Array
        for row in range(self.rows):
            self.grid.append([])
            for column in range(self.columns):
                self.grid[row].append(Casa) #Guh, aqui que eu me compliquei, tenho duvidas sobre como fazer esse array receber um obj da classe Casa e ser de duas dimensoes
        return self.grid.get()



