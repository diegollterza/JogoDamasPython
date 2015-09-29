import Peca

class Casa:
    peca = Peca
    largura = 60
    altura = 60
    ocupado = False

    def setPeca(self,peca):
        self.peca.set(peca)

    def getPeca(self):
        return self.peca.get()

    def getAltura(self):
        return self.altura.get()

    def getLargura(self):
        return self.largura.get()

    def setOcupado(self, ocupado):
        self.ocupado = ocupado

    def isOcupado(self):
        return self.ocupado


