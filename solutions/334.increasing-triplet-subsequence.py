#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#

# @lc code=start
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.sol1(nums)

    def sol1(self, nums) : 
        first = second = float('inf')
        for num in nums :
            if num < first : 
                first = num
            elif first < num < second : 
                second = num
            elif num > second > first :
                return True
        return False
# @lc code=end

