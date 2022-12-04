from individu import individu

class admin(individu):
    # Nous récupérons la classe individu qui est parent de cette classe.

    def __init__(self, nom, prenom) -> None:
        super().__init__(nom, prenom)
        pass

    def creation_compte():
        # Permettre à l'administrateur de créer un compte étudiant, ou professeur.
        pass

    def modifier_compte():
        # Permettre à l'administrateur de changer les informations d'un étudiant, ou professeur.
        pass 