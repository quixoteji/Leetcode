#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        return self.sol2(n)

    def sol1(self, n) :
        ans = 0
        for num in range(1, n + 1) :
            ans += collections.Counter(str(num))['1']
        return ans

    def sol2(self, n) :
        if n <= 0:
            return 0
        if 1 <= n <= 9:
            return 1
        # compute the first bit
        head, level = n, 1
        while head > 9:
            level *= 10
            head //= 10
        # if the first bit is 1
        # like 191, divide it into (0-99), (0-91) and the first bit in (100, 101, 1.., 191)
        if head == 1:
            return  self.countDigitOne(level-1) + self.countDigitOne(n-level) + n-level +1
        # like 491, divide it into (0-99), (100-199), (200-299, 300-399) and (400-491)
        return (head) * self.countDigitOne(level-1) + self.countDigitOne(n-head*level) + level


        
# @lc code=end

