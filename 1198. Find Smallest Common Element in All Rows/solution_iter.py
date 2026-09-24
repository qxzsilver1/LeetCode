class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        count = [0] * 10001
        n, m = len(mat), len(mat[0])

        for i in range(n):
            for j in range(m):
                count[mat[i][j]] += 1

        for k in range(1, 10001):
            if count[k] == n:
                return k

        return -1
