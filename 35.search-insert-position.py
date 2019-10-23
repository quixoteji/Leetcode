#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def sol1(self, nums, target) :
        if nums[0] > target : return 0
        if nums[-1] < target : return len(nums)
        for i in range(len(nums)):
            if nums[i] == target : return i
            if  i + 1 < len(nums) and nums[i] < target and nums[i + 1] > target : 
                return i + 1
    
    def sol2(self, nums, target) :
        if nums[0] > target : return 0
        if nums[-1] < target : return len(nums)
        l, r = 0, len(nums) - 1
        while l < r :
            m = l + (r - l) // 2
            if nums[m] == target : return m
            elif nums[m] > target : r = m - 1
            else : l = m + 1
        return r


    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.sol1(nums, target)
        
# @lc code=end

