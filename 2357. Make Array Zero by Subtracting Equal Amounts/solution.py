class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        curr = 0

        for n in nums:
            n -= curr

            if n > 0:
                curr += n
                count += 1
        
        return count
