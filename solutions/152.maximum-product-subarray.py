#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 1 : return 0
        curMax = curMin = ans = nums[0]
        for num in nums[1:] :
            curMax, curMin = max(curMax * num, curMin * num, num),  min(curMax * num, curMin * num, num)
            ans = max(ans, curMax)
        return ans
        
# @lc code=end

