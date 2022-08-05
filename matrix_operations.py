from matrix import Matrix
from copy import deepcopy
from helper import *

def add_row(matrix, idx, new_row):
    """Adds a row to matrix at given index."""
    elements = matrix.elements
    if len(new_row) != len(elements[0]):
        return 
    elements.insert(idx, new_row)
    return Matrix(elements=elements)


def remove_row(matrix, idx):
    """Removes a row from matrix at given index."""
    elements = deepcopy(matrix.elements)
    del elements[idx]
    return Matrix(elements=elements)


def replace_row(matrix, idx, new_row):
    """Replaces row at given index."""
    elements = deepcopy(matrix.elements)
    if len(new_row) != len(elements[0]):
        return 
    del elements[idx]
    elements.insert(idx, new_row)
    return Matrix(elements=elements)


def add_column(matrix, idx, new_column):
    """Adds a column to matrix at given index."""
    elements = deepcopy(matrix.elements)
    if len(new_column) != len(elements):
        return 
    for i in range(len(new_column)):
        row = elements[i]
        row.insert(idx, new_column[i])
    return Matrix(elements=elements)


def remove_column(matrix, idx):
    """Removes a column from matrix at given index."""
    elements = deepcopy(matrix.elements)
    for i in range(len(elements)):
        row = elements[i]
        del row[idx]
    return Matrix(elements=elements)


def replace_column(matrix, idx, new_column):
    """Replaces column at given index."""
    elements = deepcopy(matrix.elements)
    if len(new_column) != len(elements):
        return 
    for i in range(len(new_column)):
        row = elements[i]
        del row[idx]
        row.insert(idx, new_column[i])
    return Matrix(elements=elements)


def extract_column(matrix, column):
    """Extract columns at given index."""
    # Check if legal column
    num_columns = len(matrix.elements[0])
    if num_columns <= column:
        return 
    return [row[column] for row in matrix.elements]


def transpose(matrix):
    """Returns tranposed matrix."""
    t_rows = matrix.columns
    t_columns = matrix.rows
    t_elements = [[0 for i in range(t_columns)] for j in range(t_rows)]
    for i in range(matrix.rows): 
        for j in range(matrix.columns): 
            t_elements[j][i] = matrix.elements[i][j]
    return Matrix(elements=t_elements)


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