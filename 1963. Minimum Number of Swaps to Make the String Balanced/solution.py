class Solution:
    def minSwaps(self, s: str) -> int:
        max_unmatched_closing = 0
        extra_closing_brackets = 0

        for w in s:
            if w == ']':
                extra_closing_brackets += 1
            elif w == '[':
                extra_closing_brackets -= 1
            
            max_unmatched_closing = max(max_unmatched_closing, extra_closing_brackets)
        
        return int((max_unmatched_closing + 1) / 2)
