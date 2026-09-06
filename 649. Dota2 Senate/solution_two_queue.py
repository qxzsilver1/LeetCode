class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)

        d_q, r_q = deque(), deque()

        for i, c in enumerate(senate):
            if c == 'R':
                r_q.append(i)
            else:
                d_q.append(i)
        
        while d_q and r_q:
            d_turn = d_q.popleft()
            r_turn = r_q.popleft()

            if r_turn < d_turn:
                r_q.append(d_turn + len(senate))
            else:
                d_q.append(r_turn + len(senate))

        return 'Radiant' if r_q else 'Dire'
