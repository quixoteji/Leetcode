#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    rows = []
    cols = []
    diag1 = []
    diag2 = []
    board = []
    ans = 0

    def isavailable(self, x, y, n) :
        return self.rows[x] and self.cols[y] and self.diag1[x + y] and self.diag2[x - y + n - 1]

    def update(self, x, y, n, val) :
        self.rows[x] = val
        self.cols[y] = val
        self.diag1[x + y] = val
        self.diag2[x - y + n - 1] = val

    def queens(self, x, y, n) :
        if x == n : 
            self.ans += 1
            return
        for i in range(n) :
            if self.isavailable(x, i, n) :
                self.update(x, i, n, False)
                self.queens(x + 1, 0, n)
                self.update(x, i, n, True) 

    def totalNQueens(self, n: int) -> int:
        self.rows = [True for i in range(n)]
        self.cols = [True for i in range(n)]
        self.diag1 = [True for i in range(2 * n - 1)]
        self.diag2 = [True for i in range(2 * n - 1)]
        self.queens(0, 0, n)
        return self.ans

                    
        
# @lc code=end

