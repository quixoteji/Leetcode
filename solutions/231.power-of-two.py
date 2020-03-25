#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def sol1(self, n) :
        while n and n % 2 == 0 : 
            n /= 2
        return n == 1

    def sol2(self, n) :
        return n > 0 and n & (n-1) == 0

    def isPowerOfTwo(self, n: int) -> bool:
        return self.sol2(n)
        
# @lc code=end

