#-*-coding: utf8-*-

class SudokuSolver:

    def __init__(self, grid):
        raise NotImplementedError()

    def reduce_all_domains(self):
        raise NotImplementedError()

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
