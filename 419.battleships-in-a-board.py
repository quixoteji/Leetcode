#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board : return 0
        m, n = len(board), len(board[0])
        ans = 0
        for i in range(m) :
            for j in range(n) :
                if board[i][j] == '.' or \
                    (i > 0 and board[i - 1][j] == 'X') or \
                    (j > 0 and board[i][j - 1] == 'X') :
                    continue
                else :
                    ans += 1
        return ans
        
# @lc code=end

