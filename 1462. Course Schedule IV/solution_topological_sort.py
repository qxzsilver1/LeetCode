class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = [set() for _ in range(numCourses)]
        indegrees = [0] * numCourses
        is_prereq = [set() for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj_list[prereq].add(course)
            indegrees[course] += 1
        
        q = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while q:
            node = q.popleft()

            for nei in adj_list[node]:
                is_prereq[nei].add(node)
                is_prereq[nei].update(is_prereq[node])
                indegrees[nei] -= 1

                if indegrees[nei] == 0:
                    q.append(nei)
        
        return [u in is_prereq[v] for u, v in queries]
