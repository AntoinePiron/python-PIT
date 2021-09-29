#-*-coding: utf8-*-
import linecache

class SudokuGrid:

    def __init__(self, initial_values_str):
        #On ne rentre que si la longueur est la bonne 
        if len(initial_values_str) == 81:
            try:
                #On va créer un tableau à double entrée qui contient nos chiffres et qui représenteras notre grille
                self.grid = [[int(initial_values_str[i + 9 * j]) for i in range(9)] for j in range(9)]
            except ValueError:
                print("Valeur incorrect")
                raise ValueError
        else:
            print("Longueur incorrect")
            raise ValueError

    @staticmethod
    def from_file(filename, line):
        #On ouvre dans un premier temps le fichier en mode lecture 
        database = open(filename, 'r')
        #On vient alors lire les lignes
        all_lines = database.readlines()
        #On récupere la ligne qui nous intéresse en prenant soin de retirer le caractère de retour à la ligne
        specificLine = all_lines[line].strip("\n")
        #On oublie pas de refermer le fichier 
        database.close()
        return SudokuGrid(specificLine)

    @staticmethod
    def from_stdin():
        #On vient récuperer la saisie utilisateur
        line = input("Veuillez indiquer votre grille de sudoku : ")
        #On retourne alors une instance avec cette ligne en param
        #Pas besoin de la vérifier car ce sera effectue dans le constructeur
        return SudokuGrid(line)

    def __str__(self):
        #Le string finale comtenant la grille 
        res = ""
        for row in range(9):
            #On va reconstruire chaque ligne grace au double for
            line = ""
            for col in range(9):
                line += str(self.grid[row][col])
            #A chaque tour on ajoute la ligne suivi d'un retour
            res += line + "\n"
        return res

    def get_row(self, i):
        #On vient récuperer la ligne spécifié à l'aide d'une liste en compréhension qui se balade dans la ligne
        res = [self.grid[i][col] for col in range(9)]
        return res

    def get_col(self, j):
        #Cette méthode est finalement similaire à la précedente on ne se balade juste pas dans le même sens
        res = [self.grid[row][j] for row in range(9)]
        return res

    def get_region(self, reg_row, reg_col):
        #A l'aide d'une liste en compréhension et d'un double for on va pouvoir récuperer aisément toutes les valeurs de la régions spécifié par l'utilisateur
        res = [self.grid[i + reg_row * 3][j + reg_col * 3] for i in range(3) for j in range(3)]
        return res

    def get_empty_pos(self):
        #On va récuperer toutes les listes des positions vides en compréhension de nouveau
        #Il suffit simpleemet de vérifier si la position est vide 
        res = [(i,j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]
        return res

    def write(self, i, j, v):
        #On affecte simplement la valeur 
        self.grid[i][j] = v

    def copy(self):
        old = [[self.grid[i][j] for j in range(9)] for i in range(9)]
        new_grid = self.__new__(self.__class__)
        new_grid.grid = old
        return new_grid
