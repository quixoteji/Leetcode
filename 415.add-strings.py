#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1] 
        s, carry = '', 0
        while num1 or num2 :
            char1 = int(num1[0]) if num1 else 0
            char2 = int(num2[0]) if num2 else 0
            carry, num = divmod(char1 + char2 + carry, 10)
            s += str(num)
            num1 = num1[1:] if num1 else num1
            num2 = num2[1:] if num2 else num2
        s = s + '1' if carry else s
        return s[::-1]


        
# @lc code=end

