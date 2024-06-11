class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = defaultdict(int)
        arr2_set = set(arr2)

        ending_array = []

        for n in arr1:
            if n not in arr2_set:
                ending_array.append(n)
            
            arr1_count[n] += 1
        
        ending_array.sort()

        res = []

        for n in arr2:
            for _ in range(arr1_count[n]):
                res.append(n)
        
        return res + ending_array
