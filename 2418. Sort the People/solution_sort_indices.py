class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        indices = list(range(len(names)))
        indices.sort(key=lambda i: -heights[i])
        
        return [names[i] for i in indices]
