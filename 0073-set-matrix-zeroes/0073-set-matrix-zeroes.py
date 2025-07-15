class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows , cols = len(matrix), len(matrix[0])
        zero_rows = set()
        zero_cols = set()                
        #find the row ,colindices
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)
        
        for r in zero_rows:
            for i in range(cols):
                matrix[r][i] = 0
         
        for c in zero_cols:
            for j in range(rows):
                matrix[j][c] = 0
        print(matrix)
        return matrix
        