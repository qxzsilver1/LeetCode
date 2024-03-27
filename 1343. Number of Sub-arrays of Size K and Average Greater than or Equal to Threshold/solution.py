class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = sum(arr[0:k]) / k
        res = 1 if avg >= threshold else 0

        l = 0

        for r in range(k, len(arr)):
            avg = (avg * k - arr[l] + arr[r]) / k
            
            if avg >= threshold:
                res += 1
            
            l += 1
            r += 1
        
        return res
