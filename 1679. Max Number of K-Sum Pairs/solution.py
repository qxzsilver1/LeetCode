class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        elem_complements = defaultdict(int)

        cnt = 0

        for i in range(len(nums)):
            curr = nums[i]
            complement = k - curr

            if elem_complements[complement] > 0:
                elem_complements[complement] -= 1
                cnt += 1
            else:
                elem_complements[curr] += 1
        
        return cnt
