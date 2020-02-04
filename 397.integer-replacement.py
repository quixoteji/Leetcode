#
# @lc app=leetcode id=397 lang=python3
#
# [397] Integer Replacement
#

# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.sol1(n)

    def sol1(self, n) :
        if n == 1 : return 0
        if n % 2 == 0 : return 1 + self.sol1(n // 2)
        else :
            return min(2 + self.sol1((n + 1) // 2), 2 + self.sol1((n - 1) // 2))

        
# @lc code=end

