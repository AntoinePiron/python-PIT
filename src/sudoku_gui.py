#!/usr/bin/env python3
#-*-coding: utf8-*-
import tkinter as tk

def gameScreen():
    print("ok")

def which_button(entry, window):
    #Quelque soit le choix de l'utilisateur on va quitter la fenetre 
    window.quit()
    if entry == "Play":
        gameScreen()

#Cette méthode va servir d'écran d'accueil pour le jeu 
def entry_screen():
    #Création de la fenetre
    win = tk.Tk()
    #Choix du titre de la fenetre
    win.title("Main Menu")
    #Taille de la fenetre
    win.geometry("500x500")
    #Placement d'un bouton play au centre de la fenetre
    playButton = tk.Button(win, text ="Play", width=20, height=2, command=lambda m="Play": which_button(m,win))
    playButton.place(relx=.5, rely=.45, anchor="center")
    quitButton = tk.Button(win, text ="Quit", width=20, height=2, command=lambda m="Quit": which_button(m,win))
    quitButton.place(relx=.5, rely=.55, anchor="center")
    win.mainloop()

def main():
    entry_screen()
    pass

if __name__ == "__main__":
    main()