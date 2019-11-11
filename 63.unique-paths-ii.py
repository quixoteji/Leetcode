#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m) :
            for j in range(n) :
                print(i, j)
                if obstacleGrid[i][j] == 1 : 
                    dp[i][j] = 0
                    continue
                if i > 0 and j > 0 : dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                elif i == 0 and j == 0 : dp[i][j]
                elif i == 0 : dp[i][j] = dp[i][j-1]
                else : dp[i][j] = dp[i-1][j]
        return dp[m - 1][n - 1]
        
# @lc code=end

