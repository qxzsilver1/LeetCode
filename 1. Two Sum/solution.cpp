class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();

        unordered_map<int, int> sum_map;

        for (int i = 0; i < n; i++) {
            if (sum_map.find(target - nums[i]) == sum_map.end())
                sum_map[nums[i]] = i;
            else
                return {sum_map[target - nums[i]], i};
        }

        return {-1, -1};
    }
};
