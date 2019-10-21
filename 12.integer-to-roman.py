#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        if num // 1000 != 0 : 
            ans += (num // 1000) * 'M'
            num %= 1000
        if num // 900 != 0 :
            ans += 'CM'
            num %= 900
        if num // 500 != 0 :
            ans += 'D'
            num %= 500
        if num // 400 != 0 :
            ans += 'CD'
            num %= 400
        if num // 100 != 0 :
            ans += (num // 100) * 'C'
            num %= 100
        if num // 90 != 0 :
            ans += 'XC'
            num %= 90
        if num // 50 != 0 :
            ans += 'L'
            num %= 50
        if num // 40 != 0 :
            ans += 'XL' 
            num %= 40
        if num // 10 != 0 :
            ans += (num // 10) * 'X'
            num %= 10
        if num // 9 != 0 :
            ans += 'IX'
            num %= 9
        if num // 5 != 0 :
            ans += 'V'
            num %= 5
        if num // 4 != 0 :
            ans += 'IV'
            num %= 4
        if num // 1 != 0 :
            ans += (num // 1) * 'I'
        
        return ans 



        
        
# @lc code=end

