class Solution:
    def arraysIntersection(self, arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
        res = []

        counts = Counter(arr1 + arr2 + arr3)

        for item in counts:
            if counts[item] == 3:
                res.append(item)
        
        return res
