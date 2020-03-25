#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:   
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.sol1(board, word)

    # Solution 1 : BFS
    def sol1(self, board, word) :
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.search(i, j, 0, board, word): return True
        return False

    def search(self, x, y, i, board, word) :
        if word[i] == board[x][y] :
            if i == len(word) - 1: return True
            d = [1, 0, -1, 0, 1]
            for j in range(4) :
                dx, dy = x + d[j], y + d[j + 1]
                if dx >= len(board) or dy >= len(board[0]) or dx < 0 or dy < 0 :
                    continue
                char = board[x][y]
                board[x][y] = '*'
                if self.search(dx, dy, i + 1, board, word) : return True
                board[x][y] = char
        else : return False

        
# @lc code=end

