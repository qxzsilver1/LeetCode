class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]

        m, n = len(mat), len(mat[0])

        if m == 0 or r * c != m * n:
            return mat

        curr_row, curr_col = 0, 0

        for i in range(m):
            for j in range(n):
                res[curr_row][curr_col] = mat[i][j]

                curr_col += 1

                if curr_col == c:
                    curr_row += 1
                    curr_col = 0
        
        return res
