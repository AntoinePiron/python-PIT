#!/usr/bin/env python3
#-*-coding: utf8-*-
import tkinter as tk
from tkmacosx import Button
from tkinter.constants import *

from tkmacosx.widgets import button
from grid import SudokuGrid
import easygui

def clickCase(window,rowindex,colindex,grid):
    res = easygui.integerbox("Veuillez rentrer la valeur souhaitée", "Case ("+str(rowindex+1)+","+str(colindex+1)+")", lowerbound=1, upperbound=9)
    grid.write(rowindex, colindex, res)
    window.destroy()
    createGrid(grid)

def createGrid(sudokgrid):
    win = tk.Tk()
    win.title("Suduoku main")
    for rowindex in range (9):
        for colindex in range (9):
            if (rowindex in (0,1,2,6,7,8) and colindex in (3,4,5) or (rowindex in (3,4,5) and colindex in (0,1,2,6,7,8))):
                    colour="light blue"
            else:
                colour="white"
            x=sudokgrid.grid[rowindex][colindex]
            if x==0:
                colourTxt="red"
            else:
                colourTxt="black" 
            #Sur macos je suis obligé d'utiliser l'import tkmacosx la ligne pour les autres systemes d'exploitation est commenté    
            #MAC
            btn=Button(win, width=60, height=60, bg=colour, text=x, fg=colourTxt, command=lambda row = rowindex, col = colindex, window = win, grid = sudokgrid: clickCase(window,row,col,grid))
            #AUTRE,
            #btn=tk.Button(win, width=3, height=3, bg=colour, text=x, fg=colourTxt, command=lambda row = rowindex, col = colindex, window = win, grid = sudokgrid: clickCase(window,row,col,grid)) 
            btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)
            btn.grid(row=rowindex, column=colindex, sticky=N+S+E+W)    
    win.mainloop()

def gameScreen():
    gridToSend = SudokuGrid.from_file('../sudoku_db.txt', 1)
    createGrid(gridToSend)

def which_button(entry, window):
    window.destroy()
    if entry == "Play":
        gameScreen()
#test 1212    
#Cette méthode va servir d'écran d'accueil pour le jeu 
def entry_screen():
    #Création de la fenetre
    win = tk.Tk()
    #Choix du titre de la fenetre
    win.title("Main Menu")
    #Taille de la fenetre
    win.geometry("500x500")
    #Placement d'un bouton play au centre de la fenetre
    #J'utilise les boutons mac os de nouveau

    #MAC
    playButton = Button(win, text ="Play", width=300, height=50, command=lambda m="Play": which_button(m,win))
    quitButton = Button(win, text ="Quit", width=300, height=50, command=lambda m="Quit": which_button(m,win))

    #WINDOWS
    #layButton = tk.Button(win, text ="Play", width=20, height=5, command=lambda m="Play": which_button(m,win))
    #quitButton = tk.Button(win, text ="Quit", width=20, height=5, command=lambda m="Quit": which_button(m,win))

    playButton.place(relx=.5, rely=.40, anchor="center")
    quitButton.place(relx=.5, rely=.60, anchor="center")
    win.mainloop()

if __name__ == "__main__":
    entry_screen()