#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        guess = x
        while guess * guess > x :
            guess = (guess + x // guess) // 2
        return guess
          
# @lc code=end

