from matrix import Matrix
from matrix_operations import transpose, extract_column
from cramers import *

def coeff_row(degree, x_value):
    """Plugs in x values for polynomial of given degree."""
    coeffs = []
    for i in range(degree):
        coeffs.append(x_value**(degree-i)) # Excludes constant term (degree - i = 0)
    coeffs.append(1)
    return coeffs 


# y = a^2x + bx + c
def least_squares(coordinates, degree): 
    "Takes in list of coordinates (tuples). Returns coefficients for best fitting polynomial of given degree."
    # TODO add check to see if enough points

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


def polynomial(x, coeffs):
    """Calculates the value of polynomial with coeffs at given value."""
    degree = len(coeffs) - 1
    return sum([coeffs[i] * x**(degree-i) for i in range(len(coeffs))])


def best_degree(coordinates, deg_start=1, deg_stop=5):
    """Finds the best degree polynomial for fit a set of points."""
    # !Might over fit
    deg_stop = min(deg_stop, len(coordinates)-1) # (Number of coordinates) - 1 determines max degree
    current_best_deg = deg_start
    current_least_squares = float("inf")
    best_coeffs = []
    for deg in range(deg_start, deg_stop+1):
        print(f"Caculating degree: {deg}")
        coeffs = least_squares(coordinates, deg)
        squares_sum = sum([(polynomial(x, coeffs) - y) ** 2 for x,y in coordinates])
        if squares_sum < current_least_squares: 
            current_least_squares = squares_sum
            current_best_deg = deg
            best_coeffs = coeffs
        print(f"Square sum: {current_least_squares} Degree: {current_best_deg} Best coeffs: {best_coeffs}")
    return current_best_deg, best_coeffs

    
if __name__ == "__main__":
    coordinates = [(-1, 2), (0, 1), (1, 2), (2, 3)]
    coordinates2 = [(0, 6), (1, 0), (2, 0)]
    print(least_squares(coordinates2, 1))
    