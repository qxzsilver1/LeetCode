class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        max_per_cols = [-1] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                max_per_cols[j] = max(max_per_cols[j], matrix[i][j])
        
        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == -1:
                    matrix[i][j] = max_per_cols[j] 
        
        return matrix
