class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque([nums[0]])
        dec = deque([nums[0]])
        
        res = 1
        
        j = 0

        for i in range(1, len(nums)):
            while inc and inc[-1] > nums[i]:
                inc.pop()
            while dec and dec[-1] < nums[i]:
                dec.pop()

            inc.append(nums[i])
            dec.append(nums[i])

            if dec[0] - inc[0] > limit:
                if dec[0] == nums[j]:
                    dec.popleft()
                if inc[0] == nums[j]:
                    inc.popleft()
                
                j += 1

        return len(nums) - j
