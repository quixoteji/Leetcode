#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if not s : return s
        t,  n = '', 0
        while n < len(s) :
            t += s[n : n + k][::-1]
            if n + k < len(s) : t += s[n + k : n + 2 * k]
            n = n + 2 * k
        return t      
# @lc code=end

