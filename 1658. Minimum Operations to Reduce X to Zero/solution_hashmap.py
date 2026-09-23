total = sum(nums)
        if total == x:
            return len(nums)

        target = total - x
        if target < 0:
            return -1

        res = -1
        prefixSum = 0
        prefixMap = {0: -1}  # prefixSum -> index

        for i, num in enumerate(nums):
            prefixSum += num
            if prefixSum - target in prefixMap:
                res = max(res, i - prefixMap[prefixSum - target])
            prefixMap[prefixSum] = i

        return len(nums) - res if res != -1 else -1
