#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1 : return sum(nums)
        l, r, maxVal = 0, len(nums) - 1, float('-inf')
        temp = nums[:]
        while l <= r :
            maxVal = max(sum(temp), maxVal)
            if nums[l] < nums[r]:
                l += 1
                temp = nums[l : r + 1]
            else:
                r -= 1
                temp = nums[l : r + 1]
                
        return maxVal
        
# @lc code=end

