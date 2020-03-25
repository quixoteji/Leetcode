#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#

# @lc code=start
class Solution:
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    mem = None
    m = n = 0

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        return self.solution1(matrix)

    def solution1(self, matrix) :
        if not matrix or not matrix[0] : return 0
        self.m, self.n = len(matrix), len(matrix[0])
        self.mem = [[0]*self.n for _ in range(self.m)]
        ans = 0

        for i in range(self.m) :
            for j in range(self.n) :
                ans = max(ans, self.dfs(matrix, i, j))
        return ans

    def dfs(self, matrix, i, j) :
        if self.mem[i][j] : return self.mem[i][j]
        for d in self.dirs :
            x, y = i + d[0], j + d[1]
            if 0 <= x < self.m and 0 <= y < self.n and matrix[x][y] > matrix[i][j] :
                self.mem[i][j] = max(self.mem[i][j], self.dfs(matrix, x, y))
        self.mem[i][j] = self.mem[i][j] + 1

        return self.mem[i][j]

                


                    

        
# @lc code=end

