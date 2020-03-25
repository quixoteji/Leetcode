#
# @lc app=leetcode id=294 lang=python3
#
# [294] Flip Game II
#

# @lc code=start
class Solution:
    def canWin(self, s: str) -> bool:
        return self.sol1(s)

    # Solution 1 :
    def sol1(self, s) :
        return self.canWin(s)

    def canWin(self, s) :
        for i in range(1, len(s)) :
            if s[i] == s[i - 1] == '+' and not self.canWin(s[:i - 1] + '--' + s[i + 1 :]) :
                return True
        return False


# @lc code=end

