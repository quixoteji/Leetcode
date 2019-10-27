#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def dfs(self, ans, curr, x, y, word, board) :
        if curr == word : return ans.append(curr[:])
        if len(word) == len(curr) : return 
        if x - 1 < 0 or x + 1 >= len(board) or y - 1 < 0 or y + 1 >= len(board[0]):
            return 
        char = board[x][y]
        if x - 1 > 0 : self.dfs(ans, curr)
        
        

    def exist(self, board: List[List[str]], word: str) -> bool:
        curr = word[0]
        x = y = 0
        return self.dfs(ans, curr, x, y, word, board)

        
# @lc code=end

