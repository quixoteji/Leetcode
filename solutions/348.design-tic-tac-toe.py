#
# @lc app=leetcode id=348 lang=python3
#
# [348] Design Tic-Tac-Toe
#

# @lc code=start
class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows, self.cols = [0 for _ in range(n)], [0 for _ in range(n)]
        self.up, self.down = 0, 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        n = len(self.rows)
        score = (2 * player) - 3

        self.rows[row] += score
        self.cols[col] += score
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n :
            return player
        
        if row == col : 
            self.up += score
            if abs(self.up) == n :
                return player

        if row + col == n - 1 :
            self.down += score
            if abs(self.down) == n :
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
# @lc code=end

