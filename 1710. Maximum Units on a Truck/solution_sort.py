class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key= lambda x: -x[1])

        units_count = 0

        for box_type in boxTypes:
            box_cnt = min(truckSize, box_type[0])
            units_count += box_cnt * box_type[1]
            truckSize -= box_cnt

            if truckSize == 0:
                break
        
        return units_count
