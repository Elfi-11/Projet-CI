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
        self.assertEqual(perso.get_hp(),9)

    def test_attaquer_personnage(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(defenseur.get_hp(), 9)

    def test_pas_mort_avec_plus_de_0_hp(self):
        perso = Personnage()
        perso.recevoir_attaque(None)
        self.assertFalse(perso.estMort())
       
if __name__ == '__main__':
    unittest.main()
