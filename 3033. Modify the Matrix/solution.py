class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])

        answer = [[0] * COLS for _ in range(ROWS)]

        max_per_cols = [-1] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                max_per_cols[j] = max(max_per_cols[j], matrix[i][j])
        
        for i in range(ROWS):
            for j in range(COLS):
                answer[i][j] = max_per_cols[j] if matrix[i][j] == -1 else matrix[i][j]
        
        return answer
