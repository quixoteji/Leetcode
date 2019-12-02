#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0] : return
        rows, cols = len(matrix), len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if c != 0 : matrix[r][c] += matrix[r][c - 1]
                if r != 0 : matrix[r][c] += matrix[r - 1][c]
                if c != 0 and r != 0 : matrix[r][c] -= matrix[r - 1][c - 1]
        self.matrix = matrix
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        region = self.matrix[row2][col2]
        if col1 != 0 : region -= self.matrix[row2][col1 - 1]
        if row1 != 0 : region -= self.matrix[row1 - 1][col2]
        if row1 != 0 and col1 != 0 : region += self.matrix[row1 -1 ][col1 - 1]
        return region


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

