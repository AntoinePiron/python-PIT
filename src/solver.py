#-*-coding: utf8-*-

from unittest.case import doModuleCleanups


class SudokuSolver:

    def __init__(self, grid):
        #On initialise un array pour les solutions
        self.solutions = []
        #On renseigne note grille
        self.grid = grid
        #On appel ensuite la méthode comme demandé
        self.reduce_all_domains()
        #On crée une liste

    def reduce_all_domains(self):
        #On va explorer toutes les positions vides 
        for allPos in self.grid.get_empty_pos():
            #valeur possible
            val_poss = set()
            #ligne, colonne et region correspondant à notre tuple
            ligne_tuple = list(self.grid.get_row(allPos[0]))
            colonne_tuple = list(self.grid.get_col(allPos[1]))
            region_tuple = list(self.grid.get_region(allPos[0] // 3, allPos[1] // 3))

            #Si la valeur i ne se situe ni dans la ligne, ni dans la colonne, ni dans la région alors c'est une valeur possible 
            for i in range(1, 10):
                if i not in ligne_tuple and i not in colonne_tuple and i not in region_tuple:
                    val_poss.add(i)

            self.solutions.append((allPos, val_poss))

    def reduce_domains(self, last_i, last_j, last_v):
        for val in self.solutions:
        ##On récupère la région de l'elements courant et de l'element precedent
            region_val = (val[0][0] // 3, val[0][1] // 3)
            region_last = (last_i // 3, last_j // 3)
            if last_v in val[1] and (
                    val[0][0] == last_i or val[0][1] == last_j or (region_val == region_last)):
                val[1].remove(last_v)
    
    def commit_one_var(self):
        #On vient parcourir les solutions
        for val in self.solutions:
            #si jamais un des tuples de valeurs poossibles ne contient plus qu'une val
            if len(val[1]) == 1:
                test = 0
                for i in val[1]:
                    test = i
                self.grid.write(val[0][0],val[0][1],test)
                return (val[0][0],val[0][1],test)
        else:
            return None

    def solve_step(self):
        # Tant qu'il reste des cases vides on continue 
        last_change = (0,0,0)
    
        while last_change is not None:
            last_change = self.commit_one_var()
            if last_change is None:
                break
            self.reduce_domains(last_change[0], last_change[1], last_change[2])
            self.solutions.remove(((last_change[0], last_change[1]), set()))

    def is_valid(self):
        for element in self.solutions:
            if element[1] != set():
                return True
            else:
                return False

    def is_solved(self):
        #L'expression not liste permet de verifier si cettte derniere est vide
        return(not self.grid.get_empty_pos())

    def branch(self):
        liste_solutions = []
        coordonnees_mini = ()
        set_mini = {}
        self.solutions.sort(key=lambda oui: len(oui[1]))
        coordonnees_mini = self.solutions[0][0]
        set_mini = self.solutions[0][1]
        for i in set_mini:
            grille_sudoku_en_cours = self.grid.copy()
            grille_sudoku_en_cours.write(coordonnees_mini[0], coordonnees_mini[1], i)
            sous_probleme = self.__class__(grille_sudoku_en_cours)
            liste_solutions.append(sous_probleme)
        # print(liste_solutions)
        return liste_solutions

    def solve(self):
        # print("oui")
        self.solve_step()
        if self.is_solved():
            # print(self.grid)
            # print("Résolu !")
            # print(len(self.branch()), "branches")
            return self.grid
        elif self.is_valid():
            oui = self.branch()
            for element in oui:
                # print("oui")
                # print(element)
                s = element.solve()
                if s is not None:
                    # print("S renvoyé")
                    return s
            return None
        else:
            return None
        # print("Pas résolue")
        # raise NotImplementedError()
