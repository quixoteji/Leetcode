#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums :
            num = abs(num)
            nums[num - 1] = -1 * abs(nums[num])
        return [num for num in nums if num > 0]
        
# @lc code=end

