class Solution:
    def findSpecialNodes(self, n: int, edges: List[List[int]]) -> str:
        indegrees = [0] * n

        res = []

        for u, v in edges:
            indegrees[u] += 1
            indegrees[v] += 1
        
        for i in range(len(indegrees)):
            if indegrees[i] == 1:
                indegrees[i] = str(indegrees[i])
            else:
                indegrees[i] = '0'
        
        return ''.join(indegrees)
