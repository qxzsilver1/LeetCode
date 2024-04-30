class DetectSquares:

    def __init__(self):
        self.point_counter = defaultdict(int)
        self.points_list = []

    def add(self, point: List[int]) -> None:
        self.point_counter[tuple(point)] += 1
        self.points_list.append(point)

    def count(self, point: List[int]) -> int:
        res = 0

        p_x, p_y = point

        for x, y in self.points_list:
            if(abs(p_y - y) != abs(p_x - x)) or x == p_x or y == p_y:
                continue
            
            res += self.point_counter[(x, p_y)] * self.point_counter[(p_x, y)]
        
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
