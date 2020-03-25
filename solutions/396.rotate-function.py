#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        return self.sol2(A)

    def sol1(self, A) : 
        ans = sum([i * A[i] for i in range(len(A))])
        for _ in range(len(A) - 1) :
            A = [A[-1]] + A[:-1]
            ans = max(ans, sum([i * A[i] for i in range(len(A))]))
        return ans

    def sol2(self, A) : 
        f = sum([i * A[i] for i in range(len(A))])
        _sum= sum(A)
        ans = f
        for i in range(len(A) - 1) :
            f = f + _sum - len(A) * A[len(A) - i - 1]  
            ans = max(f, ans)
        return ans



        
# @lc code=end

