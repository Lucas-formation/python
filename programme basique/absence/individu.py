import sys

"""
    Classe individu contenant toute les fonctions communes du profil étudiant et du profil administrateur.
"""

class individu():

    """
        Partie initialisation
    """

    def __init__(self, nom = "étudiant", prenom = "étudiant", mail = "prénom.nom@gmail.com", naissance = "01/01/01") -> None:
        # Initialisation de l'objet.
        self.nom = nom
        self.prenom = prenom
        self.mail = mail
        self.naissance = naissance
        # Je vais créer un générateur de mdp un de ces jours.
        self.mot_de_passe = "mdp1234"

    """
        Partie Récupération
    """

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_mail(self):
        return self.mail

    def get_naissance(self):
        return self.naissance

    def get_mdp(self):
        return self.mot_de_passe

    """
        Partie modification
    """

    def set_mdp(self, mdp):
        self.mot_de_passe = mdp

    def set_nom(self, nom):
        self.nom = nom

    def set_prenom(self, prenom):
        self.prenom = prenom

    def set_mail(self, mail):
        self.mail = mail

    def set_naissance(self, naissance):
        self.naissance = naissance

    """
        Partie suppression
    """

    # Rien pour l'instant

    """
        Partie autre
    """

    def connecter(identifiant_rentre, mdp_rentre, identifiant_bdd, mdp_bdd):
        # Permettre à la personne de se connecter
        # Besoin de chercher en boucle les données de la bdd
        if identifiant_bdd == identifiant_rentre and mdp_bdd == mdp_rentre :
            return True
        else :
            print("Identifiant ou mot de passe incorrect.")
            return False

    # mdp oublié

    # changement de mdp

"""
    Liste des choses dans d'autres classes
    - Déconnection dans "interface".
    - Création de la classe dans "interface".
    - Affichage des informations dans "interface".
"""