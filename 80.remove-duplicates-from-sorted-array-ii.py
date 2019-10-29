#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        p, k = 1, 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] : 
                k += 1
                if k < 2 : p += 1
            else :
                k = 0
                nums[p] = nums[i]
                p += 1
        return p
        
# @lc code=end

