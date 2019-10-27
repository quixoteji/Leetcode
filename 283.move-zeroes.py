#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # p for 0 and q for non-zero
        p, q = 0, 0
        for num in nums:
            if num == 0:
                p += 1
                nums[p], nums[q] = nums[q], nums[p]  
            else :

        
# @lc code=end

