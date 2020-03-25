#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#

# @lc code=start
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        return self.sol2(A, K)

    def sol1(self, A, K) :
        ans = float('-inf')
        for i in range(len(A)) :
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K and A[i] + A[j] > ans :
                    ans = A[i] + A[j]
        return -1 if ans == float('-inf') else ans

    def sol2(self, A, K) :
        A.sort()
        l, r = 0, len(A) - 1
        mx = float('-inf')
        while l < r :
            if A[l] + A[r] < K :
                mx = max(mx, A[l] + A[r])
                l += 1
            else :
                r -= 1
        return mx if mx != float('-inf') else -1

        
# @lc code=end

