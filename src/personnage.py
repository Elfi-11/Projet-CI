import random

class Personnage:
    def __init__(self):
        self.__hp = 10

    def get_hp(self):
        return self.__hp
    
    def recevoir_attaque(self, attaquant):
        if random.random() < 0.5:
            self.__hp -= 2  # Inflige 2 dégâts
        else:
            self.__hp -= 1  # Inflige 1 dégât

    def estMort(self):
        return self.__hp == 0