#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.sol1(s)

    # Solution 1 : dp
    def sol1(self, s) :
        if s == '0' or not s : return 0
        dp = [1 for _ in range(len(s) + 1)]
        for i in range(1, len(dp)):
            dp[i] = 0 if s[i - 1] == '0' else dp[i - 1]
            if i >= 2 and 9 < int(int(s[i-2 : i])) < 27 : dp[i] += dp[i - 2]
        return dp[-1]

        
# @lc code=end

