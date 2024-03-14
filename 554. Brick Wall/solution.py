class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gaps = dict()

        n = len(wall)
        row_len = sum(wall[0])


        for row in wall:
            curr_pos = 0

            for i in row:
                curr_pos += i
                if curr_pos < row_len:
                    count_gaps[curr_pos] = count_gaps.get(curr_pos, 0) + 1
        
        return n - max(count_gaps.values()) if len(count_gaps) > 0 else n
