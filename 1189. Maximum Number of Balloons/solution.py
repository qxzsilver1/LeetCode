class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = 'ablno'
        balloon_ablno_count = [1, 1, 2, 1, 2]
        text_ablno_count = [0, 0, 0, 0, 0]

        res = len(text)

        def balloon_counter(char):
            if char == 'a':
                text_ablno_count[0] += 1
            elif char == 'b':
                text_ablno_count[1] += 1
            elif char == 'l':
                text_ablno_count[2] += 1
            elif char == 'n':
                text_ablno_count[3] += 1
            elif char == 'o':
                text_ablno_count[4] += 1

        for t in text:
            balloon_counter(t)
        
        for i in range(len(balloon)):
            res = min(res, text_ablno_count[i] // balloon_ablno_count[i])

        return res
