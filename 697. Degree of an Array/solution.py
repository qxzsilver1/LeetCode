class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count_dict = defaultdict(list)

        for i, n in enumerate(nums):
            count_dict[n].append(i)
        
        degree, smallest_len = -1, len(nums) + 1
        
        for k, v in count_dict.items():
            
            if len(v) > degree:
                degree = len(v)
                smallest_len = v[-1] - v[0] + 1
            elif len(v) == degree and v[-1] - v[0] + 1 < smallest_len:
                smallest_len = v[-1] - v[0] + 1
        
        return smallest_len
