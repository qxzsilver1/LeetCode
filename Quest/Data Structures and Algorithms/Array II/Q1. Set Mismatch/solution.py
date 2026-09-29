class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [0, 0]
        x, y = 0, 0
        xor = 0

        for i in range(1, n + 1):
            xor = xor ^ i ^ nums[i-1]
        
        differing_bit = 1

        while not (xor & differing_bit):
            differing_bit <<= 1

        for i in range(1, n + 1):
            if nums[i-1] & differing_bit:
                x ^= nums[i-1]
            else:
                y ^= nums[i-1]
            
            if i & differing_bit:
                x ^= i
            else:
                y ^= i
        
        for i in range(n):
            if nums[i] == x:
                res[0] = x
                res[1] = y
                return res
            
            if nums[i] == y:
                res[0] = y
                res[1] = x
                return res
