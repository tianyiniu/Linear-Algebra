from matrix import Matrix
from copy import deepcopy 
DECIMAL_DIGITS = 5

def get_num_leading_zeros(row):
    """Returns number of leading zeros in row."""
    num = 0
    for element in row:
        if element == 0:
            num += 1
        else: 
            return num
    return num 


def reorganize(matrix=None, row=0):
    """Reorganize matrix by reverse order of leading zeros. (Upper triangular form)."""
    matrix.elements = sorted(matrix.elements, key=lambda x: get_num_leading_zeros(x))
    return matrix


def find_pivot(matrix=None, current_pivot=(0, 0)):
    """Returns coordinate of next pivot. This function is responible for returning (-1,-1) if no further pivots."""
    rows = matrix.rows
    columns = matrix.columns
    if current_pivot[0] == rows-1 or current_pivot[1] == columns-1:
        return (-1, -1)

    current_row = current_pivot[0]+1
    current_column = current_pivot[1]+1
    row = matrix.elements[current_row]
    for j in range(current_column, columns): 
        if row[j] != 0:
            current_column = j 
            return (current_row, current_column)
    return (-1, -1)


def gauss_elim(matrix=None):
    matrix = deepcopy(matrix)
    reorganize(matrix)
    pivot = (0, 0)
    pivot_element = matrix.elements[pivot[0]][pivot[1]]
    while pivot != (-1, -1): 
        for i in range(pivot[0]+1, matrix.rows):
            for j in range(pivot[1]+1, matrix.columns):
                a = matrix.elements[i][pivot[1]]
                b = matrix.elements[pivot[0]][j]
                matrix.elements[i][j] = matrix.elements[i][j] - round((a*b)/pivot_element, DECIMAL_DIGITS)

        # Set all elements below pivot to 0
        for i in range(pivot[0]+1, matrix.rows):
            matrix.elements[i][pivot[1]] = 0
        
        reorganize(matrix)
        pivot = find_pivot(matrix, pivot)
        pivot_element = matrix.elements[pivot[0]][pivot[1]]

    return matrix
