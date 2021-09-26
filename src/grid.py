#-*-coding: utf8-*-

class SudokuGrid:

    def __init__(self, initial_values_str):
        #Dans un premier temps si la longueur ne convient pas on lève immédiatement une erreur
        if len(initial_values_str) != 81:
                raise ValueError()
        #Si la longueur est bonne on tente alors de convertir à l'aide d'un bloc try 
        try:
            self.grid = int(initial_values_str)
        except:
            raise ValueError()

    @staticmethod
    def from_file(filename, line):
        #On ouvre le fichier en mode lecture
        file = open(filename, 'r')
        #On stock son contenu
        content = file.readlines()
        #On vient alors récuperer notre ligne specifique, on prend line -1 la ligne 1 = index 0
        specificLine = content[line-1]
        #On vient alors générer la grille de sudoku avec la ligne en paramètre, pas besoin de la vérifier, ce sera fait dans le constructeur
        return SudokuGrid(specificLine)

    @staticmethod
    def from_stdin():
        #On vient récuperer la saisie utilisateur
        line = input("Veuillez indiquer votre grille de sudoku : ")
        #On retourne alors une instance avec cette ligne en param
        #A nouveau pas besoin de la vérifier car ce sera effectue dans le constructeur
        return SudokuGrid(line)

    def __str__(self):
        #on convertit d'abord notre grille de int en str
        intToStr = str(self.grid)
        res = ""
        #On va ajouter les différents numéro en prenant soin de faire un retour à la ligne
        #tout les 9 caractères pour bien correspondre à une grille de sudoku
        for i in range(0,len(intToStr), 9):
            res += intToStr[i:i+9] + "\n"
        return res

    def get_row(self, i):
        #La ligne va correspondre à une position dans la chaine de int
        position = i*9 #avec cette formule on a bien l1 = 0, l2 = 9 etc
        #On vient alors récuperer le tout avec une liste en compréhension
        res = [int(a) for a in str(self.grid)[position:position+9]]
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
        raise NotImplementedError()

    def get_empty_positions(self):
        raise NotImplementedError()

    def write(self, i, j, v):
        raise NotImplementedError()

    def copy(self):
        raise NotImplementedError()
