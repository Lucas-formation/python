from unittest import TestCase
import unittest
from main import trier 
import pytest
# Lancer classique : python -m unittest -v
# Lancer avec pytest : python -m pytest test_trier.py -v   
# Préférez utiliser pytest
#Pour lancer le covrage : coverage run -m unittest nomfichier.py
# coverage html

class testTrier(TestCase):
    def test_saisie(self):
        pass

    def test_trie_liste_en_desordre(self):
        # Vérifier que [8,9,10,1,2,3] rend [1,2,3,8,9,10]
        self.assertEqual(trier.trie_croissant([8,9,10,1,2,3]), [1,2,3,8,9,10])
        # Vérifier que [8,9,10,2,2,3] ne rend pas [9,2,3,8,2,10]
        self.assertNotEqual(trier.trie_croissant([8,9,10,2,2,3]), [9,2,3,8,2,10])

    def test_trie_liste_en_ordre(self):
        # Vérifier que [1,2,3,8,9,10] rend [1,2,3,8,9,10]
        self.assertEqual(trier.trie_croissant([1,2,3,8,9,10]), [1,2,3,8,9,10])
        # Vérifier que [1,2,3,8,9,10] ne rend pas [8,9,10,1,2,3]
        self.assertNotEqual(trier.trie_croissant([1,2,3,8,9,10]), [8,9,10,1,2,3])

    def test_trie_vide(self):
        # Vérifier que si nous n'envoyons rien, rien n'est retourné.
        self.assertEqual(trier.trie_croissant([]), [])
        # Vérifier que si nous n'envoyons rien, [1] n'est pas le résultat.
        self.assertNotEqual(trier.trie_croissant([]), [1])
