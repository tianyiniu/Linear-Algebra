import matplotlib.pyplot as plt
from regression import *
from helper import linspace

if __name__ == "__main__":

    coordinates = [(-1, 2), (0, 1), (1, 2), (2, 3)]
    coeffs = least_squares(coordinates, 2)
    #deg, coeffs = best_degree(coordinates)

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