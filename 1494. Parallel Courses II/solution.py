from itertools import combinations

class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        self.graph = defaultdict(list)
        self.n = n
        self.k = k
        in_degrees = [0] * n

        for prev_course, next_course in relations:
            in_degrees[next_course - 1] += 1
            self.graph[prev_course - 1].append(next_course - 1)
        
        # bit_mask = (1 << n) - 1 # least significant to most significant bit represents the course indices that have NOT been visited (taken) if 1, and visited (taken) if 0

        return self.traverse((1 << self.n) - 1, tuple(in_degrees))
    
    @lru_cache(None)
    def traverse(self, mask, in_degrees):
        if not mask:
            return 0
        
        res = float('inf')
        courses = [i for i in range(self.n) if mask & 1 << i and in_degrees[i] == 0] # get all non-visited courses in bitmask

        for k_courses in combinations(courses, min(self.k, len(courses))):
            new_mask, new_in_degrees = mask, list(in_degrees)
            
            for course in k_courses:
                new_mask ^= 1 << course

                for child in self.graph[course]:
                    new_in_degrees[child] -= 1

            res = min(res, 1 + self.traverse(new_mask, tuple(new_in_degrees)))
        return res
