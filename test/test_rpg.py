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
  


    def test_recevoir_attaque(self):
        """Test que le personnage a des HP >= 0 après avoir reçu une attaque."""
        perso = Personnage()  # Création d'une instance de Personnage
        perso.recevoir_attaque(None)  # Le personnage subit une attaque
        self.assertGreaterEqual(perso.get_hp(), 0)  # Vérifie que les HP ne sont pas négatifs

    def test_attaquer_personnage(self):
        """Test que les points de vie du défenseur diminuent correctement après une attaque."""
        attaquant = Personnage()  # Création d'un personnage attaquant
        defenseur = Personnage()  # Création d'un personnage défenseur
        defenseur.recevoir_attaque(attaquant)  # Le défenseur subit une attaque de l'attaquant
        self.assertIn(defenseur.get_hp(), [9, 8])  # Vérifie que les HP du défenseur sont soit 9 soit 8

    def test_mort_et_vivante(self):
        """Test que le personnage devient mort après avoir reçu suffisamment d'attaques."""
        perso = Personnage()  # Création d'une instance de Personnage
        self.assertFalse(perso.estMort())  # Vérifie que le personnage est vivant au départ

        # Boucle jusqu'à ce que le personnage soit mort
        while not perso.estMort():
            perso.recevoir_attaque(None)  # Le personnage subit des attaques
        self.assertTrue(perso.estMort())  # Vérifie que le personnage est maintenant mort
    
    def test_potion(self):
        """Test que le personnage reçoit soit 1 soit 2 dégâts après avoir été attaqué."""
        perso = Personnage()  # Création d'une instance de Personnage
        initial_hp = perso.get_hp()  # Stocke les HP initiaux
        perso.recevoir_attaque(None)  # Le personnage subit une attaque
        # Vérifie que la réduction de HP est soit 1 soit 2
        self.assertIn(initial_hp - perso.get_hp(), [1, 2])

    def test_recevoir_2_degats_avec_1_hp(self):
        """Test qu'un personnage avec 1 HP ne peut pas avoir de HP négatifs après avoir reçu 2 dégâts."""
        perso = Personnage()  # Création d'une instance de Personnage

        # Réduire les HP à 1 en infligeant uniquement 1 dégât
        for _ in range(9):
            with patch('random.random', return_value=0.6):  # Simule toujours 1 dégât
                perso.recevoir_attaque(None)

        # Vérifie que le personnage a 1 HP après 9 attaques
        self.assertEqual(perso.get_hp(), 1)

        # Simuler l'attaque qui inflige 2 dégâts
        with patch('random.random', return_value=0.4):  # Simule 2 dégâts
            perso.recevoir_attaque(None)

        # Vérifie que les HP sont à 0 après l'attaque
        self.assertEqual(perso.get_hp(), 0)  # Doit être mort maintenant
        self.assertTrue(perso.estMort())  # Vérifie que le personnage est bien mort

# Exécution des tests si ce fichier est exécuté directement
if __name__ == '__main__':
    unittest.main()