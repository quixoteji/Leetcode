#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#

# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0 : return 0
        if n == 1 : return k
        # n = 2
        same, diff = k, k * (k - 1)
        for i in range(3, n + 1) :
            same, diff = diff, (same + diff) * (k - 1)
        return same + diff

        
# @lc code=end

