class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]

        m, n = len(mat), len(mat[0])

        if m == 0 or r * c != m * n:
            return mat

        count = 0

        for i in range(m):
            for j in range(n):
                res[count // c][count % c] = mat[i][j]
                count += 1
        
        return res
