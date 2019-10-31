#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9 :
            res = 0
            while num > 0 :
                res += num % 10
                num = num // 10
            num = res
        return num
        
# @lc code=end

