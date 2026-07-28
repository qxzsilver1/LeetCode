class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses

        adj_list = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            indegrees[dst] += 1
            adj_list[src].append(dst)
        
        q = deque()

        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)
        
        finish = 0
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            finish += 1

            for neighbor in adj_list[node]:
                indegrees[neighbor] -= 1

                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        if finish != numCourses:
            return []
        
        return res[::-1]
