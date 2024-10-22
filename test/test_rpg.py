import random  # Importation de la bibliothèque random pour générer des valeurs aléatoires

class Personnage:
    def __init__(self, hp, degats):
        self.__hp = hp
        self.__degats = degats

    def get_hp(self):
        """Retourne les points de vie actuels du personnage."""
        return self.__hp
    
    def get_degats(self):
        return self.__degats  # Getter pour les dégâts
    
    def recevoir_attaque(self, degats):
        """Méthode pour gérer les dégâts subis par le personnage lors d'une attaque."""
        self.__hp -= degats
        if self.__hp < 0:
            self.__hp = 0  

    def estMort(self):
        """Vérifie si le personnage est mort."""
        return self.__hp == 0 

class Guerrier(Personnage):
    def __init__(self):
        super().__init__(hp=15, degats=[1, 3])
    
    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1]) 
        cible.recevoir_attaque(degats_infliges) 

class Mage(Personnage):
    def __init__(self):
        super().__init__(hp=8, degats=[2, 4])
    
    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1])  
        cible.recevoir_attaque(degats_infliges) 

class Archer(Personnage):
    def __init__(self):
        super().__init__(hp=12, degats=[1, 2])
    
    def attaquer(self, cible):
        degats_infliges = random.randint(self.get_degats()[0], self.get_degats()[1])  
        cible.recevoir_attaque(degats_infliges) 

# Importation des modules nécessaires pour les tests
import sys
import os

# Ajout du chemin du répertoire src au chemin système pour pouvoir importer la classe Personnage
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest  # Importation de la bibliothèque unittest pour les tests unitaires
from unittest.mock import patch  # Importation de patch pour simuler des comportements
from personnage import Personnage, Guerrier, Mage, Archer  # Importation de la classe Personnage

class TestRpg(unittest.TestCase):
    def test_hp_initiaux(self):
        guerrier = Guerrier()
        mage = Mage()  
        archer = Archer()
        self.assertEqual(guerrier.get_hp(), 15)
        self.assertEqual(mage.get_hp(), 8)
        self.assertEqual(archer.get_hp(), 12)

    @patch('random.randint')
    def test_recevoir_attaque(self, mock_randint):
        mock_randint.side_effect = [1, 1, 2, 2, 3, 3] 

        guerrier = Guerrier()
        mage = Mage()
        archer = Archer()

        # Attaques
        guerrier.attaquer(mage)  
        guerrier.attaquer(archer)
        mage.attaquer(guerrier)
        mage.attaquer(archer)   
        archer.attaquer(mage)     
        archer.attaquer(guerrier)  

        self.assertGreater(mage.get_hp(), 0, "Le mage devrait avoir des points de vie restants.")
        self.assertGreater(guerrier.get_hp(), 0, "Le guerrier devrait avoir des points de vie restants.")
        self.assertGreater(archer.get_hp(), 0, "L'archer devrait avoir des points de vie restants.")

    def test_mort_ou_vivante(self):
        classes_de_personnage = [Guerrier, Mage, Archer]
        
        for Classe in classes_de_personnage:
            perso = Classe()  
            self.assertFalse(perso.estMort()) 
            while not perso.estMort():
                degats = random.randint(perso.get_degats()[0], perso.get_degats()[1])
                perso.recevoir_attaque(degats) 
            self.assertTrue(perso.estMort())   

if __name__ == '__main__':
    unittest.main()