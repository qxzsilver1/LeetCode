class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def quadraticTransform(x):
            return a * x * x + b * x + c
        
        res = []

        l, r = 0, len(nums) - 1

        if a < 0:
            while l <= r:
                left_side_val = quadraticTransform(nums[l])
                right_side_val = quadraticTransform(nums[r])

                if left_side_val < right_side_val:
                    res.append(left_side_val)
                    l += 1
                else:
                    res.append(right_side_val)
                    r -= 1
        else:
            while l <= r:
                left_side_val = quadraticTransform(nums[l])
                right_side_val = quadraticTransform(nums[r])

                if left_side_val > right_side_val:
                    res.append(left_side_val)
                    l += 1
                else:
                    res.append(right_side_val)
                    r -= 1
            res.reverse()
        
        return res
