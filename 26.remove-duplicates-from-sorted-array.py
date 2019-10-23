#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1 : return len(nums)
        p1, p2 = 0, 1
        while p1 < len(nums) and p2 < len(nums) :
            if nums[p2] != nums[p1] : 
                p1 += 1
                nums[p1] = nums[p2]
            p2 += 1
        return p1 + 1
            
            
        
# @lc code=end

