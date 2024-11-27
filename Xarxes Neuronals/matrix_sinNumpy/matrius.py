import random    
class Matrix:
    
    def __init__(self,rows,cols):
        self.r = rows
        self.c = cols

    def init_matrix(self):

        for i in range(0,len(self.r)):
            for j in range(0,len(self.c)):
                
                print(f'{i}.{j},\n')

                
# [[random.randint(-10,10) for i in rows] for j in cols]
        print([[random.randint(-10,10) for i in rows] for j in cols])
    
Matrix.init_matrix(4,4)
