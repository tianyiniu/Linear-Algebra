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
