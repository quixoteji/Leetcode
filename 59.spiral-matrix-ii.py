#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nmin, nmax, start = 0, n - 1, 0
        directtions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        board = [[0 for i in range(n)] for j in range(n)]
        x, y = 0, 0
        for i in range(1, n * n + 1):
            board[x][y] = i
            if x >= nmin and 
            d = directtions[start % 4]
            x += 


        
# @lc code=end

