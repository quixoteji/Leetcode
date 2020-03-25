#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ones, overlaps = 0, 0
        for i in range(len(grid)) :
            for j in range(len(grid[0])) :
                if grid[i][j] == 1 : 
                    ones += 1
                    if i-1 >= 0 and grid[i-1][j] : overlaps += 1
                    if i+1 < len(grid) and grid[i+1][j] : overlaps += 1
                    if j-1 >= 0 and grid[i][j-1] : overlaps += 1
                    if j+1 < len(grid[0]) and grid[i][j+1] : overlaps += 1
        return 4 * ones - overlaps
        
# @lc code=end

