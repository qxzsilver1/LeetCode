class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        output = []
        quad = []

        def kSum(k, start_idx, target_val):
            if k != 2:
                for i in range(start_idx, len(nums) - k + 1):
                    if i > start_idx and nums[i] == nums[i-1]:
                        continue
                    
                    quad.append(nums[i])
                    kSum(k-1, i+1, target_val - nums[i])
                    quad.pop()
                
                return
            else:
                l, r = start_idx, len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] < target_val:
                        l += 1
                    elif nums[l] + nums[r] > target_val:
                        r -= 1
                    else:
                        output.append(quad + [nums[l], nums[r]])
                        l += 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
           
        kSum(4, 0, target)
        return output
