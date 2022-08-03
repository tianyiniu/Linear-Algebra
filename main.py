import matplotlib.pyplot as plt
from regression import *
from helper import linspace

def polynomial(x, coeffs):
    degree = len(coeffs) - 1
    return sum([coeffs[i] * x**(degree-i) for i in range(len(coeffs))])


if __name__ == "__main__":

    coordinates = [(-1, 2), (0, 1), (1, 2), (2, 3)]
    coordinates2 = [(0, 6), (1, 0), (2, 0)]
    coeffs = least_squares(coordinates2, 1)

    # Generates values
    x = linspace(-5,5,50)
    y = [polynomial(num, coeffs) for num in x]

    # setting the axes at the center
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Plot points
    for x_val, y_val in coordinates: 
        plt.plot(x_val, y_val, marker="+", markersize=5)
    # Plot function
    plt.plot(x,y, 'blue')


    # show the plot
    plt.show()