class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        pangram_ind_arr = [0] * 26
        chars_sum = 0

        for c in sentence:
            c_idx = ord(c) - ord('a')

            if pangram_ind_arr[c_idx] == 0:
                pangram_ind_arr[c_idx] = 1
                chars_sum += 1

                if chars_sum == 26:
                    return True
            else:
                continue
        
        return chars_sum == 26
