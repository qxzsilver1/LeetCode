class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        def dist(p_a, p_b):
            return (p_a[0] - p_b[0]) ** 2 + (p_a[1] - p_b[1]) ** 2
        
        def check(p1, p2, p3, p4):
            return dist(p1, p2) > 0 and dist(p1, p3) > 0 and dist(p1, p2) == dist(p2, p3) and dist(p2, p3) == dist(p3, p4) and dist(p3, p4) == dist(p4, p1) and dist(p1, p3) == dist(p2, p4)
        
        return check(p1, p2, p3, p4) or check(p1, p3, p2, p4) or check(p1, p2, p4, p3)
