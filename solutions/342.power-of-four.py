#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        while num and num % 4 == 0:
            num /= 4
        return num == 1
        
# @lc code=end
