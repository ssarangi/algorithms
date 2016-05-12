/*
After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house is
the neighbor of the last one. Meanwhile, the security system for these houses
remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting
the police.
*/

#include <iostream>
#include <algorithm>

using namespace std;

// class Solution {
// public:
//     int rob(vector<int>& nums) {
//         if (nums.size() == 0)
//             return 0;
            
//         else if (nums.size() == 1)
//             return nums[0];
//         else if (nums.size() == 3)
//             return *(std::max_element(nums.begin(), nums.end()));
            
//         std::vector<int> dp(nums.size(), 0);
        
//         dp[0] = nums[0];
//         dp[1] = nums[1] > nums[0] ? nums[1] : nums[0];
        
//         for (int i = 2; i < nums.size(); ++i) {
//             int profit = dp[i-2] + nums[i];
//             if (dp[i-1] > profit)
//                 profit = dp[i-1];
                
//             dp[i] = profit;
//         }
        
//         return dp[nums.size()-1];
//     }
// };

// int main() {
//     Solution soln;
//     // std::vector<int> money = {5, 8, 10, 2, 3};
//     // std::vector<int> money = {5};
//     // std::vector<int> money = {4,1,2,7,5,3,1};
//     std::vector<int> money = {2,7,9,3,1};
//     int p1 = soln.rob(money);
//     std::vector<int> money__;
//     std::copy(money.begin() + 1, money.end(), std::back_inserter(money__));
//     int p2 = soln.rob(money__);
    
//     int p = std::max(p1, p2);
//     std::cout << p << std::endl;
//     return 0;
// }

int rob0(int* nums, int size)
{
    if(size == 0)
        return 0;
    if(size == 1)
        return nums[0];
    int *profits = (int*)malloc(sizeof(int)*size);
    profits[0] = nums[0];
    profits[1] = nums[1] > nums[0] ? nums[1] : nums[0];
    for(int i = 2; i < size; i++)
    {
        int profit = profits[i-2] + nums[i];
        if(profits[i-1] > profit)
            profit = profits[i-1];
        profits[i] = profit;
    }
    return profits[size-1];
}

//AC - 0ms;
int rob(int* nums, int size)
{
    if(size == 0)
        return 0;
    if(size == 1)
        return nums[0];
    int profit0 = rob0(nums, size-1);
    int profit1 = rob0(nums+1, size-1);
    return profit0 > profit1? profit0 : profit1;
}

int main() {
    int nums[] = {2, 7, 9, 3, 1};
    int v = rob(nums, 5);
    printf("%d\n", v);
    return 0;
}