class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right= 0, len(arr)
        
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < mid:
                left = mid + 1
            else:
                right = mid
        
        return left if left < len(arr) and arr[left] == left else -1
