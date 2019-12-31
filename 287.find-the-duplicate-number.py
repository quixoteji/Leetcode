#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        return sum(nums) - (len(nums) - 1) * len(nums) // 2
        
# @lc code=end

