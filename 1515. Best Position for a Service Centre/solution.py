class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        n = len(positions)

        if n == 1:
            return 0
        
        def dist(x, y):
            res = 0

            for x_i, y_i in positions:
                res += math.sqrt((x - x_i) ** 2 + (y - y_i) ** 2)
            
            return res
        
        x_init, y_init = 0, 0

        curr = dist(x_init, y_init)

        step = 1

        while step > 0.000001:
            f = False

            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                curr_x, curr_y = x_init + step * dx, y_init + step * dy

                if dist(curr_x, curr_y) < curr:
                    curr = dist(curr_x, curr_y)
                    x_init, y_init = curr_x, curr_y
                    f = True
            
            if not f:
                step /= 10
        
        return curr
