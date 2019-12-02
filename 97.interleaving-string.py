#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    # Solution 1 : DP
    def sol1(self, s1, s2, s3):
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3 : return False
        dp = [[False for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(1, n1 + 1) :
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])

        for i in range(1, n2 + 1) :
            dp[0][i] = dp[0][i - 1] and (s2[i - 1] == s3[i - 1])

        for i in range(1, n1 + 1) :
            for j in range(1, n2 + 1) :
                dp[i][j] = (dp[i - 1][j] and (s1[i - 1] == s3[i - 1 + j])) \
                    or (dp[i][j - 1] and ((s2[j - 1] == s3[j - 1 + i])))
        print(dp)
        return dp[n1][n2]


    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.sol1(s1, s2, s3)
        
# @lc code=end

