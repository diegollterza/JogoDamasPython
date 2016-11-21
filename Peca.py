__author__ = 'Briane'

class Peca:
    WHITE = 1
    BLACK = 2
    NONE = 0
    Dama = False #promove a peca para dama
    valor = 0

    def setCor(self,cor):
        self.Cor = cor

    def getValor(self):
        return self.valor

    def promover(self):
        self.Dama = True;

    def setValor(self, valor):
        self.valor = valor
