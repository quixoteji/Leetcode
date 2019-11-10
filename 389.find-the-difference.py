#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        (s, t) = (s, t) if len(s) > len(t) else (t, s)
        num = ord(s[0])
        for char in (s+t)[1:] :
            num ^= ord(char)
        return chr(num)
        
# @lc code=end

