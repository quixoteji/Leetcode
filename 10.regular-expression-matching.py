#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def recursion(self, s, p) : 
        if not p : return not s
        first_match = s and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*' : 
            return self.recursion(s, p[2:]) or (first_match and self.recursion(s[1:], p))
        else :
            return first_match and self.recursion(s[1:], p[1:])

    # dp[i][j] :  s[0,i) and p[0,j) 
    def dp(self, s, p) :
        matched = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        matched[0][0] = True
        
        for i in range(len(s) + 1) :
            for j in range(1, len(p) + 1) :
                if j > 1 and p[j - 1] == '*' :
                    matched[i][j] = matched[i][j - 2] or (i > 0 and (s[i - 1] == p[j - 2] and p[j - 2] == '.') and matched[i - 1][j])
                else :
                    matched[i][j] = i > 0 and matched[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                        
        return matched[-1][-1]

    def isMatch(self, s: str, p: str) -> bool:
        return self.dp(s, p)
        
# @lc code=end

