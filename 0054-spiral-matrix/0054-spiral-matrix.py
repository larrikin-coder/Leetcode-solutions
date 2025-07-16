class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row, col = len(matrix),len(matrix[0])
        lst = []
        top,bottom = 0,row-1
        left,right = 0 , col-1
        while top <= bottom and left <= right:
            #top left to right traversal
            for j in range(left,right+1):
                lst.append(matrix[top][j])
            top += 1
            #top to bottom traversal
            for j in range(top,bottom+1):
                lst.append(matrix[j][right])
            right -=1
            #for left to right traversal
            if top <= bottom:
                for j in range(right,left-1,-1):
                    lst.append(matrix[bottom][j])
                bottom -= 1
            if left <= right:
                for j in range(bottom,top-1,-1):
                    lst.append(matrix[j][left])
                left += 1
            
        return lst


