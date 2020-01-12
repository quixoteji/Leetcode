#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.sol1(nums)

    def sol1(self, nums):
        if len(nums) < 2: return 0
        p1, p2 = 0, 1
        while p1 < len(nums) and p2 < len(nums) :
            if nums[p1] != nums[p2] : 
                p1 += 1
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 += 1
        return p1

        
# @lc code=end

