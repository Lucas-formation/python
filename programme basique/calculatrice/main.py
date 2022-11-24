from math import *

class calculatrice():

    def addition(a, b):
        # addition
        if isinstance(a and b,int):
            # N'accepter que les int
            return a+b
        else:
            # Si ce n'est pas un int, retourner error.
            return "error"
            
    def soustraction(a, b):
        # Soustraction
        if isinstance(a and b,int):
            # N'accepter que les int
            return a-b
        else:
            # Si ce n'est pas un int, retourner error.
            return "error"

    def multiplication(a, b):
        # Multiplication
        if isinstance(a and b,int):
            # N'accepter que les int
            return a*b
        else:
            # Si ce n'est pas un int, retourner error.
            return "error"
            
    def division(a, b):
        # Division
        if isinstance(a and b,int):
            # N'accepter que les int
            #if b == 0:
            #    # Vérifier si b == 0
            #    return "Impossible de diviser par 0."
            return a/b
        else:
            # Si ce n'est pas un int, retourner error.
            return "error"
    
    def modulo(a, b):
        # Modulo
        if isinstance(a and b,int):
            # N'accepter que les int
            #if b == 0:
            #    # Vérifier si b == 0
            #    return "Impossible de diviser par 0."
            return a%b
        else:
            # Si ce n'est pas un int, retourner error.
            return "error"

    def racine_carre(a):
        # Création d'une exception
        if a < 0 :
            # Trouver comment passer en Python
            pass
        # Racine carré
        return sqrt(a)

#print(sqrt(-1))
