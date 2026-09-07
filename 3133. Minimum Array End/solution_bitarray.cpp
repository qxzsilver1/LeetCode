#define ll long long

class Solution {
public:
    ll minEnd(int n, int x) {
        ll res = 0;
        n -= 1;

        vector<int> xBinary(64, 0);
        vector<int> nBinary(64, 0);

        ll longX = x;
        ll longN = n;

        for (int i = 0; i < 64; i++) {
            xBinary[i] = (longX >> i) & 1;
            nBinary[i] = (longN >> i) & 1;
        }

        int posX = 0, posN = 0;

        while (posX < 63) {
            while (xBinary[posX] != 0 && posX <63)
                posX++;
            
            xBinary[posX] = nBinary[posN];
            posX++;
            posN++;
        }

        for (int i = 0; i < 64; i++) {
            if (xBinary[i] == 1)
                res += pow(2, i);
        }

        return res;
    }
};
