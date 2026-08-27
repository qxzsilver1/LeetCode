class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        inverse_pairs = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]

        def generateStrobogrammaticNumbers(n, final_length):
            if n == 0:
                return ['']
            
            if n == 1:
                return ['0', '1', '8']
            
            prev_strobo_nums = generateStrobogrammaticNumbers(n - 2, final_length)

            curr_strobo_nums = []

            for prev_strobo_num in prev_strobo_nums:
                for pair in inverse_pairs:
                    if pair[0] != '0' or n != final_length:
                        curr_strobo_nums.append(pair[0] + prev_strobo_num + pair[1])
            
            return curr_strobo_nums
        
        return generateStrobogrammaticNumbers(n, n)
