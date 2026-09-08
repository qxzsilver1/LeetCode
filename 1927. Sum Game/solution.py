class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        alice_total, bob_total = 0, 0
        alice_chars, bob_chars = 0, 0

        for i in range(n // 2):
            if num[i] == '?':
                alice_chars += 1
            else:
                alice_total += int(num[i])
        
        for i in range(n // 2, n):
            if num[i] == '?':
                bob_chars += 1
            else:
                bob_total += int(num[i])
        
        if alice_chars >= bob_chars:
            alice_chars -= bob_chars
            bob_chars = 0
        else:
            bob_chars -= alice_chars
            alice_chars = 0
        
        if alice_total >= bob_total:
            alice_total -= bob_total
            bob_total = 0
        else:
            bob_total -= alice_total
            alice_total = 0
        
        if alice_total and alice_chars  or bob_total and bob_chars:
            return True
        
        chars = alice_chars + bob_chars
        total = alice_total + bob_total

        return chars % 2 == 1 or chars * 9 // 2 != total
