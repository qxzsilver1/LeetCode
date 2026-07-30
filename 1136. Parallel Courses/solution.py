class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = {i : [] for i in range(1, n+1)}
        indegrees = {i: 0 for i in range(1, n+1)}

        for s, t in relations:
            adj_list[s].append(t)
            indegrees[t] += 1
        
        q = []

        for node in adj_list:
            if indegrees[node] == 0:
                q.append(node)
        
        semester = 0
        studied_num = 0

        while q:
            semester += 1
            next_q = []

            for node in q:
                studied_num += 1
                next_courses = adj_list[node]

                for next_course in next_courses:
                    indegrees[next_course] -= 1

                    if indegrees[next_course] == 0:
                        next_q.append(next_course)
            
            q = next_q
        
        return semester if studied_num == n else -1
