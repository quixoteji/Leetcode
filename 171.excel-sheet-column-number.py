#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        num = 0
        for char in s :
            val = ord(char) - ord("A") + 1
            num = num * 26 + val
        return num
# @lc code=end

