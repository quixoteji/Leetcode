#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#

# @lc code=start
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return self.sol1(n)

    def sol1(self, n) :
        # 0 : off 1 : on
        ons = 1
        while ons * ons <= n : ons += 1
        return ons-1


        
# @lc code=end

