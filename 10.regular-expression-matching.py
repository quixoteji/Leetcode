#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0 : return True
        if len(s) == 1 and len(p) == 1 :
            if s == p or p == '.' : return True
            else : return False
        if len(s) == '' : return p[1]
        
        
# @lc code=end

