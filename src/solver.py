#-*-coding: utf8-*-

class SudokuSolver:

    def __init__(self, grid):
        #On initialise un array pour les solutions
        self.solutions = []
        #On renseigne note grille
        self.grid = grid
        #On appel ensuite la méthode comme demandé
        self.reduce_all_domains()

    def reduce_all_domains(self):
        #On va explorer toutes les positions vides 
        for allPos in self.grid.get_empty_pos():
            val_poss = set()
            ligne_tuple = list(self.grid.get_row(allPos[0]))
            colonne_tuple = list(self.grid.get_col(allPos[1]))
            region_tuple = list(self.grid.get_region(allPos[0] // 3, allPos[1] // 3))

            for i in range(1, 10):
                if i not in ligne_tuple and i not in colonne_tuple and i not in region_tuple:
                    val_poss.add(i)

            self.solutions.append((allPos, val_poss))

    def reduce_domains(self, last_i, last_j, last_v):
        raise NotImplementedError()

    def commit_one_var(self):
        raise NotImplementedError()

    def solve_step(self):
        raise NotImplementedError()

    def is_valid(self):
        raise NotImplementedError()

    def is_solved(self):
        raise NotImplementedError()

    def branch(self):
        raise NotImplementedError()

    def solve(self):
        raise NotImplementedError()
