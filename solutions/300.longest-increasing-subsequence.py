#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    # Solution 1 : O(n^2)
    def sol1(self, nums) :
        if len(nums) == 0 : return 0
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)) :
            temp = []
            for j in range(0, i) :
                if nums[j] < nums[i] : temp.append(dp[j])
            dp[i] = max(temp) + 1 if temp else 1
        return max(dp)

    # Solution 2 : O(nlogn)
    def sol2(self, nums) :
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.sol1(nums)
        
# @lc code=end

