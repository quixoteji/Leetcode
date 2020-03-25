#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        profit = [nums[0] for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0 : profit[0] = nums[0]
            elif i == 1 : profit[1] = max(nums[0], nums[1])
            else :
                profit[i] = max(profit[i - 1], profit[i - 2] + nums[i])
        return profit[-1]


        
# @lc code=end

