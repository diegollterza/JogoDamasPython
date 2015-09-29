__author__ = 'Briane'

class Peca:
    Cor = None
    Dama = False #promove a peca para dama

    def setCor(self,cor):
        self.Cor.set(cor)

    def getCor(self):
        return self.Cor.get()

    def promover(self):
        self.Dama.set(True)




