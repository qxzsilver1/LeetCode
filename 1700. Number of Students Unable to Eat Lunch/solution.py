class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        res = len(students)

        count_types = [res - sum(students), sum(students)]

        for s in sandwiches:
            if count_types[s] > 0:
                count_types[s] -= 1
                res -= 1
            else:
                return res
        
        return res
