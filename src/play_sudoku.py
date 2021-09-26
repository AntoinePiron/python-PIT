from grid import SudokuGrid
import sys
import os

#Méthode qui sera call au début, et qui, en fonction des argument donnés en ligne de commande, crée directement 
#une grille à partir d'une fichier valdie
def newGame():
    #Si le seul argument est le nom du programme
    if len(sys.argv) == 1:
        SudokuGrid.from_stdin()
    elif len(sys.argv) == 2 or len(sys.argv) > 3 : 
        print("Entrez 2 argument svp, un nom de fichier et un numéro de ligne")
    else:
        if os.path.isfile(sys.argv[2]) and type(sys.argv[3]) == int:
            SudokuGrid.from_file(sys.argv[2],sys.argv[3])
        else:
            print("Argument non valables, réessayez")
 
newGame()