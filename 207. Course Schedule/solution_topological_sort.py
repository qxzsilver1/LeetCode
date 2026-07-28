class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses

        adj_list = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegrees[dst] += 1
            adj_list[src].append(dst)
        
        q = deque()

        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)
        
        ctr = 0

        while q:
            node = q.popleft()
            ctr += 1

            for neighbor in adj_list[node]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        return ctr == numCourses
