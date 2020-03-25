#
# @lc app=leetcode id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k - 1)

    def atmost(self, nums, k) :
        if len(nums) < k : return 0
        ans = start = 0
        for i, num in enumerate(nums):
            k -= num % 2
            while k < 0 :
                k += nums[start] % 2
                start += 1
            ans += i - start + 1
        return ans
        

        
# @lc code=end

