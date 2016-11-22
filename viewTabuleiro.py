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
    white_turn = True;

    #Definindo imagens
    QuadroBranco = pygame.image.load("./data/QuadroBranco.jpg")
    QuadroPreto = pygame.image.load("./data/QuadroPreto.jpg")
    PecaPreta = pygame.image.load("./data/PecaPreta.png")
    PecaBranca = pygame.image.load("./data/PecaBranca.png")

    def jogar(self):
        # Inicializa pygames
        pygame.init()

        # Largura e altura da tela
        WINDOW_SIZE = [640, 640]
        screen = pygame.display.set_mode(WINDOW_SIZE)
		
        # Titulo
        pygame.display.set_caption("Don't be a drag, just be a queen")

        # Loop ate o usuario fechar a aplicacao
        done = False

        clock = pygame.time.Clock()


        for row in range(self.tabuleiro.getRows()):
            for column in range(self.tabuleiro.getColumns()):
                if (row + column) % 2 == 0:
                    self.tabuleiro.getGrid[row][column].setCor(self.WHITE)
                    if row < 3:
                        self.tabuleiro.getGrid[row][column].setValor(Casa().BLACK)
                    if row > 4:
                        self.tabuleiro.getGrid[row][column].setValor(Casa().WHITE)
                else:
                    self.tabuleiro.getGrid[row][column].setCor(self.BLACK)


        # -------- Recebe os movimentos do usuario -----------
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
			
                    if self.white_turn:
                        if self.white_turn and self.tabuleiro.getGrid[row][column].getValor() == Casa().WHITE and self.first_click:
                            self.last_cor = self.tabuleiro.getGrid[row][column].getCor()
                            self.tabuleiro.getGrid[row][column].setCor(self.GREEN)
                            self.last_row = row
                            self.last_column = column
                            self.first_click = False
                        elif not self.first_click:
                            if row == self.last_row - 1 and  self.tabuleiro.getGrid[row][column].getValor() == Casa().NONE:
                                if column == self.last_column - 1 or column == self.last_column + 1:
                                    self.tabuleiro.getGrid[row][column].setValor(Casa().WHITE)
                                    self.tabuleiro.getGrid[self.last_row][self.last_column].setValor(Casa().NONE)
                                    self.white_turn = False
                            self.first_click = True
                            self.tabuleiro.getGrid[self.last_row][self.last_column].setCor(self.last_cor)
                        

                            
            # background
            screen.fill(self.BLACK)


            # Desenha os quadrinhos
            for row in range(self.tabuleiro.getRows()):
                for column in range(self.tabuleiro.getColumns()):
                    pygame.draw.rect(screen,
                                         self.tabuleiro.getGrid[row][column].getCor(),
                                         [Casa().getLargura() * column,
                                          Casa().getAltura() * row,
                                          Casa().getLargura(),
                                          Casa().getAltura()])

                    #Preenche com pecas os quadros

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
