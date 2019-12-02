#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.sol2(s)

    # Solution 1 : brutal_force
    def sol1(self, s) :
        if len(s) < 1 : return 0
        ans = 0

        def helper(s, i, j) :
            res = 0
            while i >= 0 and j < len(s) and s[i] == s[j] :
                i, j, res = i - 1, j + 1, res + 1
            return res

        for i in range(len(s)) :
            ans += helper(s, i, i) + helper(s, i, i + 1)

        return ans

    # Solution 2 : dp
    # dp[i][j] : s[i : j + 1] is Palindrome
    def sol2(self, s) :
        ans, n = 0, len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n) :
            i = n - 1 - i
            for j in range(i, n) :
                dp[i][j] = s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j] : ans += 1
        # print(dp)
        return ans
  
# @lc code=end

