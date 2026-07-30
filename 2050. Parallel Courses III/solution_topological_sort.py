class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        maxTime = time[:]

        for src, dst in relations:
            adj[src - 1].append(dst - 1)
            indegree[dst - 1] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])

        while queue:
            node = queue.popleft()

            for nei in adj[node]:
                maxTime[nei] = max(maxTime[nei], maxTime[node] + time[nei])
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)

        return max(maxTime)
