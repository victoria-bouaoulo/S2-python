import tkinter as tk
import random

couleurs = ["red", "green", "blue", "cyan", "yellow", "black", "pink", "purple"]
tentatives_max = 10

CANVAS_WIDTH, CANVAS_HEIGHT= 900, 700
root = tk.Tk()
root.title("Mastermind")
canvas_accueil = tk.Canvas(root, width= CANVAS_WIDTH, height= CANVAS_HEIGHT, background= "LightBlue1")
canvas_accueil.grid()
label = tk.Label(root, text= "Jouons au Mastermind!", font= ("helevtica", "30"))
label.place(x= 250, y= 10)

def clic(couleur_bouton):
    eedevs

def solo():  # définie le mode de jeu à 1 joueur
    code_solo = random.sample(couleurs, 4)
    print(code_solo)
    fenetre_solo = tk.Toplevel(root)
    fenetre_solo.title("Mode 1 joueur")
    canvas_solo = tk.Canvas(fenetre_solo, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background="LightBlue1")
    canvas_solo.pack()
# création de l'interface de jeu: boutons pour choisir les couleurs & cercles
    rond1 = canvas_solo.create_oval((170, 50), (220, 100), width = 2, outline="black", fill="white"),
    rond2 = canvas_solo.create_oval((250, 50), (300, 100), width = 2, outline="black", fill="white"),
    rond3 = canvas_solo.create_oval((330, 50), (380, 100), width = 2, outline="black", fill="white"),
    rond4 = canvas_solo.create_oval((410, 50), (460, 100), width = 2, outline="black", fill="white")
    carre = canvas_solo.create_rectangle((490, 50), (540, 100), width=2, outline= "black")
    bouton_rouge = tk.Button(canvas_solo, background="red", text= "     ", ) 
    bouton_rouge.place(x= 250, y= 500)
    bouton_vert = tk.Button(canvas_solo, background="green", text= "     ")
    bouton_vert.place(x= 290, y= 500)
    bouton_bleu = tk.Button(canvas_solo, background="blue", text= "     ")
    bouton_bleu.place(x= 330, y= 500)
    bouton_cyan = tk.Button(canvas_solo, background="cyan", text= "     ")
    bouton_cyan.place(x= 370, y= 500)
    bouton_jaune = tk.Button(canvas_solo,background= "yellow", text= "     ")
    bouton_jaune.place(x=410, y= 500)
    bouton_noir = tk.Button(canvas_solo,background= "black", text= "     ")
    bouton_noir.place(x=450, y= 500)
    bouton_rose = tk.Button(canvas_solo,background= "pink", text= "     ")
    bouton_rose.place(x=490, y= 500)
    bouton_violet = tk.Button(canvas_solo,background= "purple", text= "     ")
    bouton_violet.place(x=530, y= 500)



def multi(): #définie le mode de jeu à 2 joueurs
    fenetre_multi = tk.Toplevel(root)
    fenetre_multi.title("Mode 2 joueurs")
    canvas_multi = tk.Canvas(fenetre_multi, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background="LightBlue1")
    canvas_multi.pack()
    label_multi = tk.Label(canvas_multi, text="Choisissez un code", font=("helvetica", "30"))
    label_multi.place(x=250, y=10)
# création des boutons permettant de créer le code secret
    bouton_rouge = tk.Button(canvas_multi, background="red", text= "    ")   
    bouton_rouge.place(x= 250, y= 500)
    bouton_vert = tk.Button(canvas_multi, background="green", text= "     ")
    bouton_vert.place(x= 290, y= 500)
    bouton_bleu = tk.Button(canvas_multi, background="blue", text= "     ")
    bouton_bleu.place(x= 330, y= 500)
    bouton_cyan = tk.Button(canvas_multi, background="cyan", text= "     ")
    bouton_cyan.place(x= 370, y= 500)
    bouton_jaune = tk.Button(canvas_multi,background= "yellow", text= "     ")
    bouton_jaune.place(x=410, y= 500)
    bouton_noir = tk.Button(canvas_multi,background= "black", text= "     ")
    bouton_noir.place(x=450, y= 500)
    bouton_rose = tk.Button(canvas_multi,background= "pink", text= "     ")
    bouton_rose.place(x=490, y= 500)
    bouton_violet = tk.Button(canvas_multi,background= "purple", text= "     ")
    bouton_violet.place(x=530, y= 500)

    canvas_multi.pack()
    rond1 = canvas_multi.create_oval((250, 300), (300, 350), width = 2, outline="black", fill="white")
    rond2 = canvas_multi.create_oval((330, 300), (380, 350), width = 2, outline="black", fill="white")
    rond3 = canvas_multi.create_oval((410, 300), (460, 350), width = 2, outline="black", fill="white")
    rond4 = canvas_multi.create_oval((490, 300), (540, 350), width = 2, outline="black", fill="white")


bouton_solo = tk.Button(root, text= "1 joueur", font= ("helvetica", "20"),
                        activebackground= "#BCBCBC", command= solo)
bouton_solo.place(x= 390, y= 200)

bouton_multi = tk.Button(root, text= "2 joueurs", font= ("helevetica", "20"),
                         activebackground= "#BCBCBC", command= multi)
bouton_multi.place(x= 388, y= 300)



root.mainloop()

