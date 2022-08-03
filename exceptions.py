class MultiplicationSizeException(Exception):
    def __init__(self, Lmatrix, Rmatrix, message=None): 
        self.message = message if message else None
        self.Lmatrix = Lmatrix
        self.Rmatrix = Rmatrix
    
    def __str__(self): 
        Lsize = f"{self.Lmatrix.rows}x{self.Lmatrix.columns}"
        Rsize = f"{self.Rmatrix.rows}x{self.Rmatrix.columns}"
        if self.message:
            return f"{self.message}\nMatrix incorrect size: Left {Lsize} Right {Rsize}"
        else: 
            return f"Matrix incorrect size: Left {Lsize} Right {Rsize}"


class DotProductException(Exception):
    def __init__(self, vec1, vec2):
        self.vec1 = vec1
        self.vec2 = vec2
    
    def __str__(self):
        return f"Dot product undefined, vector different sizes\nLeft: {len(self.vec1)} Right: {len(self.vec2)}"