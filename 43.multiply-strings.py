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
        res = 0
        for i in range(l1) :
            val = 0
            for j in range(l2) :
                val += 

        

        
# @lc code=end

