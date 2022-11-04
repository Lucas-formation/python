#Imports
import os

#Avoir le fichier courrant (actuel)
print(os.getcwd())

#lister les documents dans le fichier
files = os.listdir(os.getcwd())
#Les afficher
print(files)

#Lister les fichiers puis les trier
#Trie par la taille
files.sort(key=lambda f: os.stat(f).st_size, reverse=False)
#Afficher le résultat.
print(files)