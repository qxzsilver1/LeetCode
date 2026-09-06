class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        
        def to_string(number: int, range_val: int) -> str:
            parts = []

            for i in range(3, -1, -1):
                parts.append(str((number >> (i * 8)) & 255))

            return ".".join(parts) + "/" + str(range_val)

        def to_int(ip: str) -> int:
            parts = ip.split(".")
            result = 0

            for part in parts:
                result = result * 256 + int(part)

            return result
        
        cur = to_int(ip)
        res = []

        while n > 0:
            max_bits = (cur & -cur).bit_length() - 1 if cur else 32
            bit_val = 1
            count = 0

            while bit_val < n and count < max_bits:
                bit_val <<= 1
                count += 1

            if bit_val > n:
                bit_val >>= 1
                count -= 1

            res.append(to_string(cur, 32 - count))
            n -= bit_val
            cur += bit_val

        return res
