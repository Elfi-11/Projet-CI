import random

class Personnage:
    def __init__(self):
        self.__hp = 10

    def get_hp(self):
        return self.__hp
    
    def recevoir_attaque(self, attaquant):
        if random.random() < 0.5:
            self.__hp -= 2 
        else:
            self.__hp -= 1 

        if self.__hp < 0:
            self.__hp = 0 

    def estMort(self):
        return self.__hp == 0