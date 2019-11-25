#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2 : return sum(nums)
        # Do not rob the first
        loot1, prev = 0, 0
        for num in nums[1 : ]:
            loot1, prev = max(prev + num, loot1), loot1
        nums[-1] = 0
        loot2, prev = 0, 0
        for num in nums:
            loot2, prev = max(prev + num, loot2), loot2  
        return max(loot1, loot2) 
# @lc code=end

