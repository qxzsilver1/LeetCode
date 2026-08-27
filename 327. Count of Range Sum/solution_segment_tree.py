class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.count = 0

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cum_sum = [0]

        def build(left, right):
            root = SegmentTreeNode(cum_sum_sorted[left], cum_sum_sorted[right])

            if left == right:
                return root
            
            mid = (left + right) // 2

            root.left = build(left, mid)
            root.right = build(mid + 1, right)

            return root
        
        def update(root, val):
            if not root:
                return
            
            if root.low <= val <= root.high:
                root.count += 1
                update(root.left, val)
                update(root.right, val)
        
        def query(root, lower, upper):
            if lower <= root.low and root.high <= upper:
                return root.count
            
            if upper < root.low or root.high < lower:
                return 0
            
            return query(root.left, lower, upper) + query(root.right, lower, upper)
        
        for n in nums:
            cum_sum.append(cum_sum[-1] + n)
        
        cum_sum_sorted = sorted(list(set(cum_sum)))

        root = build(0, len(cum_sum_sorted) - 1)

        res = 0

        for val in cum_sum:
            res += query(root, val - upper, val - lower)
            update(root, val)
        
        return res
