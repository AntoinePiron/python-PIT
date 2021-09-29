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
        res = [self.grid[i][colonne] for colonne in range(9)]
        return res

    def get_col(self, j):
        #On convertit en string pour se balader 
        intToStr = str(self.grid)
        #On initialise le tableau de retour vide
        res = []
        indice = j
        #On vient alors ajouter en se baladant tout les 9 indice ce qui correspond à une colonne
        while indice < len(intToStr):
            res.append(int(intToStr[indice]))
            indice += 9
        return res

    def get_region(self, reg_row, reg_col):
         # On convertit en string pour se balader
        intToStr = str(self.grid)
        res = []
        subList = []
        # On vient d'abord récuperer les lignes correspondantes qu'on stockd dans une liste secondaire
        for a in range(int(reg_row * 3), int(reg_row * 3 + 3), 1):
            rowindice = a * 9
            for pos in range(rowindice, rowindice + 9):
                subList.append(intToStr[pos])

        # On vient alors récuperer les colonnes qui vont avec
        colIndice = reg_col * 3
        while colIndice < len(subList):
            for id in range(colIndice, colIndice + 3):
                res.append(int(subList[id]))
            colIndice += 9

        return res

    def get_empty_pos(self):
        #On convertit en string pour se balader 
        intToStr = str(self.grid)
        res = []
        for i in range(len(intToStr)):
            if intToStr[i] == '0':
                #la position de la colonne est le reste de la divisin entiere de l'indice par 9
                cpos = i%9
                #on obitent le numero de ligne divisant par 9 pour obtenir la ligne
                lpos = (i - cpos)/9
                res.append((lpos,cpos))
            
        return res

    def write(self, i, j, v):
        #Pour obtenir la position on se base sur la méthode du dessus qu'on remonte à l'envers
        position = int(j + 9*i)
        #On convertit en string pour se balader 
        intToStr = str(self.grid)
        #on vient remplacer le caractere
        intToStr = intToStr[:position] + str(v) + intToStr[position+1:]
        #puis on affecte à la grid
        self.grid = int(intToStr)

    def copy(self):
        res = str(self.grid)
        return SudokuGrid(res)
