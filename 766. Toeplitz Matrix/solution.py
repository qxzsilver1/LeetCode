class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if r <= c and matrix[r][c] != matrix[0][c-r]:
                    return False
                
                if r > c and matrix[r][c] != matrix[r-c][0]:
                    return False
        
        return True
