#
# @lc app=leetcode id=420 lang=python3
#
# [420] Strong Password Checker
#

# @lc code=start
class Solution:
    def strongPasswordChecker(self, s: str) -> int:
        missing_type = 3
        if any('a' <= c <= 'z' for c in s): missing_type -= 1
        if any('A' <= c <= 'Z' for c in s): missing_type -= 1
        if any(c.isdigit() for c in s): missing_type -= 1
        
# @lc code=end

