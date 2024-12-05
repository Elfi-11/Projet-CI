import sys
import os
import random
import unittest  
from unittest.mock import patch  

# Ajouter le chemin du module src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Import des classes et fonctions
from personnage import Guerrier, Mage, Archer, choisir_classe  

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
        classes_de_personnage = [Guerrier, Mage, Archer]
        
        for Classe in classes_de_personnage:
            perso = Classe()
            initial_hp = perso.get_hp() 

            self.assertEqual(initial_hp, perso.get_hp())

            with patch('random.randint', return_value=2): 
                for _ in range(8):  
                    perso.recevoir_attaque(2)
            self.assertEqual(perso.get_hp(), max(0, initial_hp - 16)) 
            self.assertTrue(perso.estMort())

    @patch('builtins.input', side_effect=['guerrier'])
    def test_choix_classe_guerrier(self, mock_input):
        personnage = choisir_classe()
        self.assertIsInstance(personnage, Guerrier)  # Vérifie que l'instance est un Guerrier

    @patch('builtins.input', side_effect=['mage'])
    def test_choix_classe_mage(self, mock_input):
        personnage = choisir_classe()
        self.assertIsInstance(personnage, Mage)  # Vérifie que l'instance est un Mage

    @patch('builtins.input', side_effect=['archer'])
    def test_choix_classe_archer(self, mock_input):
        personnage = choisir_classe()
        self.assertIsInstance(personnage, Archer)

if __name__ == '__main__':
    unittest.main()
