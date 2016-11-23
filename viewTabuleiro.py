__author__ = 'Briane'

from Tabuleiro import Tabuleiro
from Casa import Casa
from Peca import Peca

import pygame

class viewTabuleiro:
    tabuleiro = Tabuleiro()
    # Define algumas cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    first_click = True
    white_turn = True
    last_row = -1
    last_column = -1
    last_cor = None

    #Definindo imagens
    QuadroBranco = pygame.image.load("./data/QuadroBranco.jpg")
    QuadroPreto = pygame.image.load("./data/QuadroPreto.jpg")
    PecaPreta = pygame.image.load("./data/PecaPreta.png")
    PecaBranca = pygame.image.load("./data/PecaBranca.png")

    def jogar(self):
        # Inicializa pygames
        pygame.init()

        # Largura e altura da tela
        WINDOW_SIZE = [8*83, 8*83]
        screen = pygame.display.set_mode(WINDOW_SIZE)
        screen.fill(self.BLACK)
        # Titulo
        pygame.display.set_caption("Don't be a drag, just be a queen")

        # Loop ate o usuario fechar a aplicacao
        done = False

        clock = pygame.time.Clock()

        #iniciando o gameLoop e capturando os clicks do mouse
        while not done:
            for event in pygame.event.get():  # Usuario faz algo
                if event.type == pygame.QUIT:  # Se clicar em fechar
                    done = True  # marca como terminado e acaba o loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Usuario clica no mouse. Pega posicao
                    pos = pygame.mouse.get_pos()
                    #Converte coordenadas x,y para coordenadas da tela
                    column = pos[0] // (Casa().getLargura())
                    row = pos[1] // (Casa().getAltura())
                    print("Click ", pos, "Grid coordinates: ", row, column)
			        
                    #handler do mouse_click para movimentar as pecas / implementar as regras de jogo
                    #movimento das pecas brancas
                    if self.white_turn:
                        #primeiro click do mouse, seleciona a peca a ser movimentada
                        if self.tabuleiro.getGrid[row][column].getValor() == Casa().WHITE and self.first_click:
                            self.tabuleiro.hasToEat(self.white_turn)
                            self.tabuleiro.getGrid[row][column].setCor(self.GREEN)
                            self.last_row = row
                            self.last_column = column
                            self.first_click = False
                    

                        elif not self.first_click:
                            if self.tabuleiro.hasToEat(self.white_turn):
                                if row == self.last_row - 2 and self.tabuleiro.getGrid[row][column].getValor() == Casa().NONE:

                                    if column == self.last_column - 2 and self.tabuleiro.getGrid[self.last_row-1][self.last_column-1].getValor() == Casa().BLACK:
                                        self.tabuleiro.getGrid[row][column].setValor(Casa().WHITE)
                                        self.tabuleiro.getGrid[self.last_row -1][self.last_column - 1].setValor(Casa().NONE)
                                        self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                        if not self.tabuleiro.canContinueEating:
                                            self.white_turn = False

                                    if column == self.last_column + 2 and self.tabuleiro.getGrid[self.last_row-1][self.last_column+1].getValor() == Casa().BLACK:
                                        self.tabuleiro.getGrid[row][column].setValor(Casa().WHITE)
                                        self.tabuleiro.getGrid[self.last_row - 1][self.last_column + 1].setValor(Casa().NONE)
                                        self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                        if not self.tabuleiro.canContinueEating:
                                            self.white_turn = False
                            else:
                                if row == self.last_row - 1 and  self.tabuleiro.getGrid[row][column].getValor() == Casa().NONE:
                                    if column == self.last_column - 1 or column == self.last_column + 1:
                                        self.tabuleiro.getGrid[row][column].setValor(Casa().WHITE)
                                        self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                        self.white_turn = False
                            self.first_click = True
                            self.tabuleiro.redraw() 
                    

                    #movimento das pecas pretas
                    else:
                        if self.tabuleiro.getGrid[row][column].getValor() == Casa().BLACK and self.first_click:
                            self.tabuleiro.hasToEat(self.white_turn)
                            self.tabuleiro.getGrid[row][column].setCor(self.GREEN)
                            self.last_row = row
                            self.last_column = column
                            self.first_click = False
                    

                        elif not self.first_click:
                            if self.tabuleiro.hasToEat(self.white_turn):
                                if row == self.last_row + 2 and self.tabuleiro.getGrid[row][column].getValor() == Casa().NONE:

                                    if column == self.last_column - 2 and self.tabuleiro.getGrid[self.last_row+1][self.last_column-1].getValor() == Casa().WHITE:
                                        self.tabuleiro.getGrid[row][column].setValor(Casa().BLACK)
                                        self.tabuleiro.getGrid[self.last_row + 1][self.last_column - 1].setValor(Casa().NONE)
                                        self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                        self.white_turn = True

                                    if column == self.last_column + 2 and self.tabuleiro.getGrid[self.last_row+1][self.last_column+1].getValor() == Casa().WHITE:
                                        self.tabuleiro.getGrid[row][column].setValor(Casa().BLACK)
                                        self.tabuleiro.getGrid[self.last_row + 1][self.last_column + 1].setValor(Casa().NONE)
                                        self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                        self.white_turn = True
                            else:
                                if row == self.last_row + 1 and  self.tabuleiro.getGrid[row][column].getValor() == Casa().NONE:
                                    if column == self.last_column - 1 or column == self.last_column + 1:
                                        self.tabuleiro.getGrid[row][column].setValor(Casa().BLACK)
                                        self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                        self.white_turn = True
                            self.first_click = True
                            self.tabuleiro.redraw()          

            # Redraw
            for row in range(self.tabuleiro.getRows()):
                for column in range(self.tabuleiro.getColumns()):
                    pygame.draw.rect(screen,
                                         self.tabuleiro.getGrid[row][column].getCor(),
                                         [Casa().getLargura() * column,
                                          Casa().getAltura() * row,
                                          Casa().getLargura(),
                                          Casa().getAltura()])
                    if self.tabuleiro.getGrid[row][column].getValor() == Casa().BLACK:
    					screen.blit(self.PecaPreta, (Casa().getLargura() * column, Casa().getAltura() * row))
                    if self.tabuleiro.getGrid[row][column].getValor() == Casa().WHITE:
    					screen.blit(self.PecaBranca, (Casa().getLargura() * column, Casa().getAltura() * row))

            # Limite de 60 frames por segundo
            clock.tick(60)

            # update na tela com o que desenhamos
            pygame.display.flip()

        #finaliza o py games
        pygame.quit()

if __name__ == "__main__":
    main = viewTabuleiro()
    main.jogar()
