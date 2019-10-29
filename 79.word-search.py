#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def search(self, x, y, i, word, board) :
        if i == len(word) : return True
        
        
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] : 
                    self.search(i, j, word, board)



        
# @lc code=end

