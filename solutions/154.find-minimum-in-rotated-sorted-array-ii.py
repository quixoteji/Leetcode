#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.sol2(nums)

    def sol1(self, nums) : 
        left, right = 0, len(nums) - 1
        while left < right :
            mid = left + (right - left) // 2
            if nums[mid] > nums[right] : left = mid + 1
            elif nums[mid] < nums[right] : right = mid
            else : right -= 1
        return nums[right]

    def sol2(self, nums) :
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right) :
        if left == right : return nums[left]
        if nums[left] < nums[right] : return nums[left]
        mid = left + (right - left) // 2
        return min(self.helper(nums, left, mid), self.helper(nums, mid + 1, right))
# @lc code=end

