import numpy as np


class matrix():
    def __init__(self, elements):
        
        self.elements = elements
        self.elementst = np.transpose(elements)
        
        self.row1 = elements[0]
        self.row2 = elements[1]
        self.row3 = elements[2]
        
        self.col1 = self.elementst[0]
        self.col2 = self.elementst[1]
        self.col3 = self.elementst[2]

    def no_of_rows(self):
        return len(self.elements)

    def __str__(self):
        elements=self.elements
        x="\n"
        for i in range(3):
            x+="| "
            for j in range(3):
                x+=str(elements[i,j])+" "
            x+="|\n"
            
        return x
    
    def __add__(self, m):
        return np.add(self.elements,m.elements)

x = np.array([[1, 2, 3],
              [3, 4, 5],
              [5, 6, 7]])

matrix1 = matrix(x)
matrix2 = matrix(x)

# print(matrix1.no_of_rows(), matrix1.col1,x,matrix1)
print(matrix1)
matrix3=matrix(matrix1+matrix2)
print(matrix3)

