#
# @lc app=leetcode id=296 lang=python3
#
# [296] Best Meeting Point
#

# @lc code=start
class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        return self.sol1(grid)


    def sol1(self, grid) :
        rows, cols = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])) :
                if grid[i][j] :
                    rows.append(i)
                    cols.append(j)
        return self.minDis(rows) + self.minDis(cols)

    def minDis(self, vec) :
        vec.sort()
        ans, i, j = 0, 0, len(vec) - 1
        while i < j :
            ans += vec[j] - vec[i]
            i, j = i + 1, j - 1
        return ans

        
# @lc code=end

