#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def findfirst(self, nums, target) :
        l, r = 0, len(nums) 
        while l < r :
            m = l + (r - l) // 2
            if nums[m] >= target : r = m
            else : l = m + 1
        return -1 if l == len(nums) or nums[l] != target else l

    def findlast(self, nums, target) :
        l, r = 0, len(nums)
        while l < r :
            m = l + (r - l) // 2
            if nums[m] > target : r = m  
            else : l = m + 1
        l -= 1
        return -1 if l < 0 or nums[l] != target else l

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.findfirst(nums, target), self.findlast(nums, target)]
                     
# @lc code=end

