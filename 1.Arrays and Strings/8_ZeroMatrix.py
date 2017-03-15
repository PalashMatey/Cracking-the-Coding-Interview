import unittest
def checkZeroMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    
    rows = []
    cols = []
    for x in range(m):
        for y in range(n):
            if matrix[x][y] == 0:
                rows.append(x)
                cols.append(y)
    
    for row in rows:
        killRow(matrix,row)
    
    for col in cols:
        killCol(matrix,col)
    
    return matrix
    
def killRow(matrix,row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
    
def killCol(matrix,col):
    for i in xrange(len((matrix))):
        matrix[i][col] = 0
    
                
class Test(unittest.TestCase):
    data = [([
            [1, 2, 3, 4, 5 , 6],
            [6, 7, 8, 9, 10, 0 ] ,
            [11, 12, 13, 14, 15, 8],
            [16, 17, 18, 19, 20, 9], 
            [21, 22, 23, 24, 25, 26]
        ],[[1, 2, 3, 4, 5, 0], 
        [0, 0, 0, 0, 0, 0],
         [11, 12, 13, 14, 15, 0],
          [16, 17, 18, 19, 20, 0],
           [21, 22, 23, 24, 25, 0]])]
    def test_zero_matrix(self):
        for [matrix,expected] in self.data:
            actual = checkZeroMatrix(matrix)
            self.assertEqual(actual,expected)
if __name__ == '__main__':
    unittest.main()
    

