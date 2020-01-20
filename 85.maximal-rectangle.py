#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        return self.sol1(matrix)

    # Solution 1 : dp
    def sol1(self, matrix) :
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                x, y = i + 1, j + 1
                if matrix[i][j] == '1' : dp[i][j]
        
# @lc code=end

