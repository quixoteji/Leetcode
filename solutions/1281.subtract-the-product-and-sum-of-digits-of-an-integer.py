#
# @lc app=leetcode id=1281 lang=python3
#
# [1281] Subtract the Product and Sum of Digits of an Integer
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return self.sol1(n)

    def sol1(self, n) :
        _sum, _product = 0, 1
        for c in str(n) :
            _sum += int(c)
            _product *= int(c)
        return _product - _sum
        
# @lc code=end

