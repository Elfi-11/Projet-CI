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


    def test_recevoir_attaque(self):
        guerrier = Guerrier()
        mage = Mage()
        archer = Archer()

        guerrier.attaquer(mage)  
        self.assertGreater(mage.get_hp(), 0)
        guerrier.attaquer(archer) 
        self.assertGreater(archer.get_hp(), 0)
        mage.attaquer(guerrier)
        self.assertGreater(guerrier.get_hp(), 0)
        mage.attaquer(archer) 
        self.assertGreater(archer.get_hp(), 0)
        archer.attaquer(guerrier) 
        self.assertGreater(guerrier.get_hp(), 0)
        archer.attaquer(mage) 
        self.assertGreater(mage.get_hp(), 0)

if __name__ == '__main__':
    unittest.main()