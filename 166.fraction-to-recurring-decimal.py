#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ''
        if numerator * denominator < 0 : ans += '-'
        numerator, denominator = abs(numerator), abs(denominator)
        ans += str(numerator // denominator)
        carrier = numerator % denominator
        if carrier > 0 : ans += '.'
        memo = {}
        while carrier > 0 :
            if carrier in memo:
                index = memo[carrier]
                ans = ans[:index]+'('+ans[index:] +')'
                return ans
            else:
                memo[carrier] = len(ans)
                ans += str((carrier*10)//denominator)
                carrier = (carrier*10) % denominator
        return ans

# @lc code=end

