#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#

# @lc code=start
class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        if S == 0 : return self.atmost(A, S)
        return self.atmost(A, S) - self.atmost(A, S - 1)

    def atmost(self, A, S) :
        ans = start = 0
        for i, num in enumerate(A) :
            S -= num == 1
            while S < 0 :
                S += A[start] == 1
                start += 1
                
            ans += i - start + 1
        return ans

        
# @lc code=end

