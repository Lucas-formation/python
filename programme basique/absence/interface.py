from pprint import pprint
import inquirer
import sys
import os
import json 

class interface:

    """
        Lancement
    """

    def __init__(self):
        print("-- Lancement --")

    def accueil(self):
        # Créer le selecteur dans le CMD
        mode = [
            inquirer.List(
                "mode",
                message="Choisissez avec les flèches ",
                choices=["Se connecter", "Quitter"],
            ),
        ]
        reponse = inquirer.prompt(mode)
        if reponse == {'mode': 'Quitter'}:
            print("Fermeture du programme...")
            self.deconnexion()
        elif reponse == {'mode': 'Se connecter'}:
            print("-- Se connecter --")
            self.connexion()
    
    """
        Connexion et deconnexion
    """

    def connexion(self):
        # Connexion au compte
        identifiant = input("Votre identifiant : ")
        if self.bdd_id(identifiant):
            mot_de_passe = input("Votre mot de passe : ")
            if self.bdd_mdp(identifiant, mot_de_passe):
                self.information = self.bdd(identifiant)
                self.salon()
            else:
                print("Mot de passe incorrect.")
                self.incorrect()
        else:
            print("Identifiant incorrect.")
            self.incorrect()
            
    def deconnexion(self):
        # A tester
        if "session" in locals():
            # Vérifier si l'objet session existe
            # Si oui, le détruire.
            del self.session
        # Fermer le programme.
        sys.exit()

    """
        Cas connexion
    """

    def incorrect(self):
        # Si l'identifiant ou le mot de passe sont incorrects, que faire ?
        mode = [
            inquirer.List(
                "mode",
                message="Choisissez avec les flèches ",
                choices=["Nouvel essai", "Quitter"],
            ),
        ]
        reponse = inquirer.prompt(mode)
        if reponse == {'mode': 'Quitter'}:
            print("Fermeture du programme...")
            self.deconnexion()
        elif reponse == {'mode': 'Nouvel essai'}:
            print("-- Nouvel essai --")
            self.connexion()

    def bdd_id(self, identifiant):
        # Aller chercher dans les fichiers l'identifiant
        id_bdd = "lucas.gaio@gmail.com"
        # Boucle pour faire toute les lignes
        if id_bdd == identifiant :
            return True
        else:
            return False

    def bdd_mdp(self, identifiant, mot_de_passe):
        # Chercher le mdp par l'utilisateur
        # Aller chercher dans les fichiers le mdp par rapport à l'identifiant.
        id_mot_de_passe = "mdp123"
        if id_mot_de_passe == mot_de_passe:
            return True
        else:
            return False

    def bdd(self, identifiant):
        # Retourner toute les information de l'utilisateur
        return ({'nom' : "", 'prenom' : "", 'mail' : "", 'naissance' : ""})

    # Trop d'essai.

    """
        Affichage
    """

    def salon(self):
        # Salon, endroit central après la connexion
        print("Que souhaitez-vous faire ?")
        mode = [
            inquirer.List(
                "mode",
                message="Choisissez avec les flèches ",
                choices=["Voir mes informations", "Quitter"],
            ),
        ]
        reponse = inquirer.prompt(mode)
        if reponse == {'mode': 'Quitter'}:
            print("Fermeture du programme...")
            self.deconnexion()
        elif reponse == {'mode': 'Voir mes informations'}:
            os.system('cls')
            self.affichage()

    def affichage(self):
        # Afficher les informations de l'utilisateur.
        # A modifier et améliorer
        print("-- Information du compte -- \n \n", "Nom : ", self.information["nom"], "\n", "Prénom : ", self.information["prenom"], "\n", "Mail : ", self.information["mail"], "\n", "Date de naissance : ", self.information["naissance"],"\n")
        self.salon()

    def suppression_data(nom_fichier):
        os.remove(nom_fichier)

"""
utilisateur = {
	"nom": "gaio",
	"prenom": "lucas",
	"mail": "lucas.gaio@gmail.com",
	"naissance": "01/11/2001",
    "mot_de_passe": "mdp123",
    "admin": True
}

with open('data.json', 'w') as mon_fichier:
	json.dump(utilisateur, mon_fichier)
"""
with open('data.json') as mon_fichier:
    data = json.load(mon_fichier)

print(data)
