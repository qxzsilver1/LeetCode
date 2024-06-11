class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= (1 << i)
            found_set = set([num & mask for num in nums])

            start = res | (1 << i)

            for prefix in found_set:
                if start ^ prefix in found_set:
                    res = start
                    break
        
        return res
