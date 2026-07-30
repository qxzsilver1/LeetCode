class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        res = []

        adj_matrix = [[False] * numCourses for _ in range(numCourses)]

        for prereq, course in prerequisites:
            adj_matrix[prereq][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])
        
        for u, v in queries:
            res.append(adj_matrix[u][v])
        
        return res
