class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)

        for i, eq in enumerate(equations):
            a, b = eq

            adj_list[a].append([b, values[i]])
            adj_list[b].append([a, 1 / values[i]])
        
        def bfs(src, dst):
            if src not in adj_list or dst not in adj_list:
                return -1
            
            q = deque()

            visited = set()

            q.append([src, 1])
            visited.add(src)

            while q:
                node, weight = q.popleft()

                if node == dst:
                    return weight

                for nei, w in adj_list[node]:
                    if nei not in visited:
                        q.append([nei, weight * w])
                        visited.add(nei)
            
            return -1


        return [bfs(q[0], q[1]) for q in queries]
