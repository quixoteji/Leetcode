#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#

# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            sub = s[0:i+1]
            if len(s) % len(sub) != 0 : continue
            if sub * (len(s) // len(sub)) == s : return True
        return False
            
        
# @lc code=end

