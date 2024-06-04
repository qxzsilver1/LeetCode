class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        start = 1
        end = 9

        def backtrack(i, n, curr):
            if k == len(curr) and n == 0:
                res.append(curr[:])
                return
            
            for j in range(i, end + 1):
                curr.append(j)

                backtrack(j + 1, n - j, curr)

                curr.pop()
        
        backtrack(start, n, [])

        return res
