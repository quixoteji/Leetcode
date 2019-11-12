#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        p1, p2, k = 0, 1, 0
        while p1 < len(nums) and p2 < len(nums):
            if nums[p2] != nums[p1] : 
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1
        
# @lc code=end

