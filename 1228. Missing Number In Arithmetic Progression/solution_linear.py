class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)

        diff = (arr[-1] - arr[0]) // n

        exp_num = arr[0]

        for val in arr:
            if val != exp_num:
                return exp_num
            
            exp_num += diff
        
        return exp_num

