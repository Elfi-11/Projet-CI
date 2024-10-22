import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
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
       
if __name__ == '__main__':
    unittest.main()
