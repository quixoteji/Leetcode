#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return self.sol1(s1, s2)

    def sol1(self, s1, s2) :
        if len(s1) != len(s2) : return False
        if s1 == s2 : return True
        if ''.join(sorted(s1)) != ''.join(sorted(s2)) : return False
        for i in range(1, len(s1)) :
            s11, s12 = s1[:i], s1[i:]
            s21, s22 = s2[:i], s2[i:]
            if self.sol1(s11, s21) and self.sol1(s12, s22) : return True
            s21, s22 = s2[-i:], s2[:-i]
            if self.sol1(s11, s21) and self.sol1(s12, s22) : return True
        return False

    def __init__(self) :
        self.dict = {}
    def sol2(self, s1, s2) : 
        if (s1, s2) in self.dict : return self.dict[(s1,s2)]
        if len(s1) != len(s2) or sorted(s1) != sorted(s2):
            self.dict[(s1,s2)] = False
            return False
        if s1 == s2: 
            self.dict[(s1, s2)] = True
            return True
        for i in range(1, len(s1)) :
            s11, s12 = s1[:i], s1[i:]
            s21, s22 = s2[:i], s2[i:]
            if self.sol2(s11, s21) and self.sol2(s12, s22) : return True
            s21, s22 = s2[-i:], s2[:-i]
            if self.sol1(s11, s21) and self.sol1(s12, s22) : return True
        self.dict[(s1, s2)] = False
        return False

    #Solution : ??????
    def sol3(self, s1, s2) : 
        if len(s1) != len(s2) : return False
        if s1 == s2 : return True
        n = len(s1)
        #dp[i][j][k] : 
        # i : start idx of s1
        # j : start idx of s2
        # k : length of current string
        dp = [[[True for _ in range(n+1)] for _ in range(n)] for _ in range(n)]
        for l in range(1, n + 1) :
            for i in range(n - l) :
                for j in range(n - l) :
                    if l == 1 :
                        dp[i][j][1] = s1[i] == s2[j]
                    else :
                        for k in range(1, l) :
                            dp[i][j][k] = (dp[i][j][k] and dp[i + k][j + k][l - k]) or (dp[i + k][j][l - k] and dp[i][j + l - k][k])
        return dp[0][0][n]
# @lc code=end

