class Solution:
    def smallestCommonElement(self, mat: list[list[int]]) -> int:
        n, m = len(mat), len(mat[0])
        pos = [0] * n

        def binarySearch(arr, fromIndex, toIndex, target):
            left, right = fromIndex, toIndex - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -(left + 1)
        
        for j in range(m):
            found = True
            i = 1
            while i < n and found:
                pos[i] = binarySearch(mat[i], pos[i], m, mat[0][j])
                if pos[i] < 0:
                    found = False
                    pos[i] = -pos[i] - 1
                    if pos[i] >= m:
                        return -1
                i += 1

            if found:
                return mat[0][j]

        return -1
