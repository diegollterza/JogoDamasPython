from Peca import Peca

class Casa:
    peca = Peca()
    largura = 80
    altura = 80
    ocupado = False

    def setPeca(self,peca):
        self.peca.set(peca)

    def getPeca(self):
        return self.peca

    def getAltura(self):
        return self.altura

    def getLargura(self):
        return self.largura

    def setOcupado(self, ocupado):
        self.ocupado = ocupado

    def isOcupado(self):
        return self.ocupado


