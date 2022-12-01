from pprint import pprint
import inquirer

class trier():

    """
    Initialisation
    Et toute les méthodes utiles.
    """
    def __init__(self) -> None:
        # Création de la varaible saisie qui contiendra la liste.
        self.saisie = []
        # Choisir son option
        self.selecteur_cmd()
        if self.reponse == {'mode': 'Générique'}:
            # Génération de la liste de façon automatique.
            # Faire du aléatoire à l'avenir.
            self.saisie = [8,9,5,4,9]
        elif self.reponse == {'mode': 'Editer'}:
            # Saisir manuellement la liste.
            self.entree()
        elif self.reponse == {'mode': 'Importer'}:
            # Importer des données.
            # A faire.
            print("Cette fonction n'est pas encore disponible.")
        
    def entree(self):
        # Choisir le nombre d'élément à saisir
        n = int(input("Entrez un nombre, qui est le nombre de valeur que vous souhaitez saisir : "))
        # Boucle suivant le nombre d'élément que souhaite saisir l'utilisateur
        for i in range(0, n):
            ele = int(input())
            self.saisie.append(ele) # ajout de l'élément choisit

    def selecteur_cmd(self):
        # Créer le selecteur dans le CMD
        mode = [
            inquirer.List(
                "mode",
                message="Souhaitez-vous faire une liste générique ou la définir vous même ?",
                choices=["Générique", "Editer", "Importer"],
            ),
        ]
        self.reponse = inquirer.prompt(mode)

    """
    Trier, pour les tests
    """
    def trie_croissant(saisie = []):
        # Trie des nombres croissant,
        # et caractères, ou chaine, par ordre alphabétique. 
        saisie = sorted(saisie)
        return saisie

    """
    Trier, avec "self", sans test.
    Je dois encore regarder comment tester quand il y a des saisies à faire, non pas en paramètre, mais en cmd.
    """
    def trie_croissant_self(self):
        # Trie des nombres croissant,
        # et caractères, ou chaine, par ordre alphabétique. 
        self.saisie = sorted(self.saisie)
        return self.saisie

    def trie_nombre_croissant_self(self):
        # Trie seulement des nombres de façon croissante.
        self.saisie.sort()

#test = trier()
#test.trie_croissant()
#print(test.saisie)
a = trier.trie_croissant([5,7,2,3,9])
print(a)