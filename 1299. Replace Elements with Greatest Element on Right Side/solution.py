class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = 0
        curr_num = 0

        for i in range(len(arr) - 1, -1, -1):
            if i == len(arr) - 1:
                curr_max = arr[i]
                arr[i] = -1
            else:
                curr_num = arr[i]
                arr[i] = curr_max
                curr_max = max(curr_max, curr_num)
        
        return arr
