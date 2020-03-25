#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = [nums[0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            f[i] = f[i - 1] + nums[i] if f[i - 1] > 0 else nums[i]
        return max(f)


        
# @lc code=end

