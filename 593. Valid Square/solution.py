class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        def dist(p_a, p_b):
            return (p_a[0] - p_b[0]) ** 2 + (p_a[1] - p_b[1]) ** 2
        
        if p1 == p2 == p3 == p4:
            return False
        
        all_dists = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), dist(p3, p4)]

        all_dists.sort()

        if all_dists[0] == all_dists[1] == all_dists[2] == all_dists[3]:
            if all_dists[4] == all_dists[5]:
                return True
        
        return False
