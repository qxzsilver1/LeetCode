class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        row_ct, col_ct = Counter(), Counter()
        diag_ct, anti_diag_ct = Counter(), Counter()

        lamps = set((i, j) for i, j in lamps)

        for i, j in lamps:
            row_ct[i] += 1
            col_ct[j] += 1
            diag_ct[i-j] += 1
            anti_diag_ct[i+j] += 1

        res = [0] * len(queries)

        for k, (i, j) in enumerate(queries):
            res[k] = 1 if (row_ct[i] or col_ct[j] or diag_ct[i-j] or anti_diag_ct[i+j]) else 0
        
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if (x, y) in lamps:
                        lamps.remove((x, y))

                        row_ct[x] -= 1
                        col_ct[y] -= 1
                        diag_ct[x-y] -= 1
                        anti_diag_ct[x+y] -= 1
        
        return res
