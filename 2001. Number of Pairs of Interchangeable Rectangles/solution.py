class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        interchangeable_dict = {}

        for rectangle in rectangles:
            ratio = rectangle[0]/rectangle[1]
            interchangeable_dict[ratio] = 1 + interchangeable_dict.get(ratio, 0)
        
        res = 0

        for _, val in interchangeable_dict.items():
            res += val * (val - 1) // 2
        

        return res
