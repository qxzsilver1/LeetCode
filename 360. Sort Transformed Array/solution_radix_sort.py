class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            res[i] = a * num * num + b * num + c
        
        max_elem = nums[0]

        for num in res:
            max_elem = max(abs(num), max_elem)
        
        max_digits = 0

        while max_elem > 0:
            max_digits += 1
            max_elem /= 10
        
        place_val = 1

        def radixSort():
            map_digits = [[] for i in range(10)]

            for num in res:
                digit = abs(num) / place_val
                digit = int(digit % 10)
                map_digits[digit].append(num)
            
            idx = 0

            for digit in range(10):
                for num in map_digits[digit]:
                    res[idx] = num
                    idx += 1
            
        for _ in range(max_digits):
            radixSort()
            place_val *= 10
        
        positives = [num for num in res if num >= 0]
        negatives = [num for num in res if num < 0]
        negatives.reverse()

        res = negatives + positives
        return res
