#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x, ans, length = x * sign, 0, 10
        while x > 0 :
            res = x % 10
            ans = ans * length + res
            x =  x // 10
        ans = ans * sign 
        if ans > 2**31 - 1 : return 0
        if ans < -1 * 2**31 : return 0
        return ans


# @lc code=end

