from tkinter import *
from labo11.utils import *
from labo11.joueur import *
from labo11.plateau import *
from labo11.scrabble import *
fenetre = Tk()

bouton=Button(fenetre, text="jeton", command=fenetre.quit)
bouton.pack()

fenetre.mainloop()

self.chevalet.delete('lettre')
        for j, jeton in enumerate(self.joueur_actif.jetons):
            if jeton:

                fenetre = Tk()
                bouton = Button(fenetre, text=jeton)                     #text=jeton, command=fenetre.quit)
                bouton.pack()
                fenetre.mainloop()


"""root = Tk()

#def key(event):
    #print("pressed", repr(event.char))

def callback(event):
    #frame.focus_set()
    print("clicked at", event.x, event.y)
    return (event.x, event.y)

def jeton_choisi():

    return

frame = Frame(root, width=100, height=100)
#frame.bind("<Key>", key)
frame.bind("<Button-1>", callback)

frame.pack()

root.mainloop()
print(callback)

#self.parent.bind("<Button-1>", self.callback())


fenetre = Tk()
def recupere():
    print("Alerte", entree.get())

value = StringVar()
value.set("Valeur")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()

bouton = Button(fenetre, text="Valider", command=recupere)
bouton.pack()
fenetre.mainloop()

def dessiner_chevalet(self):
    self.chevalet.delete('lettre')
    for j, jeton in enumerate(self.joueur_actif.jetons):
        if jeton:
            dessiner_jeton(self.chevalet, jeton, 0, j, self.nb_pixels_per_case)
            print(jeton)
            print(j)
            print(self.nb_pixels_per_case)
            print(type(self.chevalet))
            print(type(self.joueur_actif.jetons))

Scrabble.mainloop()

#TODO
    def key(event):
        print("pressed", repr(event.char))

    def callback(event):

        Scrabble.chevalet.focus_set()
        print("clicked at", event.x, event.y)
        Scrabble.chevalet.bind("<Key>", key)
        Scrabble.chevalet.bind("<Button-1>", callback)

    def choisir_jetons(self, event):

        if 0 < event.x < 60:
            pass """
"""class What:


    def __init__(self):
        dunno = 0


    def gestionEvent(self, input):
        # do whatever with input
        input += input + 1


    def click(self):
        var = input('whatever')
        self.gestionEvent(var)
raw_input("Press Enter to continue ...")
exit()""""""