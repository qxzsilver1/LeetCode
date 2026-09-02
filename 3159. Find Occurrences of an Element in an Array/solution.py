class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        num_occurrence = [-1] * len(queries)
        num_idx = []

        for i in range(len(nums)):
            if nums[i] != x:
                continue
            else:
                num_idx.append(i)
        
        if len(num_idx) == 0:
            return num_occurrence
        
        for i in range(len(queries)):
            if len(num_idx) < queries[i]:
                continue
            else:
                num_occurrence[i] = num_idx[queries[i] - 1]
        
        return num_occurrence
