class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        k = 5

        items.sort(key = lambda x: (x[0], - x[1]))

        res = []

        n = len(items)

        i = 0

        while i < n:
            student_id = items[i][0]

            sum_val = 0

            for j in range(i, i + k):
                sum_val += items[j][1]
            
            while i < n and items[i][0] == student_id:
                i += 1
            
            res.append([student_id, sum_val // k])
        
        return res
