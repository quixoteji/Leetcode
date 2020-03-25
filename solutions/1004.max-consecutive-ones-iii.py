#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#

# @lc code=start
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        return self.sol1(A, K)

    def sol1(self, A, K) :
        ans = start = 0
        for i, num in enumerate(A) :
            K -= num == 0
            while K < 0 :
                K += A[start] == 0
                start += 1
            ans = max(ans, i - start + 1)
        return ans





        
# @lc code=end

