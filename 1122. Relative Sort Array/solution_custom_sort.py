class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {num: i for i, num in enumerate(arr2)}
        return sorted(arr1, key=lambda x: (index.get(x, 1000 + x)))
