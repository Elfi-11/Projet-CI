import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from personnage import Personnage
import unittest

class TestRpg(unittest.TestCase):
    def test_10_hp_initiaux(self):
        personnage = Personnage()
        self.assertEqual(10, personnage.get_hp())

    def test_attaquer_enleve_1_hp(self): 
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(9, defenseur.get_hp())

    
    def test_attaquer_10_fois_tue(self):
        attaquant = Personnage()
        defenseur = Personnage()

        for i in range(0,10):
            defenseur.recevoir_attaque(attaquant)
        
        self.assertTrue(defenseur.estMort())
    
    def test_attaquer_9_fois_ne_tue_pas(self):
        attaquant = Personnage()
        defenseur = Personnage()

        for i in range(0,9):  
            defenseur.recevoir_attaque(attaquant)
        
        self.assertFalse(defenseur.estMort())

if __name__ == '__main__':
    unittest.main()
