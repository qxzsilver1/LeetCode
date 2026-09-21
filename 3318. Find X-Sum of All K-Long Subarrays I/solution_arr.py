class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # cnts = [0] * 50

        res = []
        n = len(nums)
        
        # for num in nums:
        #     cnts[num - 1] += 1
        
        # num_counts = [(i + 1, v) for i, v in enumerate(cnts)]

        # num_counts.sort(key= lambda y: (-y[1], -y[0]))

        for i in range(n - k + 1):
            cnts = [0] * 50
            for j in range(i, i + k):
                cnts[nums[j] - 1] += 1

            num_counts = [(l + 1, v) for l, v in enumerate(cnts)]
            num_counts.sort(key= lambda y: (-y[1], -y[0]))
            x_sum = sum(y[0] * y[1] for y in num_counts[:x])

            res.append(x_sum)
        
        return res

