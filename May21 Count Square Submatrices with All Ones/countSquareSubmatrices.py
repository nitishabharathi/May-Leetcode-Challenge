class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        row , col = len(matrix) , len(matrix[0])
        result = 0
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        result += 1
                    else:
                        val = min(matrix[r-1][c-1],matrix[r-1][c],matrix[r][c-1])+1
                        result += val
                        matrix[r][c] = val
        return result
                        
