class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj_mat = { i: [] for i in range(n) }

        for parent, child in edges:
            adj_mat[parent].append(child)
            adj_mat[child].append(parent)
        
        def dfs(curr, parent):
            time = 0

            for child in adj_mat[curr]:
                if child == parent:
                    continue
                
                child_time = dfs(child, curr)

                if child_time or hasApple[child]:
                    time += child_time + 2
            
            return time
        
        return dfs(0, -1)
