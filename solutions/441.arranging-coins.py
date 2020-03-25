#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1 
        while n > 0 : n, i = n - i , i + 1
        return i - 1 if n == 0 else i - 2
        
# @lc code=end

