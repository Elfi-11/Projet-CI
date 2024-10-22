import random  # Importation de la bibliothèque random pour générer des valeurs aléatoires

class Personnage:
    def __init__(self):
        # Initialisation des points de vie du personnage à 10
        self.__hp = 10

    def get_hp(self):
        """Retourne les points de vie actuels du personnage."""
        return self.__hp
    
    def recevoir_attaque(self, attaquant):
        """Méthode pour gérer les dégâts subis par le personnage lors d'une attaque.

        Args:
            attaquant: Le personnage qui attaque (non utilisé ici).
        """
        # Génère un nombre aléatoire entre 0 et 1
        # Si le nombre est inférieur à 0.5, inflige 2 dégâts
        # Sinon, inflige 1 dégât
        if random.random() < 0.5:
            self.__hp -= 2  # Inflige 2 dégâts
        else:
            self.__hp -= 1  # Inflige 1 dégât

        # Assure que les points de vie ne tombent pas en dessous de 0
        if self.__hp < 0:
            self.__hp = 0  # Réinitialise les HP à 0 si le personnage est mort

    def estMort(self):
        """Vérifie si le personnage est mort.

        Returns:
            bool: True si le personnage est mort, False sinon.
        """
        return self.__hp == 0  # Retourne True si les HP sont à 0
