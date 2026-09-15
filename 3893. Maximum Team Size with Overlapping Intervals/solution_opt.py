class Solution:
    def maximumTeamSize(self, startTime: list[int], endTime: list[int]) -> int:
        intervals = zip(startTime[:], endTime[:])

        res = 0

        startTime.sort()
        endTime.sort()

        for beg, end in intervals:
            l = bisect_left(endTime, beg)
            r = bisect_right(startTime, end)

            res = max(res, r - l)
        
        return res
