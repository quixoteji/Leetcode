#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#

# @lc code=start
class Solution:
    def sol1(self, num) :
        if num < 2 : return True
        l, r = 2, num // 2
        while l <= r :
            mid = l + (r - l) // 2
            x = mid * mid
            if x == num : return True
            elif x > num : r -= 1
            else : l += 1
        return False
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2: return True
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        return x * x == num
# @lc code=end

