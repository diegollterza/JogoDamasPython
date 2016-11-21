__author__ = 'Briane'

class Peca:
    Cor = None
    Dama = False #promove a peca para dama

    def setCor(self,cor):
        self.Cor = cor

    def getCor(self):
        return self.Cor

    def promover(self):
        self.Dama = True;

    def setOcupado(self):
        self.ocupado = True;
    



