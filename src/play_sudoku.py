#!/usr/bin/env python3
#-*-coding: utf8-*-

from grid import SudokuGrid
import sys
import os


def play(game_grid):
    while len(game_grid.get_empty_pos()) > 0:
        print("Etat actuel de la grille : ")
        print("--------------------------------------")
        print(game_grid)
        print("--------------------------------------")
        while 1:
            x = input("x : ")
            y = input("y : ")
            v = input("v : ")
            try:
                x = int(x)
                y = int(y)
                v = int(v)
            except:
                print("Veuillez renseigner des entier.")
                continue
            if x > 8 or x < 0 or y < 0 or y > 8 or v < 1 or v > 9:
                print("Veuillez renseigner des valeurs compatibles.")
                continue
            else:
                game_grid.write(x, y, v)
                break


def newGame():
    # Si le seul argument est le nom du programme
    if len(sys.argv) == 1:
        play(SudokuGrid.from_stdin())
    elif len(sys.argv) == 2 or len(sys.argv) > 3:
        print("mauvais nb arg")
    else:
        try:
            num = int(sys.argv[2])
            if os.path.isfile(sys.argv[1]):
                play(SudokuGrid.from_file(str(sys.argv[1]), num))
            else:
                print("Argument non valable")
        except:
            print("Argument numérique incorrect")


newGame()
