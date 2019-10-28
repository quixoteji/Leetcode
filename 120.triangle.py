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
        if len(triangle) == 0 : return 0 
        ans = []
        self.dfs(ans, triangle[0][0], 1, 0, triangle)
        return min(ans)
        
# @lc code=end

