class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        mod = 10 ** 9 + 7

        left = [-1] * n
        right = [n] * n

        prefix_arr = [0] + list(accumulate(strength))
        prefix_of_prefix_arr = [0] + list(accumulate(prefix_arr))

        stack = []
        res = 0
        
        for i, m in enumerate(strength):
            while stack and stack[-1][0] >= m:
                stack.pop()
            
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1][1]
            
            stack.append((m, i))
        
        stack = []

        for i in range(n-1, -1, -1):
            m = strength[i]

            while stack and stack[-1][0] > m:
                stack.pop()
            
            if not stack:
                right[i] = n
            else:
                right[i] = stack[-1][1]
            
            stack.append((m, i))
        
        for i in range(n):
            l, r = i - left[i], right[i] - i

            subtotal = 0

            subtotal += l * (prefix_of_prefix_arr[right[i] + 1] - prefix_of_prefix_arr[i + 1])
            subtotal -= r * (prefix_of_prefix_arr[i + 1] - prefix_of_prefix_arr[left[i] + 1])
            
            res += subtotal * strength[i]
            res %= mod
        
        return res % mod
