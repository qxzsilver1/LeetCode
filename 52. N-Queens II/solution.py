class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diags = set() # (r + c) constant
        neg_diags = set() # (r - c) constant

        res = 0

        def backtrack(r):
            if r == n:
                nonlocal res
                res += 1

            for c in range(n):
                if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                    continue
                
                cols.add(c)
                pos_diags.add(r + c)
                neg_diags.add(r - c)
                
                backtrack(r+1)

                cols.remove(c)
                pos_diags.remove(r + c)
                neg_diags.remove(r - c)
        
        backtrack(0)

        return res
