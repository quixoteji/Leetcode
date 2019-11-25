#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) < 1 : return None
        left, right = 0, len(nums) - 1
        while left < right :
            if nums[left]
            mid = left + (right - left) // 2
            if mid

        
# @lc code=end

