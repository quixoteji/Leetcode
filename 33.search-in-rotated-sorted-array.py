#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def helper(self, nums, target, start, end) :
        if start > end : return - 1 
        m = start + (start - end) // 2
        if nums[m] == target : return m
        elif nums[m] > target :
            if nums[start] < nums[m] : self.helper(nums, target, start, m - 1)
            else : self.helper(nums, target, start)
        else :


        

    def sol1(self, nums, target) :
        if len(nums) < 1 : return - 1
        return self.helper(nums, target, 0, len(nums) - 1)
        

    def search(self, nums: List[int], target: int) -> int:
        return self.sol1(nums, target)
        
# @lc code=end

