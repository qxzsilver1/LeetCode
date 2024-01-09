class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = dict()
        output, max_count = 0, 0

        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

            output = n if counts[n] > max_count else output
            max_count = max(counts[n], max_count)
        
        return output
