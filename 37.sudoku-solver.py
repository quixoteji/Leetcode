#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def fill(self, board, x, y) :
        if y == 9 : return 
        nx = (x + 1) % 9;
        ny = y + 1 if nx == 0 else y
        if board[y][x] != '.': 
            self.fill(board, nx, ny)
        for num in range(1, 10) :
            nr, nc, nb = 
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        _rows = [True for i in range(9)]
        _cols = [True for i in range(9)]
        _blocks = [True for i in range(9)]
        for i in range(9) :
            for j in range(9) :
                if board[i][j] != '.' :
                    n = board[i][j] - '0'
                    _rows[i][n] = False
                    _cols[j][n] = False
                    _blocks[i // 3 * 3 + j // 3][n] = False
        self.fill(board, 0, 0)
        
        
# @lc code=end

