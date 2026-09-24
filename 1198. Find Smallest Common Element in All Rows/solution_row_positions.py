class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])
        
        pos = [0] * n
        cur_max, cnt = 0, 0

        while True:
            for i in range(n):
                while pos[i] < m and mat[i][pos[i]] < cur_max:
                    pos[i] += 1
                if pos[i] >= m:
                    return -1
                if mat[i][pos[i]] != cur_max:
                    cnt = 1
                    cur_max = mat[i][pos[i]]
                else:
                    cnt += 1
                    if cnt == n:
                        return cur_max
