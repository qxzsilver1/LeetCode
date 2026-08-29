class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        k = 5

        all_scores = defaultdict(list)

        for item in items:
            student_id = item[0]
            score = item[1]
            heapq.heappush(all_scores[student_id], -score)
        
        res = []

        for student_id in sorted(all_scores.keys()):
            curr_sum = 0

            for i in range(k):
                curr_sum += - heapq.heappop(all_scores[student_id])
            
            res.append([student_id, curr_sum // k])
        
        return res
