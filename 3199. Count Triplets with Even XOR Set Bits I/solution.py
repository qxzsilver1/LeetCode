class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:
        
        def count(arr):
            even = odd = 0

            for a in arr:
                if bin(a).count('1') % 2 == 0:
                    even += 1
                else:
                    odd += 1
            
            return even, odd
        
        a_even, a_odd = count(a)
        b_even, b_odd = count(b)
        c_even, c_odd = count(c)

        return a_even * b_even * c_even + a_even * b_odd * c_odd + a_odd * b_even * c_odd + a_odd * b_odd * c_even
