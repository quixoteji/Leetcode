#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#

# @lc code=start
class Solution:

    def toHex(self, num: int) -> str:
        if num == 0 : return '0'
        if num < 0 : num += 2 ** 32
        res = ''
        while num > 0 :
            num, r = divmod(num, 16)
            if r > 9 : res = chr(ord('a') + r - 10) + res
            else : res = str(r) + res
        return res
        
# @lc code=end

