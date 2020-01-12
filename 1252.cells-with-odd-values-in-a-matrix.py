#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#

# @lc code=start
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        return self.sol1(n, m, indices)

    def sol1(self, n, m, indices) :
        row_count = [0] * n
        col_count = [0] * m
        for idx in indices :
            row_count[idx[0]] += 1
            col_count[idx[1]] += 1
        row_cnt = sum([1 for r in row_count if r % 2 == 1])
        col_cnt = sum([1 for c in col_count if c % 2 == 1])
        num_odd = row_cnt * m + (n - row_cnt) * col_cnt - row_cnt * col_cnt
        return num_odd
        
        
# @lc code=end

