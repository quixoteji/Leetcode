#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        return self.sol1(A)

    def sol1(self, A) :
        if len(A) < 3 : return 0
        diff = [A[i] - A[i - 1] for i in range(1, len(A))]
        dp = [0 for i in diff]
        for i in range(1, len(diff)):
            if diff[i] == diff[i - 1] :
                dp[i] = dp[i - 1] + 1
        return sum(dp)
        
# @lc code=end

