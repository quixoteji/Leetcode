#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def _sort(self, nums) :
        nums.sort()

    def two_pointers(self, nums) :
        idx, left, right = 0, 0, len(nums) - 1
        while idx <= right :
            if nums[idx] == 0 :
                nums[idx], nums[left] = nums[left], nums[idx]
                left, idx = left + 1, idx + 1
            elif nums[idx] == 1 :
                idx += 1
            else :
                nums[idx], nums[right] = nums[right], nums[idx]
                right = right - 1

        

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.two_pointers(nums)
        
# @lc code=end

