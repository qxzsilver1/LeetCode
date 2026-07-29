class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        res = 0

        def dfs(node):
            isConnected[node][node] = 0

            for nei in range(n):
                if node != nei and isConnected[node][nei] and isConnected[nei][nei]:
                    dfs(nei)
        
        for i in range(n):
            if isConnected[i][i]:
                dfs(i)
                res += 1
        
        return res
