#Liste initiale
test_list = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi']

#Afficher la liste originel
print("Voici la liste originel : " + str(test_list))

#Choix du nombre de caractère à retirer
k = 3

#Retirer les caractères
res = list(map(lambda i: i[k :], test_list))

#Afficher
print("Liste modifiée : " + str(res))