class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        node_safety = {}

        res = []

        def dfs(i):
            if i in node_safety:
                return node_safety[i]
            
            node_safety[i] = False

            for nei in graph[i]:
                if not dfs(nei):
                    return node_safety[i] # will always be false by default
            
            node_safety[i] = True
            return node_safety[i]

        for i in range(n):
            if dfs(i):
                res.append(i)
        
        return res
