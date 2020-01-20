#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.sol3(nums)

    # Solution 1 : O(n)
    def sol1(self, nums) :
        ans = float('-inf')
        for i in range(1, len(nums)) :
            if nums[i] < nums[i - 1] : ans = nums[i]
        return nums[0] if ans == float('-inf') else ans
            
    # Solution 2 : O(log(n))
    def sol2(self, nums) :
        left, right = 0, len(nums) - 1
        while left < right :
            mid = left + (right - left) // 2
            if nums[mid] > nums[right] : left = mid + 1
            else : right = mid
        return nums[right]

    # Solution 3
    def sol3(self, nums) :
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, left, right) :
        if nums[left] <= nums[right] : return nums[left]
        mid = (left + right) // 2
        return min(self.helper(nums, left, mid), self.helper(nums, mid + 1, right))
        
# @lc code=end

