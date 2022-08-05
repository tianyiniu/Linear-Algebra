from helper import *
from exceptions import MultiplicationSizeException, NewMatrixSizeException
DECIMAL_DIGITS = 6

class Matrix: 
    def __init__(self, rows=None, columns=None, elements=None):
        if elements == None:
            self.rows = rows
            self.columns = columns
            self.elements = [[0 for i in range(columns)] for j in range(rows)]
        else: 
            self.rows = len(elements)
            self.columns = len(elements[0])
            self.elements = elements
        
        # Check if each row has same number of elements
        for i in range(self.rows):
            if len(self.elements[i]) != self.rows: 
                raise NewMatrixSizeException(self)


    def __str__(self): 
        # Find max number digits of elements in matrix ("-", "." both count as one digit)
        max_digits = max([max([len(str(self.elements[j][i])) for i in range(self.columns)]) for j in range(self.rows)])
        matrix_str = ""
        for row in self.elements: 
            matrix_str += " ".join([str(num) + " "*(max_digits+1-len(str(num))) for num in row])
            matrix_str +="\n"
        matrix_str = matrix_str.rstrip("\n")
        return matrix_str


    def __mul__(self, other):
        """Other is B: this gives A * B."""
        # Check if matrix dimensions are correct
        if self.columns != other.rows:
            raise MultiplicationSizeException(self, other)

        result_rows = self.rows
        result_columns = other.columns
        # normal matrix should be square matrix
        result_elements = [[0 for i in range(result_columns)] for j in range(result_rows)]
        for i in range(result_rows): 
            for j in range(result_columns):
                result_elements[i][j] = dot(self.elements[i], extract_column(other, j)) 
        return Matrix(rows=result_rows, columns=result_columns, elements=result_elements)

    
    def __rmul__(self, other):
        """Defines scalar multiplication of matrices."""
        if type(other) is int or type(other) is float: 
            result_elements = [[0 for i in range(self.columns)] for j in range(self.rows)]
            for i in range(self.rows): 
                for j in range(self.columns): 
                    result_elements[i][j] = other * self.elements[i][j]
            return Matrix(elements=result_elements)
        else: 
            raise TypeError(f"Multiplication not supported between {type(other)} and matrix.") 
