class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        n_total = m + n
        left_partition_size = (n_total + 1) // 2
        lo = 0
        hi = m

        while lo <= hi:
            mid_1 = (lo + hi) // 2
            mid_2 = left_partition_size - mid_1

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid_1 < m:
                r1 = nums1[mid_1]
            if mid_2 < n:
                r2 = nums2[mid_2]
            if mid_1 - 1 >= 0:
                l1 = nums1[mid_1 - 1]
            if mid_2 - 1 >= 0:
                l2 = nums2[mid_2 - 1]
            
            if l1 <= r2 and l2 <= r1:
                if n_total % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                hi = mid_1 - 1
            else:
                lo = mid_1 + 1
        
        return -1
