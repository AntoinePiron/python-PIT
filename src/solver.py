#-*-coding: utf8-*-

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
        raise NotImplementedError()

    def commit_one_var(self):
        #On vient parcourir les solutions
        for val in self.solutions:
            #si jamais un des tuples de valeurs poossibles ne contient plus qu'une val
            if len(val[1]) == 1:
                self.grid.write(val[0][0],val[0][1],val[1])
                return (val[0][0],val[0][1],val[1])
        else:
            return None

    def solve_step(self):
        # Tant qu'il reste des cases vides on continue 
        while(self.grid.get_empty_pos() != []):
            self.grid.commit_one_var()
            self.grid.reduce_domains

    def is_valid(self):
        raise NotImplementedError()

    def is_solved(self):
        return(not self.grid.get_empty_pos())

    def branch(self):
        raise NotImplementedError()

    def solve(self):
        raise NotImplementedError()
