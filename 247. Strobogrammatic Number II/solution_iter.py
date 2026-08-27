class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        inverse_pairs = [['0', '0'], ['1', '1'], ['6', '9'], ['8', '8'], ['9', '6']]

        curr_strings_length = n % 2

        queue =['0', '1', '8'] if curr_strings_length == 1 else ['']

        while curr_strings_length < n:
            
            curr_strings_length += 2

            curr_strobo_nums = []

            for num in queue:
                for pair in inverse_pairs:
                    if pair[0] != '0' or curr_strings_length != n :
                        curr_strobo_nums.append(pair[0] + num + pair[1])
            
            queue = curr_strobo_nums
        
        return queue
