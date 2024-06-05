class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for n in nums:
            xor ^= n
        
        differing_bit = 1

        while not (xor & differing_bit):
            differing_bit <<= 1
        
        diff_match, not_diff_match = 0, 0

        for n in nums:
            if differing_bit & n:
                diff_match ^= n
            else:
                not_diff_match ^= n
        
        return [diff_match, not_diff_match]
