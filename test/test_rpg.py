
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

     def test_recevoir_2_degats_avec_1_hp(self):
        
if __name__ == '__main__':
    unittest.main()