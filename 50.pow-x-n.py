#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1.0
        sign, n = 1 if n > 0 else 0, abs(n)
        ans, i = 0, 0
        while n > 0:
            ans += i
            i += 1
            while i * i 
        
# @lc code=end

