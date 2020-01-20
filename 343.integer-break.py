#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        return self.sol1(n)

    def sol1(self, n) :
        if n == 2 or n == 3 : return n - 1
        ans = 1
        while n > 4 :
            ans *= 3
            n -= 3
        return ans * n
        
            

# @lc code=end

