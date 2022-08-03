from matrix import Matrix
from matrix_operations import * 
from helper import *

def determinant(matrix):
    """Find determinant of matrix. Assumes matrix is square."""
    matrix_size = square_matrix_size(matrix)
    if matrix_size == 1:
        det = matrix.elements[0][0]
    elif matrix_size == 2:
        det = matrix.elements[0][0]*matrix.elements[1][1] - matrix.elements[0][1]*matrix.elements[1][0]
    else: 
        det = 0
        first_row = matrix.elements[0] # TODO optimize row/column selection for efficiency
        for idx, element in enumerate(first_row):
            sign = 1 if is_even(idx) else -1
            cofactor_matrix = remove_column(remove_row(matrix, 0), idx)
            det += sign * element * determinant(cofactor_matrix)
    return det


def solve_cramers(coef_matrix, const_terms):
    """Uses Cramer's rule to solve a system of linear equations. Returns a list of solutions if solvable, empty list otherwise."""
    if not is_square(coef_matrix):
        print("Matrix not square")
        return []
    elif len(coef_matrix.elements) != len(const_terms):
        print("Number of constant terms not correct")
        return []

    detA = determinant(coef_matrix)
    
    if detA == 0: 
        print("Unsolvable, determinant is zero.")
        return []
    
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