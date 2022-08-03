from matrix import Matrix
from matrix_operations import transpose, extract_column
from cramers import *

def coeff_row(degree, x_value):
    """Calculates list of coefficients for polynomial of given degree."""
    coeffs = []
    for i in range(degree):
        coeffs.append(x_value**(degree-i)) # Excludes constant term (degree - i = 0)
    coeffs.append(1)
    return coeffs 

# y = a^2x + bx + c
def least_squares(coordinates, degree): 
    "Takes in list of coordinates (tuples). Returns coefficients for best fitting polynomial of given degree."
    # TODO add check to see if enough points
    # TODO Generalize function for all degree polynomials.
    x_values = [point[0] for point in coordinates]
    y_values = [point[1] for point in coordinates]
    coeff_matrix = Matrix(elements=[coeff_row(degree, x_value) for x_value in x_values])
    coeff_transposed = transpose(coeff_matrix)
    full_matrix = add_column(coeff_matrix, len(coeff_matrix.elements[0]), y_values)

    normal = coeff_transposed * full_matrix
    
    const_terms = extract_column(normal, normal.columns-1)
    normal_coeff = remove_column(normal, normal.columns-1)

    solutions = solve_cramers(normal_coeff, const_terms)
    return solutions


if __name__ == "__main__":
    coordinates = [(-1, 2), (0, 1), (1, 2), (2, 3)]
    coordinates2 = [(0, 6), (1, 0), (2, 0)]
    print(least_squares(coordinates2, 1))