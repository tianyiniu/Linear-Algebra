from exceptions import DotProductException

def dot(lst1, lst2):
    """Returns the dot product between two vectors."""
    if len(lst1) != len(lst2): 
        raise DotProductException(lst1, lst2)
    return sum([lst1[i] * lst2[i] for i in range(len(lst1))])


def is_even(num) -> bool:
    """Check if number is even."""
    return num % 2 == 0


def is_square(matrix):
    """Check if matrix is square."""
    return matrix.rows == matrix.columns


def square_matrix_size(matrix):
    """Returns size of square matrix"""
    return matrix.rows


def linspace(start, stop, n):
    """Generates list of n linearly spaced numbers on given interval."""
    step = (stop - start) / n
    return [start + i * step for i in range(n)]


def extract_column(matrix, column_idx):
    """Extract column from matrix."""
    # Check if legal column
    return [row[column_idx] for row in matrix.elements]