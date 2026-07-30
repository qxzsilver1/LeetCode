class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)

        for prereq, course in prerequisites:
            adj_list[course].append(prereq)
        
        prereq_map = {}

        def dfs(node):
            if node not in prereq_map:
                prereq_map[node] = set()

                for prereq in adj_list[node]:
                    prereq_map[node] |= dfs(prereq)
                
                prereq_map[node].add(node)

            return prereq_map[node]
        
        for course in range(numCourses):
            dfs(course)
        
        res = []

        for u, v in queries:
            res.append(u in prereq_map[v])
        
        return res
