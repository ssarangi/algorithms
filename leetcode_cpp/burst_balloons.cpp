#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int getCoinValue(vector<int>& nums, int i) {
        int val = (i < 0 || i == nums.size()) ? 1 : nums[i];
        return val;
    }

    int maxCoins(vector<int>& nums) {
        
    }
};

int main() {
    vector<int> coins = { 3, 1, 5, 8 };
    Solution soln;
    int total_coins = soln.maxCoins(coins);
    cout << total_coins << endl;
    return 0;
}