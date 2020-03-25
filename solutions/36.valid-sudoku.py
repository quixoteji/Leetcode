#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9) :
            for j in range(9) :
                if board[i][j] == '.' : continue
                idx = (i // 3) + (j // 3) * 3
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[idx] :
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[idx].add(board[i][j])
        
        return True

        
# @lc code=end

