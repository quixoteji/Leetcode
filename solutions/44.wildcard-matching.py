#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    # def backtracking(self, s, p) :
    #     if p == '*' : return True
    #     if not s : 
    #         if not p: return True
    #         else : return False
    #     if not p : return False

        
    #     if s[0] == p[0] or p[0] == '?': 
    #         return self.backtracking(s[1:], p[1:])

    #     if p[0] == '*' :
    #         if len(p) > 1 and p[1:] == '*' :
    #             return self.backtracking(s, p[1:])
    #         for i in range(len(s)) :

            # return False

    def iter_method(self, s, p) :
        s_idx, p_idx, match, start_idx = 0, 0, 0, -1
        while s_idx < len(s) :
            if p_idx < len(p) and (p[p_idx] == s[s_idx] or p[p_idx] == '?') :
                p_idx, s_idx = p_idx + 1, s_idx + 1
            elif p_idx < len(p) and p[p_idx] == '*' :
                start_idx = p_idx
                match = s_idx
                p_idx += 1
            elif start_idx != -1 :
                p_idx = start_idx + 1
                match += 1
                s_idx = match
            else :
                return False
            while p_idx < len(p) and p[p_idx] == '*' :
                p_idx += 1
            return len(p) == p_idx

    def dp(self, s, p) :
        dp = [[True for _ in range(len(p))] for _ in range(len(s))]
        for i in range(len(s)) :
            for j in range(len(p)) :
                s_idx = len(s) - i
                p_idx = len(p) - i
                if s_idx == len(s) and p_idx == len(p) : continue
                first_match = s_idx < len(s) and p_idx < len(p) \
                    and (p[p_idx] == s[s_idx] or p[p_idx] == '?' or p[p_idx] == '*')
                if p_idx < len(p) and p[p_idx] == '*' :
                    d[i][j] = dp[i][j + 1] or (first_match and dp[i + 1][j])
                else :
                    d[i][j] = first_match and dp[i + 1][j + 1]
        return dp[0][0]



    def isMatch(self, s: str, p: str) -> bool:
        return self.dp(s, p)
        
# @lc code=end

