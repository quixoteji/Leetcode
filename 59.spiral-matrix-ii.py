#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        seen = [[False] * n for _ in range(n)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        board = [[0] * n for _ in range(n)]
        d, x, y = 0, 0, 0
        for t in range(1, n * n + 1) :
            board[x][y] = t
            seen[x][y] = True
            ix, iy = x + directions[d][0], y + directions[d][1]
            if -1 < ix < n and -1 < iy < n and not seen[ix][iy] :
                x, y = ix, iy
            else :
                d = (d + 1) % 4
                x, y = x + directions[d][0], y + directions[d][1]
        return board



        
# @lc code=end

