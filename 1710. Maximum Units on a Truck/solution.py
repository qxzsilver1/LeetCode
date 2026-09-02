class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        q = deque(sorted(boxTypes, key= lambda x: x[1], reverse=True))

        units_count = 0

        while len(q) != 0:
            curr_box = q.popleft()
            box_cnt = min(truckSize, curr_box[0])
            units_count += box_cnt * curr_box[1]
            truckSize -= box_cnt

            if truckSize == 0:
                break
        
        return units_count
