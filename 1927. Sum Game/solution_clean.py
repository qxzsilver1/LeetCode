class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        total = 0
        chars = 0

        for i in range(n // 2):
            a_num = num[i]

            if a_num == '?':
                chars -= 1
            else:
                total -= int(a_num)

            b_num = num[i + n // 2]

            if b_num == '?':
                chars += 1
            else:
                total += int(b_num)
        
        if not chars:
            return total != 0
        
        if not total:
            return True
        
        if total * chars  > 0:
            return True

      return chars % 2 == 1 or abs(chars * 9 // 2) != abs(total)
