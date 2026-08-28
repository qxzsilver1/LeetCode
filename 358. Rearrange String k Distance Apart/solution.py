class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        freqs = Counter(s)
        max_freq = max(freqs.values()) if freqs else 0

        most_chars, second_most_chars = set(), set()
        
        for char, freq in freqs.items():
            if freq == max_freq:
                most_chars.add(char)
            elif freq == max_freq - 1:
                second_most_chars.add(char)
        
        segments = [[] for _ in range(max_freq)]

        for i in range(max_freq):
            for c in most_chars:
                segments[i].append(c)
            
            if i < max_freq - 1:
                for c in second_most_chars:
                    segments[i].append(c)
        
        segment_id = 0

        for char, freq in freqs.items():
            if char in most_chars or char in second_most_chars:
                continue
            
            for _ in range(freq):
                segments[segment_id].append(char)
                segment_id = (segment_id + 1) % (max_freq - 1)
        
        for i in range(max_freq - 1):
            if len(segments[i]) < k:
                return ''
        
        return ''.join(''.join(segment) for segment in segments)
