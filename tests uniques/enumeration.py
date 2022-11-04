from doctest import Example


liste = ["truc", "machin", "bidule"]

def iterate_using_range():
    # La fonction utile mais pas efficace. 
    for i in range(len(liste)):
        element = liste[i]
        example = f"Element {i +1} -- {element}"
        print(example)

def iterate_using_ennumerate():
    # La fonction la plus efficace
    for i, element in enumerate(liste, 1):
        example = f"Element {i} -- {element}"
        print(example)

iterate_using_ennumerate()