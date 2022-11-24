from unittest import TestCase
import unittest
from main import calculatrice 
# import pytest
# Lancer classique : python -m unittest -v
# Lancer avec unittst : python -m pytest test_calculatrice.py -v   


class testCalculatrice(TestCase):
    def test_addition(self):
        # Vérifier que 1 + 1 == 2
        self.assertEqual(calculatrice.addition(1, 1), 2)
        # Vérifier que 1 + 2 != 2
        self.assertNotEqual(calculatrice.addition(1, 2), 2)

#    def test_addidtion_pas_egual(self):
#        # Vérifier que 1 + 2 != 2
#        self.assertNotEqual(calculatrice.addition(1, 2), 2)

    def test_multiplication(self):
        # Vérifier que 2 * 2 == 4
        self.assertEqual(calculatrice.multiplication(2, 2), 4)
        # Verifier que 2 * 2 != 5
        self.assertNotEqual(calculatrice.multiplication(2, 2), 5)

    def test_soustraction(self):
        # Vérifier que 2 - 2 == 0
        self.assertEqual(calculatrice.soustraction(2, 2), 0)
        # Verifier que 2 - 2 != 5
        self.assertNotEqual(calculatrice.soustraction(2, 2), 5)

    def test_division(self):
        # Vérifier que 2 / 2 == 1
        self.assertEqual(calculatrice.division(2, 2), 1)
        # Verifier que 2 / 2 != 5
        self.assertNotEqual(calculatrice.division(2, 2), 5)
        ## Vérifier qu'on ne peut pas diviser par zéro, avec une condition dans la méthode.
        #self.assertEqual(calculatrice.division(1, 0), "Impossible de diviser par 0.")
        # Vérifier l'erreur quand nous divisions par 0.
        with self.assertRaises(ArithmeticError):
            calculatrice.division(1, 0)

# Erreur avec Pytest
#def test_erreur():
#    with pytest.raises(ArithmeticError):
#        calculatrice.division(1, 0)


    def test_modulo(self):
        # Vérifier que 2 % 2 == 0
        self.assertEqual(calculatrice.modulo(2, 2), 0)
        # Verifier que 2 % 2 != 5
        self.assertNotEqual(calculatrice.modulo(2, 2), 5)
        # Vérifier l'erreur quand nous divisions par 0.
        with self.assertRaises(ArithmeticError):
            calculatrice.modulo(1, 0)

    def test_racine_carre(self):
        # Vérifier que V4 == 2.
        self.assertEqual(calculatrice.racine_carre(4), 2)
        # Vérifier que V6 == 3.
        self.assertEqual(calculatrice.racine_carre(9), 3)
        # Vérifier que V4 != 3.
        self.assertNotEqual(calculatrice.racine_carre(4), 3)
        # Vérifier que V6 != 2.
        self.assertNotEqual(calculatrice.racine_carre(9), 2)
        # Vérifier que les chaînes de caractère ne passent pas. 
        with self.assertRaises(TypeError):
            calculatrice.modulo("lol")
        # Vérifier que les négatifs ne passent pas.
        # Ne fonctionne pas.
        with self.assertRaises(ValueError):
            calculatrice.modulo("-1")