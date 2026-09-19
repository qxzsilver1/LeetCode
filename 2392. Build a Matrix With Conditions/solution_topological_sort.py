class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def topoSort(edges):
            indegree = [0] * (k + 1)
            adj = [[] for _ in range(k + 1)]
            for u, v in edges:
                adj[u].append(v)
                indegree[v] += 1

            order = []
            q = deque()
            for i in range(1, k + 1):
                if not indegree[i]:
                    q.append(i)

            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    indegree[nei] -= 1
                    if not indegree[nei]:
                        q.append(nei)

            return order

        row_order = topoSort(rowConditions)
        if len(row_order) != k: return []

        col_order = topoSort(colConditions)
        if len(col_order) != k: return []

        res = [[0] * k for _ in range(k)]
        col_idx = [0] * (k + 1)
        
        for i in range(k):
            col_idx[col_order[i]] = i

        for i in range(k):
            res[i][col_idx[row_order[i]]] = row_order[i]
        
        return res
