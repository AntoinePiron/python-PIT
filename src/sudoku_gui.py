#!/usr/bin/env python3
#-*-coding: utf8-*-
import tkinter as tk
from tkinter.constants import Y

#Cette méthode va servir d'écran d'accueil pour le jeu 
def entry_screen():
    #Création de la fenetre
    win = tk.Tk()
    #Choix du titre de la fenetre
    win.title("Main Menu")
    #Taille de la fenetre
    win.geometry("500x500")
    #Placement d'un bouton play au centre de la fenetre
    tk.Button(win, text ="Play", width=20, height=2).place(relx=.5, rely=.5, anchor="center")
    win.mainloop()
    return win

def main():
    entry_screen()
    pass

if __name__ == "__main__":
    main()