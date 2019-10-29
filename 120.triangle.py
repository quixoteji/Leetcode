#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
class Solution:
    def dfs(self, ans, curr, d, i, triangle) :
        if d == len(triangle) : 
            ans.append(curr + triangle[d - 1][i])
            ans.append(curr + triangle[d - 1][i + 1])
            return
        self.dfs(ans, curr + triangle[d - 1][i], d + 1, i, triangle)
        self.dfs(ans, curr + triangle[d - 1][i + 1], d + 1, i + 1, triangle)

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return 0
        
        dp = [triangle[0][0]]
        
        for i in range(1, len(triangle)):
            level = [dp[0]+triangle[i][0]]
            for j in range(1, i):
                level.append(min(dp[j], dp[j-1]) + triangle[i][j])
            level.append(dp[-1]+triangle[i][-1])
            dp = level
                
        return min(dp)
        
# @lc code=end

