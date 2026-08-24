class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [ {'digit': 1, 'sign': 2, 'dot': 3}, {'digit': 1, 'dot': 4, 'exp': 5}, {'digit': 1, 'dot': 3}, {'digit': 4}, {'digit': 4, 'exp': 5}, {'sign': 6, 'digit': 7}, {'digit': 7}, {'digit': 7}]

        curr_state = 0

        for c in s:
            if c.isdigit():
                group = 'digit'
            elif c in ['+', '-']:
                group = 'sign'
            elif c in ['e', 'E']:
                group = 'exp'
            elif c == '.':
                group = 'dot'
            else:
                return False
        
            if group not in dfa[curr_state]:
                return False
            
            curr_state = dfa[curr_state][group]
        
        return curr_state in [1, 4, 7]
