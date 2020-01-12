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
                if self.search(i, j, 0, board, word): return True
        return False

    def search(self, x, y, i, word, board) :
        if word[i] == board[x][y] :
            if i == len(word) - 1 : return True
            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            char = board[x][y]
            board[x][y] = '*'
            for (d0, d1) in d :    
                if self.search(x + d0, y + d1, i + 1, word, board) : 
                    return True
            


                    

        
# @lc code=end

