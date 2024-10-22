import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from personnage import Personnage

class TestRpg(unittest.TestCase):
    def test_hp_initiaux(self):
        test à définir
       

if __name__ == '__main__':
    unittest.main()
