def dot(lst1, lst2):
    if len(lst1) != len(lst2): 
        print("*** Dot product undefined: Lists are not equal length ***")
        return 
    length = len(lst1)
    return sum([lst1[i] * lst2[i] for i in range(length)])


def is_even(num):
    return num % 2 == 0


def is_square(matrix):
    return len(matrix.elements) == len(matrix.elements[0])


def square_matrix_size(matrix):
    return len(matrix.elements)


def linspace(start, stop, n):
    """Generates list of n linearly spaced number w.r.t. given interval."""
    step = (stop - start) / n
    return [start + i * step for i in range(n)]