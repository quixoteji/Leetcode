#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums[1:] :
            ans ^= num
        return ans
        
# @lc code=end

