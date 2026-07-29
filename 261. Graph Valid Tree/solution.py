class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj_list = { i: [] for i in range(n) }

        for s, t in edges:
            adj_list[s].append(t)
            adj_list[t].append(s)
        
        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for j in adj_list[i]:
                if j == prev:
                    continue
                
                if not dfs(j, i):
                    return False

            return True
        
        return dfs(0, -1) and len(visited) == n
