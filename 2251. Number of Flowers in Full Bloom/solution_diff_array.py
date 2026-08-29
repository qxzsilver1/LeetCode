class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        diff_array = SortedDict({0: 0})

        for start, end in flowers:
            diff_array[start] = diff_array.get(start, 0) + 1
            diff_array[end + 1] = diff_array.get(end + 1, 0) - 1
        
        positions = []
        prefix = []

        curr = 0

        for k, v in diff_array.items():
            positions.append(k)
            curr += v
            prefix.append(curr)
        
        res = []

        for p in people:
            i = bisect_right(positions, p) - 1
            res.append(prefix[i])
        
        return res
