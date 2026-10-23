class Solution:
    def arraysIntersection(self, arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
        i = j = k = 0

        res = []

        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i += 1; j += 1; k += 1
            else:
                smallest = min(arr1[i], arr2[j], arr3[k])

                if arr1[i] == smallest:
                    i += 1
                
                if arr2[j] == smallest:
                    j += 1
                
                if arr3[k] == smallest:
                    k += 1
        
        return res
