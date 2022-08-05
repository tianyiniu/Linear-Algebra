from matrix import Matrix
from matrix_operations import * 
from helper import *
from exceptions import ZeroDetException

def solve_cramers(coef_matrix, const_terms):
    """Uses Cramer's rule to solve a system of linear equations. Raises ZeroDetException if unsolvable."""
    if not is_square(coef_matrix):
        print("Matrix not square")
        return []
    elif len(coef_matrix.elements) != len(const_terms):
        print("Number of constant terms not correct")
        return []

    detA = determinant(coef_matrix)
    
    if detA == 0: 
        raise ZeroDetException(coef_matrix)
    
    solution_set = []
    for i in range(len(const_terms)):
        sol_matrix = replace_column(coef_matrix, i, const_terms)
        solution = round(determinant(sol_matrix)/detA, 5)
        solution_set.append(solution)
    return solution_set


if __name__ == "__main__":
    elements = [[1, 4, 2, 1], [-1, -1, 3, 2], [0, 5, 7, -4], [2, 1, -3, 2]]
    elements2 = [[1, 2, -1], [0, 2, 2], [2, 1, 3]]
    const_terms = [2, 1, -4]
    matrix = Matrix(elements=elements2)
    cramers_solution_set = solve_cramers(matrix, const_terms)
    print(cramers_solution_set)