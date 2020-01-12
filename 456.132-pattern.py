#
# @lc app=leetcode id=456 lang=python3
#
# [456] 132 Pattern
#

# @lc code=start
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.sol1(nums)

    def sol1(self, nums) :
        start, end = 0, len(nums) - 1
        while start < end :
            if nums[start] < nums[end] :
                for num in nums[start : end + 1] :
                    if num > nums[end] : return True
                start += 1
            else : 
                end -= 1
        return False
        
# @lc code=end

