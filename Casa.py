from Peca import Peca

class Casa:
    peca = Peca()
    largura = 83
    altura = 83
    Cor = None
    WHITE = 1
    BLACK = 2
    NONE = 0
    valor = 0

    def setPeca(self,peca):
        self.peca = peca

    def getPeca(self):
        return self.peca

    def getAltura(self):
        return self.altura

    def getLargura(self):
        return self.largura

    def setCor(self,cor):
        self.Cor = cor

    def getCor(self):
        return self.Cor

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor
