#!/usr/bin/env python3
#-*-coding: utf8-*-
import tkinter as tk

#Cette méthode va servir d'écran d'accueil pour le jeu 
def entry_screen():
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("500x500")
    root["bg"] = "coral"
    root.mainloop()

def main():
    entry_screen()
    pass

if __name__ == "__main__":
    main()