from unittest import TestCase
import unittest
import pytest
import mockito 
# Lancer classique : python -m unittest -v
# Lancer avec pytest : python -m pytest test_trier.py -v   
# Préférez utiliser pytest
#Pour lancer le covrage : python -m coverage run -m unittest nomfichier.py
# python -m coverage html
from interface import interface
from unittest.mock import MagicMock
import os
import tempfile
import mock

class testInterface(TestCase):
    def test_bdd_id(self):
        inter = interface()
        # Vérifier que le mail lucas.gaio@gmail.com retourne "True"
        self.assertEqual(inter.bdd_id("lucas.gaio@gmail.com"), True)
        # Vérifier que le mail lucas.False@gmail.com retourne pas "True"
        self.assertNotEqual(inter.bdd_id("lucas.polart@gmail.com"), True)

    def test_bdd_mdp(self):
        inter = interface()
        # Vérifier que le mail lucas.gaio@gmail.com retourne "True"
        self.assertEqual(inter.bdd_mdp("lucas.gaio@gmail.com", "mdp123"), True)
        # Vérifier que le mail lucas.False@gmail.com retourne pas "True"
        self.assertNotEqual(inter.bdd_mdp("lucas.gaio@gmail.com", "mdp1234"), True)

    def test_bdd(self):
        inter = interface()
        # Vérifier que le mail lucas.gaio@gmail.com retourne toutes les données en rapport.
        self.assertEqual(inter.bdd("lucas.gaio@gmail.com"), {'nom' : "", 'prenom' : "", 'mail' : "", 'naissance' : ""})

    """tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")

    def setUp(self):
        with open("data.json", "wb") as f:
            f.write("Delete me!")
        
    def test_rm(self):
        # remove the file
        interface.suppression_data()
        # test that it was actually removed
        self.assertFalse(os.path.isfile("data.json"), "Failed to remove the file.")"""

class RmTestCase(unittest.TestCase):
    
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        interface.suppression_data("data.json")
        mock_os.remove.assert_called_with("data.json")