#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        return self.sol1(s)

    def sol1(self, s) :
        numStack = []
        opStack = []
        i = 0
        while i < len(s):
            while s[i].isspace() : i += 1
            if s[i]
            num = ''

        
# @lc code=end

