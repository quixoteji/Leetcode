#
# @lc app=leetcode id=256 lang=python3
#
# [256] Paint House
#

# @lc code=start
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        if not costs : return 0
        dp = costs
        for i in range(1, len(costs)) :
            dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])
            dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])
            dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])
        return min(dp[-1])
        
# @lc code=end

