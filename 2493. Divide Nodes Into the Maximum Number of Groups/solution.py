class Solution:
    def magnificentSets(self, n: int, edges: list[list[int]]) -> int:
        adj_list = defaultdict(list)

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)

        visited = set()
        
        def getConnectedComponent(src):
            q = deque([src])
            component = set([src])

            while q:
                node = q.popleft()

                for nei in adj_list[node]:
                    if nei in component:
                        continue
                    q.append(nei)
                    component.add(nei)
                    visited.add(nei)
            
            return component
        
        def longestPath(src):
            q = deque([(src, 1)]) # node and group pair
            dist = { src: 1 } # node -> length from src + 1

            while q:
                node, comp_length = q.popleft()

                for nei in adj_list[node]:
                    if nei in dist:
                        if dist[nei] not in (comp_length + 1, comp_length - 1): # or dist[nei] == comp_length
                            return -1
                        continue
                    q.append((nei, comp_length + 1))
                    dist[nei] = comp_length + 1
            
            return max(dist.values())

        res = 0

        for i in range(1, n + 1):
            if i in visited:
                continue
            
            visited.add(i)

            component = getConnectedComponent(i)

            max_cnt = 0

            for src in component:
                comp_length = longestPath(src)

                if comp_length == -1:
                    return -1

                max_cnt = max(max_cnt, comp_length)
            
            res += max_cnt
        

        return res
