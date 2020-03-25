#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:            
    def findPeakElement(self, nums: List[int]) -> int:
        return self.sol2(nums)

    def sol1(self, nums) :
        nums.insert(0, float('-inf'))
        nums.append(float('-inf'))
        for i in range(1, len(nums) - 1) :
            if nums[i - 1] < nums[i] > nums[i + 1] :
                return i - 1

    def sol2(self, nums) :
        l, r = 0, len(nums) - 1
        while l < r :
            m = l + (r - l) // 2
            if nums[m] < nums[m + 1] : l = m + 1
            else : r = m
        return r

        
# @lc code=end

