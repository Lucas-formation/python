from individu import individu

class etudiant(individu):
    # Nous récupérons la classe individu qui est parent de cette classe.

    def __init__(self, nom, prenom) -> None:
        super().__init__(nom, prenom)
        #self.niveau = niveau
        #self.promotion = promotion
        pass