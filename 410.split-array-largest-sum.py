#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        return self.sol1(nums, m)
        
    # dp
    def sol1(self, nums, m) :
        n = len(nums)
        sums = [n for _ in nums]
        dp = [[float('inf')] * n for _ in range(m + 1)]
        sums[0] = nums[0]
        for i in range(1, n) :
            sums[i] = sums[i - 1] + nums[i]
        for i in range(n) :
            dp[1][i] = sums[i]

        for i in range(2, m + 1) :
            for j in range(i - 1, n) :
                for k in range(j) : 
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][k], sums[j] - sums[k]))
        return dp[m][n - 1]

        
# @lc code=end

