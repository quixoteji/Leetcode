#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def toVal(self, char) :
        return ord(char) - ord('0')
    
    def toStr(self, num) :
        return chr(num + ord('0'))

    def multiply(self, num1: str, num2: str) -> str:
        ans = ''
        l1, l2 = len(num1), len(num2)
        if l1 * l2 == 0 : return ans
        i = j = carry = 0
        while l1 > 0 or l2 > 0 :
            val1 = self.toVal(num1[l1 - 1]) if l1 > 0 else 1
            val2 = self.toVal(num2[l2 - 1]) if l2 > 0 else 1
            carry, val = divmod(val1 * val2 + carry, 10)
            ans = self.toStr(val) + ans
            l1, l2 = l1 - 1, l2 - 1
        return ans if carry == 0 else self.toStr(carry) + ans

        
# @lc code=end

