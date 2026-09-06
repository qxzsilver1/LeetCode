class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        curr_floor = 0

        res = 0

        for floor in requests:
            if curr_floor == floor:
                continue
            
            res += abs(curr_floor - floor)
            curr_floor = floor
        
        return res
