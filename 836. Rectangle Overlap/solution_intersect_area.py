class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        def intersect(p1_left, p1_right, p2_left, p2_right):
            return min(p1_right, p2_right) > max(p1_left, p2_left)
        
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2])) and (intersect(rec1[1], rec1[3], rec2[1], rec2[3]))
