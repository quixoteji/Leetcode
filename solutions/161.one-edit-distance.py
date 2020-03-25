#
# @lc app=leetcode id=161 lang=python3
#
# [161] One Edit Distance
#

# @lc code=start
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t : return False
        if abs(len(s) - len(t)) > 1 : return False
        else:
            (s, t) = (s, t) if len(s) > len(t) else (t, s)
            idx = -1
            for i in range(len(t)) :
                if s[i] != t[i] : 
                    idx = i
                    break
            if len(s) == len(t) :
                return s[idx + 1 : ] == t[idx + 1 : ]
            else :
                return s[idx + 1 : ] == t[idx : ] if idx != -1 else True
        
# @lc code=end

