class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = { (a, b) for a, b in connections }
        neighbors = { city: [] for city in range(n) }

        visited = set()
        num_changes = 0

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        def dfs(city):
            nonlocal num_changes

            for nei in neighbors[city]:
                if nei in visited:
                    continue
                
                if (nei, city) not in edges:
                    num_changes += 1
                
                visited.add(nei)

                dfs(nei)
        
        visited.add(0)
        dfs(0)

        return num_changes
