#import des packages
import turtle

#fonction de dessin
#étoile colorée
def colored_star():
    #taille de l'étoile
    size = 80

    #couleur
    turtle.color("red")

    #largeur de l'objet
    turtle.width(4)

    #angle
    angle = 120

    #color to fill
    turtle.fillcolor("yellow")
    turtle.begin_fill()

    # Frome de l'étoile
    for side in range(5):
        turtle.forward(size)
        turtle.right(angle)
        turtle.forward(size)
        turtle.right(72 - angle)
    
    #fill color
    turtle.end_fill()

#lancement
colored_star()