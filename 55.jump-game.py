#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i, num in enumerate(nums):
            if cover < i : return False
            cover = max(cover, i + nums[i])
            if cover >= len(nums) - 1 : return True
        return False
        
# @lc code=end

