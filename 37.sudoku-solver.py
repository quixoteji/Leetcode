#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def __init__(self) :
        self.board = None
        self.checkrows = None
        self.checkcols = None
        self.checkblocks = None
    def position(self, i, j) :
        x, y, z = i, j, (i // 3) * 3 + (j // 3)
    # True : cannot place
    def check(self, i, j, val) :
        x, y, z = self.position(i, j)
        return self.checkrows(x, val) or self.checkcols(y, val) or self.checkblocks(z, block)
    
    def update(self, i, j, val) :
        x, y, z = self.position(i, j)
        self.checkrows[x][val] = True
        self.checkcols[y][val] = True
        self.checkblocks[z][val] = True
        self.board[i][j] = str(val)
        
    def search(self, i, j) :
        if i == 8 and j == 8 : return self.board
        for i_idx in range(i, 9) :
            for j_idx in range(j, 9) :
                if self.board[i][j].isdigit() : 
                    if not self.check(i_idx, j_idx, int(self.board[i][j])) :
                        self.update(i_idx, j_idx, int(self.board[i][j]))
                    else : return
                else :
                    for val in range(1, 10) :
                        if self.check(i_idx, j_idx, val) : return
                        else :
                            self.update(i_idx, j_idx, val)
                            self.search(i_idx, j_idx)
                            self.update(i_idx, j_idx, '.')


                

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.checkrows = [[False for _ in range(9)] for _ in range(9)]
        self.checkcols = [[False for _ in range(9)] for _ in range(9)]
        self.checkblocks = [[False for _ in range(9)] for _ in range(9)]
        ans = self.search(0, 0)
        return ans
        
        
# @lc code=end

