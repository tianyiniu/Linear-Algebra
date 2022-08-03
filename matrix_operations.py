from matrix import Matrix
from copy import deepcopy

def add_row(matrix, idx, new_row):
    # !Idx may not be valid
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
    # Check if legal column
    num_columns = len(matrix.elements[0])
    if num_columns <= column:
        return 
    return [row[column] for row in matrix.elements]


def transpose(matrix):
    t_rows = matrix.columns
    t_columns = matrix.rows
    t_elements = [[0 for i in range(t_columns)] for j in range(t_rows)]
    for i in range(matrix.rows): 
        for j in range(matrix.columns): 
            t_elements[j][i] = matrix.elements[i][j]
    return Matrix(elements=t_elements)


if __name__ == "__main__":
    elements = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = Matrix(elements=elements)
    print(remove_column(matrix, 0))