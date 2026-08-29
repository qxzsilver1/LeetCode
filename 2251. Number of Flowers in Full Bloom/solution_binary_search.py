class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []

        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)
        
        starts.sort()
        ends.sort()

        res = []

        for p in people:
            i = bisect_right(starts, p)
            j = bisect_right(ends, p)
            res.append(i - j)
        
        return res
