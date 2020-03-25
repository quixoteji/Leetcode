#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#

# @lc code=start
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        max_r, max_c = m, n
        for op in ops :
            max_r = min(op[0], max_r)
            max_c = min(op[1], max_c)
        return max_r * max_c

        
# @lc code=end

