#!/usr/bin/env python3
#-*-coding: utf8-*-
import tkinter as tk
from tkmacosx import Button
from tkinter.constants import *
from grid import SudokuGrid

def createGrid(grid):
    win = tk.Tk()
    win.title("Suduoku main")
    for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light blue"
            else:
                colour="white"
            x=grid[rowindex][colindex]
            if x==0:
                colourTxt="red"
            else:
                colourTxt="black" 
            #Sur macos je suis obligé d'utiliser l'import tkmacosx la ligne pour les autres systemes d'exploitation est commenté    
            #MAC
            btn=Button(win, width=60, height=60, bg=colour, text=x, fg=colourTxt)  
            #AUTRE 
            #btn=tk.Button(win, width=60, height=60, bg=colour, text=x, fg=colourTxt)  
            btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)
            btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)

    win.mainloop()

def gameScreen():
    gridToSend = SudokuGrid.from_file("sudoku_db.txt", 1)
    createGrid(gridToSend.grid)

def which_button(entry, window):
    window.destroy()
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