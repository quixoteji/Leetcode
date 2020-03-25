#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
import functools
class Solution:
    def sol1(self, nums) :
        diff = functools.reduce((lambda x, y : x ^ y), nums)
        diff &= -diff
        res = [0,0]
        for num in nums :
            if diff & num : res[0] ^= num
            else : res[1] ^= num
        return res

    def singleNumber(self, nums: List[int]) -> List[int]:
        return self.sol1(nums)
        
# @lc code=end

