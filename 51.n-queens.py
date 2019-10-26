#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    checkRow = []
    checkCol = []
    checkDiag1 = []
    checkDiag2 = []
    board = []
    ans = []
    # True : available for a Q
    # False : not available for a Q
    def check(self, x, y, n):
        return self.checkRow[x] and self.checkCol[y] and self.checkDiag1[x + y] and self.checkDiag2[x - y + n - 1]

    def update(self, x, y, n, val) :
        self.checkRow[x] = val
        self.checkCol[y] = val
        self.checkDiag1[x + y] = val
        self.checkDiag2[x - y + n - 1] = val
        self.board[x][y] = 'Q' if not val else '.'

    def queens(self, x, y, n) :
        if x == n :
            ans = []
            for l in self.board :
                ans.append(''.join(l))
            self.ans.append(ans)     
            return
        for i in range(n) :
            if self.check(x, i, n) :
                self.update(x, i, n, False)
                self.queens(x + 1, 0, n)
                self.update(x, i, n, True)


    def solveNQueens(self, n: int) -> List[List[str]]:
        self.checkRow = [True for i in range(n)]
        self.checkCol = [True for i in range(n)]
        self.checkDiag1 = [True for i in range(2*n - 1)]
        self.checkDiag2 = [True for i in range(2*n - 1)]
        self.board = [['.' for i in range(n)] for j in range(n)]
        self.queens(0, 0, n)
        return self.ans
        
# @lc code=end

