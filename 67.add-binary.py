#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b, carry = a[::-1], b[::-1], 0
        ans = ''
        while a or b :
            val1 = ord(a[0]) - ord('0') if a else 0
            val2 = ord(b[0]) - ord('0') if b else 0
            val = (val1 + val2 + carry) % 2
            ans += str(val)
            carry = (val1 + val2 + carry) // 2
            a = a[1:] if a else a
            b = b[1:] if b else b
        return (ans + str(carry))[::-1] if carry else ans[::-1]
        
# @lc code=end

