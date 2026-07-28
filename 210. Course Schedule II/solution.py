class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = { i: [] for i in range(numCourses) }

        for course, prereq in prerequisites:
            prereq_map[course].append(prereq)
        
        res = []

        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False
            
            if course in visited:
                return True
            
            cycle.add(course)

            for prereq in prereq_map[course]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            res.append(course)

            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res
