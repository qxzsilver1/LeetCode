class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []

        for idx, val in enumerate(nums):
            if val != 0:
                self.pairs.append([idx, val])

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        v1, v2 = 0, 0

        while v1 < len(self.pairs) and v2 < len(vec.pairs):
            if self.pairs[v1][0] == vec.pairs[v2][0]:
                res += self.pairs[v1][1] * vec.pairs[v2][1]
                v1 += 1
                v2 += 1
            elif self.pairs[v1][0] < vec.pairs[v2][0]:
                v1 += 1
            else:
                v2 += 1
        
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
