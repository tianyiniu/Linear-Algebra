import matplotlib.pyplot as plt
from regression import *
from helper import linspace

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
    #coeffs = least_squares(coordinates, 2)
    deg, coeffs = best_degree(coordinates)

    # Setting graph axes
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.title(f"Function coefficients: {coeffs}")

    # Plot points
    for x_val, y_val in coordinates: 
        plt.plot(x_val, y_val, marker="+", markersize=5)

    # Generates x, y values for function plot
    x = linspace(-5,5,50)
    y = [polynomial(num, coeffs) for num in x] 
    # Plot function
    plt.plot(x, y, "blue")

    # Display plot
    plt.show()