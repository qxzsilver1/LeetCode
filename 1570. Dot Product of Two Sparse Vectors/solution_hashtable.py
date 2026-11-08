class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeroes = {}

        for idx, val in enumerate(nums):
            if val != 0:
                self.nonzeroes[idx] = val

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        for i, n in self.nonzeroes.items():
            if i in vec.nonzeroes:
                res += n * vec.nonzeroes[i]
        
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
