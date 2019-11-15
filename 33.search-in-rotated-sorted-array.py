#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def sol1(self, nums, target) :
        start, end = 0, len(nums) - 1
        while start < end :
            mid = (start + end) // 2
            if nums[mid] < nums[start] : end = mid - 1
            else : start = mid
        bias = (start + len(nums))  - (len(nums) - 1)
        start, end = 0, len(nums) - 1
        while start <= end :
            mid0 = (start + end) // 2
            mid1 = ( mid0 + bias) % len(nums)
            if target == nums[mid1] : return mid1
            if target < nums[mid1] : end = mid0 - 1
            else : start = mid0 + 1
        return -1

    def sol2(self, nums, target) :
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]: 
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        return self.sol2(nums, target)
        
# @lc code=end

