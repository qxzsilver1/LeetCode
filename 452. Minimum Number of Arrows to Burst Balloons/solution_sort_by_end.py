class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key= lambda x: x[1])

        res = 1

        prev_end = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] > prev_end:
                prev_end = points[i][1]
                res += 1

        return res
