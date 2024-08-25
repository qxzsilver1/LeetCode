class Solution:
    def compress(self, chars: List[str]) -> int:
        curr_idx, i = 0, 0

        while i < len(chars):
            curr_char = chars[i]
            cnt = 1

            while i + 1 < len(chars) and chars[i+1] == curr_char:
                cnt += 1
                i += 1
            
            chars[curr_idx] = curr_char
            curr_idx += 1

            if cnt > 1:
                for c in str(cnt):
                    chars[curr_idx] = c
                    curr_idx += 1
            
            i += 1
        
        return curr_idx
