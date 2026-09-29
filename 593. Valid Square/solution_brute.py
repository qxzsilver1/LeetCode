class Solution:
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        def dist(p_a, p_b):
            return (p_a[0] - p_b[0]) ** 2 + (p_a[1] - p_b[1]) ** 2
        
        def check(p1, p2, p3, p4):
            return dist(p1, p2) > 0 and dist(p1, p2) == dist(p2, p3) and dist(p2, p3) == dist(p3, p4) and dist(p3, p4) == dist(p4, p1) and dist(p1, p3) == dist(p2, p4)
        
        def checkAllPermutations(p, l):
            if l == 4:
                return check(p[0], p[1], p[2], p[3])
            else:
                res = False
                for i in range(l, 4):
                    p[l], p[i] = p[i], p[l]
                    res |= checkAllPermutations(p, l + 1)
                    p[l], p[i] = p[i], p[l]
                return res
        
        p = [p1, p2, p3, p4]
        all_dists = [dist(p[i], p[(i + 1) % 4]) for i in range(4)]
        all_dists += [dist(p[i], p[(i + 2) % 4]) for i in range(4)]

        return len(set(all_dists)) == 2 and min(all_dists) != 0 and checkAllPermutations(p, 0)
