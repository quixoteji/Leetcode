#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] : 
                    if self.search(i, j, 1, word, board) : return True
        return False

    def search(self, x, y, i, word, board) :
        if i == len(word) : return True
        temp = board[x][y]
        if x - 1 >= 0 and word[i] == board[x][y]:
            self.search(x - 1, y, i + 1, word, board)
            board[x][y] = temp
        if x + 1 < len(word) and word[i] == board[x][y]:
            self.search(x + 1, y, i + 1, word, board)
            board[x][y] = temp
        if y - 1 >= 0 and word[i] == board[x][y]:
            self.search(x, y - 1, i + 1, word, board)
            board[x][y] = temp
        if y + 1 < len(word) and word[i] == board[x][y]:
            self.search(x, y + 1, i + 1, word, board)
            board[x][y] = temp


        
# @lc code=end

