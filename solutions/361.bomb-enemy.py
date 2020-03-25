#
# @lc app=leetcode id=361 lang=python3
#
# [361] Bomb Enemy
#

# @lc code=start
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        return self.solution1(grid)

    def solution1(self, grid) :
        if not grid or not grid[0] : return 0
        r, c = len(grid), len(grid[0])
        ans = 0
        dp = [[0] * c for _ in range(r)]
        # left
        for i in range(r) :
            row_hits = 0
            for j in range(c) :
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'w' :
                    row_hits = 0
                else :
                    dp[i][j] = row_hits

        # right
        for i in range(r) :
            row_hits = 0
            for j in range(c - 1, -1, -1) :
                if grid[i][j] == 'w' :
                    row_hits = 0
                elif grid[i][j] == 'E' :
                    row_hits += 1
                else :
                    dp[i][j] += row_hits

        # down
        for i in range(len(dp[0])):
            col_hits = 0
            for col in range(len(dp)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    dp[col][i] += col_hits

        for i in range(len(dp[0])):
            col_hits = 0
            for col in range(len(dp)-1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits +=1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    dp[col][i] += col_hits
                    ans = max(ans, dp[col][i])

        return ans     



        
# @lc code=end

