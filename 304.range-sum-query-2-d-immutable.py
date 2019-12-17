#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        if not matrix : return 
        m, n = len(matrix), len(matrix[0])
        self._sum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1) :
            for j in range(1, n + 1) :
                self._sum[i][j] = matrix[i - 1][j - 1] \
                    + self._sum[i - 1][j] \
                    + self._sum[i][j - 1] \
                    - self._sum[i - 1][j - 1]
        # print(self._sum)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self._sum[row2 + 1][col2 + 1] \
            - self._sum[row2 + 1][col1] \
            - self._sum[row1][col2 + 1] \
            + self._sum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

