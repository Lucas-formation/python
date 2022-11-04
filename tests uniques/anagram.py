def anagramCheck(str1, str2):

    list1, list2 = list(str1), list(str2)
    list1.sort()
    list2.sort()

    position = 0
    matches = True

    while position < len(str1) and matches:
        if list1[position] == list2[position] :
            position+=1
        else:
            matches = False

    return matches

print("enter any two strings :")
string1=input()
string2=input()
print(anagramCheck(string1, string2))