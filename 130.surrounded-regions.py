#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.sol1(board)

    # Solution 1 : DFS
    def sol1(self, board) :
        if not board : return
        r, c = len(board), len(board[0])
        hs = set()
        for j in range(c) :
            if board[0][j] == 'O' : hs.add((0,j))
            if board[r-1][j] == 'O' : hs.add((r-1,j))

        for i in range(r) :
            if board[i][0] == 'O' : hs.add((i, 0))
            if board[i][c-1] == 'O' : hs.add((i, c-1))

        hashset = set()
        for (i, j) in hs :
            self.dfs(i, j, board, hashset)
        
        for i in range(r) :
            for j in range(c) :
                if (i,j) in hashset :
                    board[i][j] = 'O'
                else :
                    board[i][j] = 'X'

    def dfs(self, i, j, board, hashset) :
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) :
            return
        else :
            if board[i][j] == 'X' : return
            else :
                hashset.add((i, j))
                board[i][j] = 'X'
                self.dfs(i + 1, j, board, hashset)
                self.dfs(i - 1, j, board, hashset)
                self.dfs(i, j + 1, board, hashset)
                self.dfs(i, j - 1, board, hashset)

            
        
# @lc code=end

