#!/usr/bin/env python3
#-*-coding: utf8-*-

import easygui

#Cette méthode va servir d'écran d'accueil pour le jeu 
def entry_screen():
    #On utilise une button box pour récuperer le choix 
    res = easygui.buttonbox('Bienvenue dans ce jeu de sudoku', 'Sudoku', ('Play', 'Quit'))
    return res

def game():
    pass

def main():
    start_game = entry_screen()
    if start_game == 'Play':
        print("Début du jeu")
        game()
    else: 
        exit()

if __name__ == "__main__":
    main()