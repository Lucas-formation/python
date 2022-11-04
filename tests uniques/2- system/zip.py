number_list = [1, 2, 3]
str_list = ['one', 'two', "three"]

#Pas d'itteration passe
result = zip()

#convertir un iterateur en liste
result_list = list(result)
print(result_list)

#Deux iterrateur passé
result = zip(number_list, str_list)

#Convertir un iterateur en set
result_set = set(result)
print(result_set)