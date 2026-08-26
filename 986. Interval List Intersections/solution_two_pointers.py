class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            start_1, end_1 = firstList[i]
            start_2, end_2 = secondList[j]

            start = max(start_1, start_2)
            end = min(end_1, end_2)

            if start <= end:
                res.append([start, end])
            
            if end_1 < end_2:
                i += 1
            else:
                j += 1
        
        return res
