#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        low, high = 0, 0
        for num in nums:
            low = ~high & (low ^ num)
            high = ~low & (high ^ num)
        return low
# @lc code=end

