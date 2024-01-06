class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m = len(nums1)
        n = len(nums2)
        
        start = 0
        end = m
        
        while start <= end:
            partition_nums1 = (start + end) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1
            
            max_L_nums1 = nums1[partition_nums1 - 1] if partition_nums1 > 0 else -sys.maxsize
            min_R_nums1 = nums1[partition_nums1] if partition_nums1 < m else sys.maxsize
            
            max_L_nums2 = nums2[partition_nums2 - 1] if partition_nums2 > 0 else -sys.maxsize
            min_R_nums2 = nums2[partition_nums2] if partition_nums2 < n else sys.maxsize
            
            if (max_L_nums1 <= min_R_nums2) and (max_L_nums2 <= min_R_nums1):
                
                if (m+n) % 2 == 0:
                    return (max(max_L_nums1, max_L_nums2) + min(min_R_nums1, min_R_nums2)) / 2
                else:
                    return max(max_L_nums1, max_L_nums2)
            elif max_L_nums1 > min_R_nums2:
                end = partition_nums1 - 1
            else:
                start = partition_nums1 + 1
        
        return -1
