#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    # Solution 1 :
    def sol1(self, n) :
        dp = [1] + [0 for _ in range(n)]
        for i in range(1, n + 1) :
            for j in range(0, i) :
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]

    def numTrees(self, n: int) -> int:
        return self.sol1(n)
        
# @lc code=end

