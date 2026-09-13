class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dim = len(img1)

        def nonZeroCells(M):
            res = []

            for x in range(dim):
                for y in range(dim):
                    if M[x][y] == 1:
                        res.append((x, y))
            
            return res
        
        transformation_cnt = defaultdict(int)
        
        max_overlaps = 0

        img1_ones = nonZeroCells(img1)
        img2_ones = nonZeroCells(img2)

        for (x_1, y_1) in img1_ones:
            for (x_2, y_2) in img2_ones:
                vec = (x_2 - x_1, y_2 - y_1)
                transformation_cnt[vec] += 1
                max_overlaps = max(max_overlaps, transformation_cnt[vec])
        
        return max_overlaps
