class Solution {
public:
    int maximumProduct(vector<int>& nums) {
        int min1 = INT_MAX, min2 = INT_MAX;
        int max1 = INT_MIN, max2 = INT_MIN, max3 = INT_MIN;

        for (auto& n : nums) {
            int prevMin1 = min1, prevMax1 = max1, prevMax2 = max2;

            max1 = max(max1, n);
            max2 = max(max2, min(prevMax1, n));
            max3 = max(max3, min(prevMax2, n));

            min1 = min(min1, n);
            min2 = min(min2, max(prevMin1, n));
        }

        return max(min1 * min2 * max1, max3 * max2 * max1);
    }
};
