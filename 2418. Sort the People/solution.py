class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        name_heights = list(zip(names, heights))
        
        name_heights.sort(key=lambda x: -x[1])
        
        return [x[0] for x in name_heights]
