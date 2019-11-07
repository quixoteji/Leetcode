#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2n, t2n = dict(), dict()
        for i, char in enumerate(s) : s2n[char] = i
        for i, char in enumerate(t) : t2n[char] = i
        for i in range(len(s)) :
            if s2n[s[i]] != t2n[t[i]] : return False
        return True

        
# @lc code=end

