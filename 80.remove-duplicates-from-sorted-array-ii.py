#
# @lc app=leetcode id=80 lang=python3
#
# [80] Remove Duplicates from Sorted Array II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i, j, k = 0, 1, 0
        while i < len(nums) and j < len(nums):
            if nums[i] == nums[j] :
                if k < 2 : i, k = i + 1, k + 1
            else : 
                i, k = i + 1, 0
            nums[i] = nums[j]
            j += 1
            

        return i
        
# @lc code=end

