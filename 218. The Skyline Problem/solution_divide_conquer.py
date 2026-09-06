class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        def merge(left_skyline, right_skyline):
            res = []
            l_pos, r_pos = 0, 0
            l_prev_height, r_prev_height = 0, 0

            while l_pos < len(left_skyline) and r_pos < len(right_skyline):
                next_left_x = left_skyline[l_pos][0]
                next_right_x = right_skyline[r_pos][0]

                if next_left_x < next_right_x:
                    l_prev_height = left_skyline[l_pos][1]
                    curr_x = next_left_x
                    curr_y = max(l_prev_height, r_prev_height)
                    l_pos += 1
                elif next_left_x > next_right_x:
                    r_prev_height = right_skyline[r_pos][1]
                    curr_x = next_right_x
                    curr_y = max(l_prev_height, r_prev_height)
                    r_pos += 1
                else:
                    l_prev_height = left_skyline[l_pos][1]
                    r_prev_height = right_skyline[r_pos][1]
                    curr_x = next_left_x
                    curr_y = max(l_prev_height, r_prev_height)
                    l_pos += 1
                    r_pos += 1
                
                if not res or res[-1][1] != curr_y:
                    res.append([curr_x, curr_y])
            
            while l_pos < len(left_skyline):
                res.append(left_skyline[l_pos])
                l_pos += 1
            
            while r_pos < len(right_skyline):
                res.append(right_skyline[r_pos])
                r_pos += 1
            
            return res
        
        n = len(buildings)

        if n == 0:
            return []
        
        if n == 1:
            return [[buildings[0][0], buildings[0][2]], [buildings[0][1], 0]]
        
        left_skyline = self.getSkyline(buildings[:n//2])
        right_skyline = self.getSkyline(buildings[n//2:])

      return merge(left_skyline, right_skyline)
