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
    
    def test_attaquer_enleve_2_hp(self):
        attaquant = Personnage()
        defenseur = Personnage()
        defenseur.recevoir_attaque(attaquant)
        defenseur.recevoir_attaque(attaquant)
        self.assertEqual(8, defenseur.get_hp())
    
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

    def test_attaquer_plus_de_10_fois(self):
        attaquant = Personnage()
        defenseur = Personnage()

        for i in range(0, 12):  # On attaque 12 fois
            defenseur.recevoir_attaque(attaquant)

    # Vérifier que les HP sont bien à -2 après 12 attaques
        self.assertEqual(-2, defenseur.get_hp())

    # Vérifier que le personnage est considéré comme mort (il a 0 HP ou moins)
        self.assertTrue(defenseur.get_hp() <= 0) 


if __name__ == '__main__':
    unittest.main()
