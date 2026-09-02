class Solution:
    def oddString(self, words: List[str]) -> str:
        diff_arr = []
        prev_idx, curr_idx = -1, -1

        for i in range(len(words)):
            word_len = len(words[i])
            curr_diff = [None] * (word_len - 1)
            
            for j in range(word_len - 1):
                curr_diff[j] = ord(words[i][j+1]) - ord(words[i][j])
            
            diff_arr.append(curr_diff)

            if len(diff_arr) <= 2:
                prev_idx = 0
                curr_idx = len(diff_arr) - 1
            else:
                if diff_arr[curr_idx] != diff_arr[prev_idx] and diff_arr[curr_idx] != diff_arr[i]:
                    return words[curr_idx]
                elif diff_arr[prev_idx] != diff_arr[curr_idx] and diff_arr[prev_idx] != diff_arr[i]:
                    return words[prev_idx]
                elif diff_arr[i] != diff_arr[curr_idx] and diff_arr[i] != diff_arr[prev_idx]:
                    return words[i]
                
                prev_idx += 1
                curr_idx = i
