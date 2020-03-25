#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m) :
            for j in range(n) :
                if i > 0 and j > 0:
                    dp[i][j] =  dp[i - 1][j] + dp[i][j - 1]
                elif i == 0 :
                    dp[i][j] = dp[i][j - 1]
                else :
                    dp[i][j] = dp[i - 1][j]
        return dp[m - 1][n - 1]
        
# @lc code=end

