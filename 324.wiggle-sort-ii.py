#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 : return
        for i in range(1, len(nums)) :
            if (i % 2 == 0 and nums[i] <= nums[i - 1]) or (i % 2 == 1 and nums[i] >= nums[i - 1]) :
                nums[i], nums[i - 1] = nums[i - 1], nums[i]
        
# @lc code=end

