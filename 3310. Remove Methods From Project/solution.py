class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(n)]
        indegrees = [0] * n

        for u, v in invocations:
            adj_list[u].append(v)
            indegrees[v] += 1
        
        q = deque([k])
        suspicious = [0] * n
        suspicious[k] = 1

        while q:
            u = q.popleft()

            for v in adj_list[u]:
                indegrees[v] -= 1

                if suspicious[v] == 0:
                    q.append(v)
                    suspicious[v] = 1
        
        can_remove_all = True

        for i in range(n):
            if suspicious[i] == 1 and indegrees[i] > 0:
                can_remove_all = False
                return list(range(n))
        
        return [i for i in range(n) if suspicious[i] == 0]
        
