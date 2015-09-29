__author__ = 'Briane'
import Tabuleiro
import Casa
import Peca

import pygame

class viewTabuleiro:
    tabuleiro = Tabuleiro
    # Define algumas cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    #Definindo imagens
    QuadroBranco = pygame.image.load("./data/QuadroBranco.jpg")
    QuadroPreto = pygame.image.load("./data/QuadroPreto.jpg")
    PecaPreta = pygame.image.load("./data/PecaPreta.png")
    PecaBranca = pygame.image.load("./data/PecaBranca.png")

    def jogar(self):
        # Inicializa pygames
        pygame.init()

        # Largura e altura da tela
        WINDOW_SIZE = [725, 725]
        screen = pygame.display.set_mode(WINDOW_SIZE)

        # Titulo
        pygame.display.set_caption("Don't be a drag, just be a queen")

        # Loop ate o usuario fechar a aplicacao
        done = False

        # gerencia os cliques do mouse
        clock = pygame.time.Clock()
        # -------- Recebe os movimentos do usuario -----------
        while not done:
            for event in pygame.event.get():  # Usuario faz algo
                if event.type == pygame.QUIT:  # Se clicar em fechar
                    done = True  # marca como terminado e acaba o loop
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Usuario clica no mouse. Pega posicao
                    pos = pygame.mouse.get_pos()
                    #Converte coordenadas x,y para coordenadas da tela
                    column = pos[0] // (Casa.getLargura())
                    row = pos[1] // (Casa.getAltura())
                    print("Click ", pos, "Grid coordinates: ", row, column)

            # background
            screen.fill(self.BLACK)

            print(self.tabuleiro.getRows())

            # Desenha os quadrinhos
            for row in range(self.tabuleiro.getRows()):
                for column in range(Tabuleiro.getColumns()):
                    #Seta a cor das pecas
                    if (row + column) % 2 == 0:
                        self.tabuleiro.Tabuleiro.getGrid()[row][column].Casa.getPeca().setCor(self.WHITE)
                    else:
                        self.tabuleiro.Tabuleiro.getGrid()[row][column].Casa.getPeca().setCor(self.BLACK)
                    #desenha as pecas
                    pygame.draw.rect(screen,
                                         self.tabuleiro.Tabuleiro.getGrid()[row][column].Casa.getPeca().getCor(),
                                         [Casa.getLargura() * column,
                                          Casa.getAltura() * row,
                                          Casa.getLargura(),
                                          Casa.getAltura()])

                    #Preenche com pecas os quadros
                    if self.tabuleiro.getGrid()[row][column].Casa.getPeca().getCor() == self.WHITE and (row < 3):
                        #cada quadro tem 90px, entao pegamos a coordenada (x,y) e multiplicamos pelo valor do lado do quadrado
                        # para obtermos a posicao que a peca deve ficar
                        screen.blit(self.PecaPreta, (Casa.getLargura() * column+3, Casa.getAltura() * row+3))
                        #Esse +3 eh apenas pra peca nao ficar colada com o canto do quadrado
                        #serve de margem
                        #marca a casa como ocupada
                        self.tabuleiro.getGrid()[row][column].Casa.getPeca().setOcupado()

                    #Preenche com pecas os quadros
                    if self.tabuleiro.getGrid()[row][column].Casa.getPeca().getCor() == self.WHITE and (row > 4):
                        #cada quadro tem 90px, entao pegamos a coordenada (x,y) e multiplicamos pelo valor do lado do quadrado
                        # para obtermos a posicao que a peca deve ficar
                        screen.blit(self.PecaBranca, (Casa.getLargura() * column+3, Casa.getAltura() * row+3))
                        #Esse +3 eh apenas pra peca nao ficar colada com o canto do quadrado
                        #serve de margem
                        #marca a casa como ocupada
                        self.tabuleiro.getGrid()[row][column].Casa.getPeca().setOcupado()

            # Limite de 60 frames por segundo
            clock.tick(60)

            # update na tela com o que desenhamos
            pygame.display.flip()

        #finaliza o py games
        pygame.quit()

if __name__ == "__main__":
    main = viewTabuleiro()
    main.jogar()