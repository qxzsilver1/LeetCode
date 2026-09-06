class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = [[0] * c for _ in range(r)]

        m, n = len(mat), len(mat[0])

        if m == 0 or r * c != m * n:
            return mat
        
        q = deque()

        for i in range(m):
            for j in range(n):
                q.append(mat[i][j])
        
        for i in range(r):
            for j in range(c):
                res[i][j] = q.popleft()
        
        return res
