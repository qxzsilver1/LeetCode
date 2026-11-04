class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        l_arr, r_arr = [], []
        delayed = defaultdict(int)

        left_size = right_size = 0
        sum_l, sum_r = 0, 0

        ops = [0] * n

        def prune(h: List[int], sign: int) -> None:
            while h and delayed[sign * h[0]]:
                delayed[sign * h[0]] -= 1
                heappop(h)

        def balance() -> None:
            nonlocal left_size, right_size, sum_l, sum_r
            
            if left_size > right_size + 1:
                num = -heappop(l_arr)
                heappush(r_arr, num)
                sum_r += num
                sum_l -= num
                right_size += 1
                left_size -= 1
                prune(l_arr, -1)
            elif right_size > left_size:
                num = heappop(r_arr)
                heappush(l_arr, -num)
                sum_l += num
                sum_r -= num
                left_size += 1
                right_size -= 1
                prune(r_arr, 1)

        for i, num in enumerate(nums):
            if not l_arr or num <= -l_arr[0]:
                heappush(l_arr, -num)
                left_size += 1
                sum_l += num
            else:
                heappush(r_arr, num)
                right_size += 1
                sum_r += num
            
            balance()
            
            if i >= x:
                num = nums[i - x]
                delayed[num] += 1
                
                if num <= -l_arr[0]:
                    left_size -= 1
                    sum_l -= num
                    if num == -l_arr[0]:
                        prune(l_arr, -1)
                else:
                    right_size -= 1
                    sum_r -= num
                    if num == r_arr[0]:
                        prune(r_arr, 1)
                
                balance()
            
            if i >= x - 1:
                mid = -l_arr[0]
                ops[i] = sum_r - sum_l + mid * (left_size - right_size)

        dp = [[0] + [inf] * k for _ in range(n)]
        
        for j in range(1, k + 1):
            if j == 1:
                dp[x - 1][j] = ops[x - 1]
            else:
                dp[j * x - 1][j] = dp[(j - 1) * x - 1][j - 1] + ops[j * x - 1]
        
        for j in range(1, k + 1):
            for i in range(j * x, n):
                dp[i][j] = min(dp[i - x][j - 1] + ops[i], dp[i - 1][j])
        
        return dp[n - 1][k]
