#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1: return s
    
        ans = []
        l = len(s)
        for r in range(numRows):
            idx = r
            if r == 0 or r == numRows - 1 :
                while idx < l :
                    ans.append(s[idx])
                    idx += 2 * numRows - 2
            else :
                while idx < l :
                    ans.append(s[idx])
                    x = 2 * (numRows - r - 2) + 2
                    if idx + x < l :
                        ans.append(s[idx + x])
                    idx += 2 * numRows - 2
        return ''.join(ans)
        
# @lc code=end

