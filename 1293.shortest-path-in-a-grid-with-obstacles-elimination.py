#
# @lc app=leetcode id=1293 lang=python3
#
# [1293] Shortest Path in a Grid with Obstacles Elimination
#

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dirs = (0, 1, 0, -1, 0)
        m, n = len(grid), len(grid[0])
        seen = set()
        
# @lc code=end

