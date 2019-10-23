#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 : return 0 
        if divisor == 0 : return 0x7fffffff
        sign = (dividend > 0) ^ (divisor > 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor :
            x = divisor
            i = 1
            while dividend >= x + x :
                x += x
                i += i
            dividend -= x
            ans += i
        ans = -ans if sign else ans
        if ans > 2**31 - 1 : return 2**31 - 1
        if ans < -2**31 : return -2**31
        return ans

        
# @lc code=end

