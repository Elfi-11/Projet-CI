import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import patch
from personnage import Personnage

class TestRpg(unittest.TestCase):
    def test_hp_initiaux(self):
        perso = Personnage()
        self.assertEqual(perso.get_hp(),10)

    def test_recevoir_attaque(self):
        perso = Personnage()
        perso.recevoir_attaque(None)
        self.assertGreaterEqual(perso.get_hp(),0)

    def test_attaquer_personnage(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_attaque(attaquant)
        self.assertIn(defenseur.get_hp(), [9,8])

    def test_mort_et_vivante(self):
        perso = Personnage ()
        self.assertFalse(perso.estMort())
        while not perso.estMort():
            perso.recevoir_attaque(None)
        self.assertTrue(perso.estMort())
    
    def test_potion(self):
        perso = Personnage()
        initial_hp = perso.get_hp()
        perso.recevoir_attaque(None)
        self.assertIn(initial_hp - perso.get_hp(), [1, 2])

    def test_recevoir_2_degats_avec_1_hp(self):
        perso = Personnage ()
        for _ in range(9):
            with patch('random.random', return_value=0.6):
                perso.recevoir_attaque(None)
        self.assertEqual(perso.get_hp(), 1)
        with patch('random.random', return_value=0.4):  
            perso.recevoir_attaque(None)
        self.assertEqual(perso.get_hp(), 0)
        self.assertTrue(perso.estMort())

       
if __name__ == '__main__':
    unittest.main()
