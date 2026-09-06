class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        next_possible_states = []

        for i in range(len(currentState) - 1):
            if currentState[i] == '+' and currentState[i + 1] == '+':
                next_state = currentState[:i] + '--' + currentState[i + 2:]
                next_possible_states.append(next_state)
        
        return next_possible_states
