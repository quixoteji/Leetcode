#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
class Solution:
    def dfs(self, ans, grid, i, j, val) :
        m, n = len(grid), len(grid[0])
        if i == m - 1 and j == n - 1 : 
            ans.append(val + grid[i][j])
            return
        if i > m - 1 or j > n - 1 :
            return
        self.dfs(ans, grid, i + 1, j, val + grid[i][j])
        self.dfs(ans, grid, i, j + 1, val + grid[i][j])
    def sol1(self, grid) :
        ans = []
        i, j = 0, 0
        self.dfs(ans, grid, i, j, 0)
        return min(ans)

    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m) :
            for j in range(n) :
                if i == 0 and j == 0 : continue
                elif i == 0 : grid[i][j] = grid[i][j] + grid[i][j - 1]
                elif j == 0 : grid[i][j] = grid[i][j] + grid[i - 1][j]
                else : grid[i][j] = grid[i][j] + min(grid[i - 1][j], grid[i][j - 1])
        return grid[m - 1][n - 1]
        
# @lc code=end

