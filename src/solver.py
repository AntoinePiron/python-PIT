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
            #On récupère la région de l'elements courant et de l'element precedent
            # l'opérateur // est une division entière
            region_val = (val[0][0] // 3, val[0][1] // 3)
            region_last = (last_i // 3, last_j // 3)
            if last_v in val[1] and (
                    val[0][0] == last_i or val[0][1] == last_j or (region_val == region_last)):
                val[1].remove(last_v)
    
    def commit_one_var(self):
        retResult = ()
        #On se balade parmi les solutions
        for val in self.solutions:
            #Si jamais le tuple de solutions ne fait que 1 <=> une seule solution possible pour la case
            if len(val[1]) == 1:
                #On écrit notre valeur 
                self.grid.write(val[0][0], val[0][1], next(iter(val[1])))
                #Puis on retourne comme demandé
                retResult = (val[0][0], val[0][1], next(iter(val[1])))
                return retResult
        #Si jamais on est sorti du for c'est qu'aucune solution n'a été trouvé => on return None
        return None

    def solve_step(self):    
        last_change = -1
        #Comme nous allons utilisé la méthode commit_one_var pn va boucler tant que notre résultat n'est pas nul
        #Autrement dit on boucle tant qu'il y a des valeurs à rentrer dans la grille
        while last_change is not None:
            #on tente des solutions
            last_change = self.commit_one_var()
            if last_change is not None:
                #Comme on a trouvé une valeur on vient l'enlever des différentes solutions
                self.solutions.remove(((last_change[0], last_change[1]), set()))
                #Comme on a rajouté une valeur dans la grille on doit réactualiser les solutions
                self.reduce_domains(last_change[0], last_change[1], last_change[2])
                last_change = ()

    def is_valid(self):
        #On vient se balader dans la liste de solution
        for val in self.solutions:
            #Si un set de solution n'est pas vide cela siginifie que la solution courante est encore valable 
            if val[1] != set():
                return True
            else:
                return False

    def is_solved(self):
        complete = False
        if not list(self.grid.get_empty_pos()):
            complete = True
        return complete


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
        return liste_solutions

    def solve(self):
        self.solve_step()
        if self.is_solved():
            return self.grid
        elif self.is_valid():
            oui = self.branch()
            for element in oui:
                s = element.solve()
                if s is not None:
                    return s
            return None
        else:
            return None
