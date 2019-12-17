#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#

# @lc code=start
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        best = 0
        for i in range(1, m + 1) :
            for j in range(1, n + 1) :
                dp[i][j] = mat[i - 1][j - 1] + dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
                l, r = 1, min(i, j)
                while l <= r :
                    k = (l + r) // 2
                    _sum = dp[i][j] - dp[i - k][j] - dp[i][j - k] + dp[i - k][j - k]
                    if _sum <= threshold:
                        best = max(best, k)
                        l = k + 1
                    else:
                        r = k - 1
        return best     
# @lc code=end

