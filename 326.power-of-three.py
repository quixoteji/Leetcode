#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n > 0 and n % 3 == 0 :
            n /= 3
        return n == 1
        
# @lc code=end

