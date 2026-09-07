class Solution {
public:
    long long minEnd(int n, int x) {
        long long res = x, mask;
        n -= 1;

        for (mask = 1; n > 0; mask <<= 1)
            if ((mask & x) == 0) {
                res |= (n & 1) * mask;
                n >>= 1;
            }
        return res;
    }
};
