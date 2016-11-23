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

    def __init__(self, valor = 0):
        self.valor = valor
        
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
    
    def getValorInverso(self):
        _valor = 0
        if self.valor == self.WHITE:
            _valor = self.BLACK
        elif self.valor == self.BLACK:
            _valor = self.WHITE 
        return _valor
