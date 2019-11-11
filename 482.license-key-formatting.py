#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        s = ''.join(S.split('-')).upper()[::-1]
        n, t = 0, ''
        while n < len(s) :
            t += s[n : n + K] + '-'
            n += K
        
        return t[::-1][1:] 
        
# @lc code=end

