#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2 : return nums
        p, q = 0, 0
        while q < len(nums) and p < len(nums):
            if nums[q] == 0 : pass
            else :
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            q += 1
            
            
            
            
    
# @lc code=end

