class Bucket:
    def __init__(self):
        self.used = False
        self.min_val = float('inf')
        self.max_val = float('-inf')

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        min_idx, max_idx = min(nums), max(nums)

        bucket_size = max(1, (max_idx - min_idx) // (len(nums) - 1))
        bucket_num = (max_idx - min_idx) // bucket_size + 1
        buckets = [Bucket() for _ in range(bucket_num)]

        for num in nums:
            idx = (num - min_idx) // bucket_size

            buckets[idx].used = True
            buckets[idx].min_val = min(num, buckets[idx].min_val)
            buckets[idx].max_val = max(num, buckets[idx].max_val)
        
        prev_bucket_max = min_idx

        max_gap = 0

        for bucket in buckets:
            if not bucket.used:
                continue
            
            max_gap = max(max_gap, bucket.min_val - prev_bucket_max)
            prev_bucket_max = bucket.max_val
        
        return max_gap
