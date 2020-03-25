#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#

# @lc code=start
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if sum(A) < K : return -1
        ans, start = len(A) + 1, 0
        for i, num in enumerate(A) :
            K -= num
            while K <= 0 :
                K += A[start]
                start += 1
            ans = min(ans, i - start + 1)
        return -1 if ans == len(A) + 1 else ans
        
# @lc code=end

