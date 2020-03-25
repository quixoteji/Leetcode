#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atmost(A, K) - self.atmost(A, K - 1)
        
    def atmost(self, A, K) :
        if K <= 0 : return 0
        cnt = collections.defaultdict(int)
        ans = start = 0
        for i, num in enumerate(A) :
            cnt[num] += 1
            while len(cnt) > K :
                cnt[A[start]] -= 1
                if cnt[A[start]] == 0 : del cnt[A[start]]
                start += 1
            ans += i - start + 1
        print(ans)
        return ans




        
# @lc code=end

