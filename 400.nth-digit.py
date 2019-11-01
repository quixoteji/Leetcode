#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        l, cnt, start = 1, 9, 1
        while n > l * cnt :
            n -= l * cnt
            l += 1
            cnt *= 10
            start *= 10
        start += (n - 1) / l
        

        
# @lc code=end

