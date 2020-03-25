#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ''
        while n > 0:
            s += chr(ord('A') + (n - 1) % 26 )
            n = (n - 1) // 26
        return s[::-1]

        
# @lc code=end

