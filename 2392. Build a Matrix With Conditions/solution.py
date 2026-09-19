class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def dfs(src, adj_list, visited, path, order):
            if src in path:
                return False
            
            if src in visited:
                return True
            
            visited.add(src)
            path.add(src)

            for nei in adj_list[src]:
                if not dfs(nei, adj_list, visited, path, order):
                    return False


            path.remove(src)
            order.append(src)

            return True

        def topoSort(edges):
            adj_list = defaultdict(list)

            for src, dst in edges:
                adj_list[src].append(dst)
            
            visited = set()
            path = set()
            order = []
            
            for src in range(1, k + 1):
                if not dfs(src, adj_list, visited, path, order):
                    return []
            
            return order[::-1]

        row_order = topoSort(rowConditions)
        col_order = topoSort(colConditions)

        if not row_order or not col_order:
            return []
        
        val_to_row = { n: i for i, n in enumerate(row_order) }
        val_to_col = { n: i for i, n in enumerate(col_order) }
        
        res = [[0] * k for _ in range(k)]

        for num in range(1, k + 1):
            r, c = val_to_row[num], val_to_col[num]
            res[r][c] = num
        
        return res
