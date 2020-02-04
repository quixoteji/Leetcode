#
# @lc app=leetcode id=308 lang=python3
#
# [308] Range Sum Query 2D - Mutable
#

# @lc code=start
class FenwickTree :
    def __init__(self, matrix) :
        m, n = len(matrix), len(matrix[0]) if matrix else 0

        self.matrix = matrix
        self.sums = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        [operator.setitem(
            self.sums[row], col,
            self.sums[row][col] + self.matrix[i - 1][j - 1]
        )
        for row in range(1, len(self.sums))
        for col in range(1, len(self.sums[0]))
        for i in range(row + 1 - (row & -row), row + 1)
        for j in range(col + 1 - (col & -col), col + 1)]

    def update(self, row, col, val) :
        i = row + 1
        while i < len(self.sums) :
            j = col + 1
            while j < len(self.sums[0]) :
                self.sums[i][j] += val - self.matrix[row][col]
                j += j & (-j)
            i += i & (-i)
        self.matrix[row][col] = val

    def sum(self, row, col) :
        r, i = 0, row
        while i > 0 :
            j = col
            while j > 0 :
                r += self.sums[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return r


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.tree = FenwickTree(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.tree.update(row, col, val)
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.tree.sum(row2 + 1, col2 + 1) \
            + self.tree.sum(row1, col1) \
            - self.tree.sum(row1, col2 + 1) \
            - self.tree.sum(row2 + 1, col1)
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

