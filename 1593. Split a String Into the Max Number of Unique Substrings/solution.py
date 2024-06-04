class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        res = 0

        n = len(s)
        visited = set()

        def dfs(i):
            nonlocal res

            if len(visited) + n - i <= res:
                return
            
            if i == n:
                res = len(visited)
                return
            
            for j in range(i, n + len(visited) - res):
                substr = ''.join([s[k] for k in range(i, min(j+1, n))])

                if substr not in visited:
                    visited.add(substr)

                    dfs(j+1)

                    visited.remove(substr)
        
        dfs(0)

        return res
