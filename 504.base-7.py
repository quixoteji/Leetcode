#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0 : return '0'
        f = 1 if num > 0 else 0
        num, s = abs(num), ''
        while num > 0:
            num, r = divmod(num, 7)
            s = str(r) + s
        return s if f else '-'+s
        
# @lc code=end

