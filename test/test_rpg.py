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

if __name__ == '__main__':
    unittest.main()