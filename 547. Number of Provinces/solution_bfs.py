class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n

        res = 0

        q = deque()

        for i in range(n):
            if not visited[i]:
                res += 1

                visited[i] = True

                q.append(i)

                while q:
                    node = q.popleft()

                    for nei in range(n):
                        if isConnected[node][nei] and not visited[nei]:
                            visited[nei] = True
                            q.append(nei)
        
        return res
        
        return res
