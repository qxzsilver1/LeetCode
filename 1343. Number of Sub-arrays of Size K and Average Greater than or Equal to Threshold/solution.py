class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        running_sum = sum(arr[0:k])
        res = 1 if running_sum >= k * threshold else 0

        l = 0

        for r in range(k, len(arr)):
            running_sum = running_sum - arr[l] + arr[r]
            
            if running_sum >= k * threshold:
                res += 1
            
            l += 1
            r += 1
        
        return res
